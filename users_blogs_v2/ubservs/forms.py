from django import forms
from .models import User, Post, Blog

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['id', 'title', 'text']


class NewsForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['read_posts']


class SetSubscriptionsForm(forms.ModelForm):

    

    blogs_subcribe = forms.ModelMultipleChoiceField(
        queryset = User.objects.all(), 
        widget  = forms.CheckboxSelectMultiple,
        label = 'Авторы постов'
    )
 #   print(blogs_subcribe)
    
#    def __init__(self, *args, **kwargs):
#        super(SetSubscriptionsForm, self).__init__(*args, **kwargs)
#        user = User.objects.get(username=kwargs['context']['user'])
#        self.fields['blogs_subcribe'].queryset = user.blogs_subcribe.all()


    class Meta:
        model = User
        fields = ['blogs_subcribe']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']