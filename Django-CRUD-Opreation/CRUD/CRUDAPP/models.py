from django.db import models

# Create your models here.
class Student(models.Model):
    S_id=models.IntegerField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    course=models.CharField(max_length=100)
    def __str__(self):
        return self.name