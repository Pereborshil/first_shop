from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    
class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    pass