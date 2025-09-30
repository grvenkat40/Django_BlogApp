from django.contrib import admin
from .models import post,Category,Feedback

admin.site.register(post)
admin.site.register(Category)
admin.site.register(Feedback)