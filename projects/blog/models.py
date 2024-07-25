from django.conf import settings
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from django.contrib.auth.models import User


# class CustomUser(AbstractUser):
#    image = models.ImageField(upload_to="images/",null=True,blank=True)


class Category(models.Model):
    
    name = models.CharField(max_length=100,unique=True,null=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True,null=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
# def user_directory_path(instance,filename):
# 	return 'images/blog_{0}/'.format(instance.post.slug,filename)



class Post(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,default='')
    image = models.ImageField(upload_to="images/",null=True,blank=True)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True,null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')
    
    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()
    class Meta:
        ordering = ['created_on']
        
    def __str__(self):
        return self.text
    
