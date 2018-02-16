from django.contrib import admin

from .models import Auth, Key, Mixnet


admin.site.register(Auth)
admin.site.register(Key)
admin.site.register(Mixnet)
