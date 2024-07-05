from django.db import models
from author_app.models import add_author
# Create your models here.
class profile (models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    author = models.OneToOneField(add_author,on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return self.name
    