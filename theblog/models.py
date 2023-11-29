from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class post(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    title_tag=models.CharField(max_length=255,null=True,blank=True,default="my blog")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
    image=models.ImageField(upload_to="profile/",null=True,blank=True)
    # body = models.TextField()
    publication_date=models.DateField(auto_now_add=True,)
    category=models.CharField(max_length=255,default="coding")
    snippet=models.CharField(max_length=255)
    like=models.ManyToManyField(User,related_name='blog_posts')


    def total_likes(self):
        return self.like.count()


    def __str__(self):
        return self.title + '  | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
class profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)          #association
    bio = models.TextField()
    profile_image=models.ImageField(upload_to="images/profile/",null=True,blank=True)
    website_url=models.CharField(max_length=255,null=True,blank=True)
    facebook_url=models.CharField(max_length=255,null=True,blank=True)
    instagram_url=models.CharField(max_length=255,null=True,blank=True)
    twitter_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.user)
class Command(models.Model):
    post= models.ForeignKey(post,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.post.title, self.name)
