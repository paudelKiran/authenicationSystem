from django.contrib import admin
from .models import User,Profile

class userAdmin(admin.ModelAdmin):
    # list_editable = ['is_read', 'message']
    list_display = ['email',]


class profileAdmin(admin.ModelAdmin):
    list_editable = ['is_verified']
    list_display = ['user','full_name','email_token','is_verified']
   

admin.site.register(User,userAdmin)
admin.site.register(Profile,profileAdmin)

