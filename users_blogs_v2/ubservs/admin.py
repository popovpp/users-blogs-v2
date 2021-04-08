from django.contrib import admin

from .models import User, Post, Blog


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'show_blogs_suscribe', 
                    'show_read_posts']
    list_display_links = ['username']
    search_fields = ['username', 'email']

    class Meta:
        model = User

    def show_blogs_suscribe(self, obj):
        return ", ".join([a.author for a in obj.blogs_suscribe.all()])

    def show_read_posts(self, obj):
        return ", ".join([str(a.id) for a in obj.read_posts.all()])


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'author', 'timestamp']
    list_display_links = ['title']
    search_fields = ['title', 'author']

    class Meta:
        model = Post


class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'show_posts']
    list_display_links = ['id']
    search_fields = ['author']

    class Meta:
        model = Blog

    def show_posts(self, obj):
        return ", ".join([str(a.id) for a in obj.posts.all()])


admin.site.register(User, UserModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Blog, BlogModelAdmin)
