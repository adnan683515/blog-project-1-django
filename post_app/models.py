from django.db import models
from cetagory_app.models import add_cetagory
from author_app.models import add_author
# Create your models here.
class add_post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    cetagory = models.ManyToManyField(add_cetagory) #akta post multiple cetagoryi undare thakte pare,,akta cetagorir modde multiple post thake
    author = models.ForeignKey(add_author,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    