from django.db import models

# Create your models here.

    
class Blog(models.Model):
    title = models.CharField(max_length=50,blank=True, null=True)
    post_body = models.TextField()


    def __str__(self):
        return self.title
