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
    success_url = r'/'
    
    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        if self.request.method == 'POST':
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
#                instance = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['password2'])
#                instance.username = form.cleaned_data['username']
                instance.set_password(form.cleaned_data['password2']) #= form.cleaned_data
                instance.save()
        return super(SignUpView, self).form_valid(form)

#class NewsList(FormView):
#    model = News
#    template_name = 'news.html'
#    form_class = NewsForm
#    success_url = '/news/' 
    
#    def get_context_data(self, **kwargs):
#        context = super(NewsList, self).get_context_data(**kwargs)
#        context['user'] = self.request.user
#        context['object_list'] = News.objects.filter(owner=self.request.user)
#        return context

#    def form_valid(self, form, **kwargs):
#        context = super(NewsList, self).get_context_data(**kwargs)
#        print('In News form_valid')
#        print(self.render_to_response(context))
#        print(form.cleaned_data)
#        print(self.request.POST)
#        return super(NewsList, self).form_valid(form)

#    def post_red(request, idPost):
#        instance = get_object_or_404(News, idPost=idPost)
#        if request.method == 'POST':
#            form = NewsForm(request.POST)
#            if form.is_valid():
#                instance.notRead = form.instance.notRead
#                instance.save(force_update=True)
#        context = {
#            'object_list': News.objects.filter(owner=request.user),
#            'form': form
#        }
#        return render(request, 'news.html', context)



#class ScrView(FormView):
#    form_class = SubscriptionsForm
#    model = Subscriptions
#    template_name = 'Subscriptions.html'
#    success_url = r'/subscriptions/'
    
#    def get_context_data(self, **kwargs):
#        context = super(ScrView, self).get_context_data(**kwargs)
#        context['user'] = self.request.user
#        context['authorSub_list'] = Subscriptions.objects.filter(owner=self.request.user)
#        return context

#    def form_valid(self, form):
#        authorSubs = Subscriptions.objects.filter(owner=self.request.user)
#        authorSubs_list = [x.authorSub for x in authorSubs]
#        request_POST = self.request.POST
#        current_user = self.request.user
#        clicked_user = list(form.cleaned_data['authorSub'])
#        if current_user in clicked_user:
#            clicked_user.remove(current_user)
#        for ele in clicked_user:
#            el = Subscriptions.objects.filter(owner=current_user, authorSub=str(ele))
#            if len(el) != 0:
#                print(dict(self.request.POST))
#                if 'unsubscribe' in self.request.POST:
#                    el.delete()
#            else:
#                if 'subscribe' in self.request.POST:
#                    el = Subscriptions()
#                    el.owner = current_user
#                    el.authorSub = ele
#                    el.save()
#         return super(ScrView, self).form_valid(form)
