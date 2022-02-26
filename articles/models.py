from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from config.helpers import upload_file_name


class HomeCaruselModel(models.Model):
    title = models.CharField(verbose_name="title karusel", max_length=100)
    summary = models.CharField(max_length=250)
    body = RichTextField()
    def __str__(self):
        return self.title


class FutureModels(models.Model):
    folder = "future"
    title = models.CharField(max_length=250)
    descriptions = models.TextField()
    plan = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=upload_file_name, blank=True)

    def __str__(self):
        return self.title


class SubMenuModels(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=250, blank=True)
    web_address = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title


class MainSiteModels(models.Model):
    folder = 'mainsite'
    image = models.ImageField(upload_to=upload_file_name, blank=True)
    title = models.CharField(max_length=100)
    body = RichTextField()
    youtube_silka = models.CharField(max_length=100, blank=True)
    video = models.FileField(upload_to='upload/', blank=True)
    icon = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title


class About(models.Model):
    folder = 'about'
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250)
    body = RichTextField()
    image = models.ImageField(upload_to=upload_file_name, blank=True)

    def __str__(self):
        return self.title

class AboutMaydon(models.Model):
    maydon = models.FloatField()
    title = models.CharField(max_length=150)
    def __str__(self): 
        return self.title

class Newsmodel(models.Model):
    folder = 'news'
    image = models.ImageField(upload_to=upload_file_name)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=250)
    body = RichTextField()
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title

    # @property
    # def title(self):
    #     if len(self.title) < 100:
    #         return self.title
        
    #     return self.title[:100] + "..."
    
  

class NewsPrise(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    tarif = models.CharField(max_length=50, blank=True)
    plan = models.CharField(max_length=100, blank=True)
    
    def __str__(self) -> str:
        return self.title

class XodimModel(models.Model):
    folder = 'xodim'
    ism= models.CharField(max_length=250)
    lavozim = models.CharField(max_length=250)
    birth_day = models.DateField()
    image = models.ImageField(upload_to=upload_file_name, blank=True)

    def __str__(self) -> str:
        return self.ism