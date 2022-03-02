from django.contrib import admin

# Register your models here.
from .models import (homepage,login,logout,post,teaching,non-teaching,teaching apply,non-teaching apply,create,register)

class RegisterAdmin(admin.ModelAdmin):
    model = Register
    search_fields = ('email_address',)
admin.site.register(homepage)
admin.site.register(register,RegisterAdmin)
admin.site.register(logout)
admin.site.register(post)
admin.site.register(teaching)
admin.site.register(non-teaching)
admin.site.register(teaching apply)
admin.site.register(non-teaching apply)
admin.site.register(create)
admin.site.register(login)
