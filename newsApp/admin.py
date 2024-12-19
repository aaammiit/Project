from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(keyWords)
admin.site.register(newsModel)
admin.site.register(newsArticle)