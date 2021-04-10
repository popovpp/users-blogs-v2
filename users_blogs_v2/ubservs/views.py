from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import FormView
from .models import User, Post, Blog
from .forms import PostForm, NewsForm, SetSubscriptionsForm, UserRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class PostList(ListView):
    model = Post
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['object_list'] = Post.objects.filter(author=self.request.user)
        return context


class PostCreate(FormView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    success_url = r'/post_list/'

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        if self.request.method == 'POST':
            blog, created = Blog.objects.get_or_create(author=self.request.user)
            if created:
                blog.save()
            form = PostForm(self.request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = self.request.user
                instance.save()
        return super(PostCreate, self).form_valid(form)

class SignUpView(generic.CreateView):
    form_class = UserRegistrationForm
    model = User
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
    def form_valid(self, form):
        if self.request.method == 'POST':
            form = UserRegistrationForm(self.request.POST)
            if form.is_valid():              
                instance = form.save(commit=False)
                instance.set_password(form.cleaned_data['password2'])
                instance.save()
            blog, created = Blog.objects.get_or_create(author=self.request.user)
            if created:
                blog.save()
        return super(SignUpView, self).form_valid(form)


class StartView(generic.ListView):
    template_name = 'index0.html'

    def get_queryset(self):       
        return []


class NewsList(FormView):
    model = User
    template_name = 'news.html'
    form_class = NewsForm
    success_url = '/news/' 
    
    def get_context_data(self, **kwargs):
        user = User.objects.get(username=self.request.user)
        context = super(NewsList, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        news_list = []
        for el in user.blogs_subcribe.all():
            news_list = list(news_list + list(Post.objects.filter(author=el.author.id)))
        for el in news_list:
            if el in user.read_posts.all():
                el.not_read = False
            else:
                el.not_read = True
        context['object_list'] = news_list
        return context

    def form_valid(self, form, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        return super(NewsList, self).form_valid(form)

    def post_red(request, post_id):
        user = User.objects.get(username=request.user)
        instance = get_object_or_404(Post, id=post_id)
        if request.method == 'POST':
            form = NewsForm(request.POST)
            if form.is_valid():
                user.read_posts.add(instance)
                user.save()  
        news_list = []
        for el in user.blogs_subcribe.all():
            news_list = list(news_list + list(Post.objects.filter(author=el.author.id)))
        for el in news_list:
            if el in user.read_posts.all():
                el.not_read = False
            else:
                el.not_read = True
        context = {
            'object_list': news_list,
            'form': form}
        return render(request, 'news.html', context)


class ScrView(FormView):
    form_class = SetSubscriptionsForm
    model = User
    template_name = 'Subscriptions.html'
    success_url = r'/subscriptions/'
    
    def get_context_data(self, **kwargs):
        context = super(ScrView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        user_subs = User.objects.get(username=self.request.user).blogs_subcribe.all()
        context['blogs_authors1'] = [x.author.username for x in user_subs]
        return context

    def form_valid(self, form):
        user = User.objects.get(username=self.request.user)
        user_subs = user.blogs_subcribe.all()
        blogs_authors = [x.author for x in user_subs]
        current_user = self.request.user
        clicked_user_list = list(form.cleaned_data['blogs_subcribe'])
        if current_user in clicked_user_list:
            clicked_user_list.remove(current_user)
        for ele in clicked_user_list:
            if ele in blogs_authors:
                if 'unsubscribe' in self.request.POST:
                    b = Blog.objects.get(author=ele)
                    user.blogs_subcribe.remove(b)
                    for el in user.read_posts.all():
                        if el.author == b.author:
                            user.read_posts.remove(el)
            elif ele not in blogs_authors:
                if 'subscribe' in self.request.POST:
                    blog, created = Blog.objects.get_or_create(author=ele)
                    user.blogs_subcribe.add(blog)
        user.save()
        return super(ScrView, self).form_valid(form)
