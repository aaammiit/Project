from django.db import models

# Create your models here.

class Category(models.Model):
    categroy=models.CharField(max_length=500)

    def __str__(self):
        return self.categroy

class keyWords(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    keyword=models.CharField(max_length=300)
    urlKeyWord=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.keyword


class newsModel(models.Model):
    keyWord=models.ForeignKey(keyWords,on_delete=models.CASCADE)
    newsTitle=models.TextField()
    newsUrl=models.URLField()
    newsDate=models.CharField(max_length=400)
    isScraped=models.BooleanField(default=False)
    newsAgency=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.keyWord.keyword



class newsArticle(models.Model):
    news=models.ForeignKey(newsModel,on_delete=models.CASCADE)
    newsarticle=models.TextField()
    scrapingDate=models.DateField(auto_now=True)
    gptSummary=models.TextField(null=True)
    isEdited=models.TextField(null=True)

    def __str__(self):
        return self.news.newsTitle


