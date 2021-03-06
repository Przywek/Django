from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principle = models.CharField(max_length=256)
    Location = models.CharField(max_length=256)
    def __str__(self):
        return self.name
class Students(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)
    def __str__(self):
        return self.name