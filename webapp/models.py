from django.db import models


class Course(models.Model):
    name=models.CharField(max_length=30)
    fees=models.CharField(max_length=100000, )
    duration=models.CharField(max_length=100, )
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name


    
    
    



# Create your models here.
