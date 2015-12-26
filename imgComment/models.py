from django.db import models

# Create your models here.
class Image(models.Model):
    origFile = models.CharField(max_length = 200,default="None")
    editFile = models.CharField(max_length = 200,default="None")
    postTag = models.CharField(max_length = 20,default="None")
    url = models.CharField(max_length = 100,default="None")
    title = models.CharField(max_length = 100,default="None")
    uploadTime = models.DateTimeField(auto_now_add=True, blank=True)

class Comment(models.Model):
    image = models.ForeignKey(Image,on_delete=models.CASCADE,)
    text = models.CharField(max_length = 200,default="None")
    username = models.CharField(max_length = 20,default="None")
    commentType = models.CharField(max_length = 10,default="None")
    uploadTime = models.DateTimeField(auto_now_add=True, blank=True)