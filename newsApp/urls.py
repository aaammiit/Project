
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexPage),
    path('homePage',newshomePage),
    path('categroyNews/<int:id>',categroyNewsPage,name='categroyNews'),
    path('keyWordAllNews/<int:id>',keyWordAllNews),
    path('searchNews',searchKeywordNews),
    path('saveNewsInBucket',saveNewsInBucket),
    path('sendFile',sendFileInEmail),
    path('keyWordNews/<int:id>',keyWordNews),
    path('newsUrlScrap/<int:id>',newsUrlScrap),
    path('newsArticles',newsArticles),
    path('deleteAll',deleteAllData),
    path('remove/<int:id>',removeNews),
    path('editText/<int:id>',editArticle),
    path('gptSummary/<int:id>',gptSummary),
    path('saveContent',save_content, name='save_content'),
    path('updateArticleContent',update_article_content, name='update_article_content'),
    
]
