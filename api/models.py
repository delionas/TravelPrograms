from django.db import models
from django.contrib.auth.models import User
# Create your models here.
PRIORITY_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]


class Problem(models.Model):
    name = models.CharField(max_length=60),
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    age = models.IntegerField(default=0)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, default='In_progress')
    solution = models.TextField(default="no solution yet")
    assigned_user = models.ForeignKey(User,null=True,on_delete=models.CASCADE, related_name='assigned_user')
    resolved_user = models.ForeignKey(User, null=True ,on_delete=models.CASCADE, related_name='resolved_user')

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    # def __str__(self):
    #     return self.name

# class Group
# Aa1234567891!