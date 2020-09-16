from django.contrib import admin
from booktest.models import BookInfo,HeroInfo,User

# Register your models here.
admin.site.register(BookInfo)
admin.site.register(HeroInfo)
admin.site.register(User)
