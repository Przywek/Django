from django.db import models

# Create your models here.
class Users(models.Model):
    first_name= models.CharField(max_length=256)
    last_name= models.CharField(max_length=256)
    email= models.EmailField()
    def __str__(self):
        return (str(self.last_name) + ' ' + str(self.last_name))