from django.contrib import admin
from .models import UserProfile, Chellenge, TopicList, Comment


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Chellenge)
admin.site.register(TopicList)
admin.site.register(Comment)