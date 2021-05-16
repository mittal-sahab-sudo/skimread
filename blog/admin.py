from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, Inquiry

class BlogPostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title','date_created')
    list_display_links = ('id','title')
    search_fields = ('title',)
    list_per_page = 25
    summernote_fields = ('content',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Inquiry)
