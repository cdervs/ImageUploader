from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=140, blank = False, null = False) #Blank = false means the field needs to be filled, null = False means it can't be blank, empty text etc.
    image = ImageField()
    
    def __str__(self):
        return self.text