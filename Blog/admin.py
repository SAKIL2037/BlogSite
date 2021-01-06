from django.contrib import admin
from .models import BlogPost,Category

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_filter = ['created_at']
    search_fields = ['title','body']

admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Category)
