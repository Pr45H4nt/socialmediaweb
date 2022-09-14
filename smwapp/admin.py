from django.contrib import admin
from .models import comments, likes , post

# Register your models here.
class postadmin(admin.ModelAdmin):
    list_display = ('user', 'status')
    list_filter = ('user',)

class commentadmin(admin.ModelAdmin):
    list_display = ('user', 'post' , 'comment')
    list_filter = ('post', 'user')
admin.site.register(post, postadmin)
admin.site.register(comments, commentadmin)
admin.site.register(likes)