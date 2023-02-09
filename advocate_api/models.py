from django.db import models

class Advocate(models.Model):
    username = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    bio = models.TextField()
    profile_pic = models.ImageField(blank=True)
    twitter = models.CharField(max_length=200, null=True)
    joined_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    
