from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Vote(models.Model):
    VOTE_CHOICES = [
        ('RED', 'Red'),
        ('ORANGE', 'Orange'),
        ('GREEN', 'Green'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10, choices=VOTE_CHOICES)
    question = models.CharField(max_length=100, default='codebase-quality')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.vote_type}"
    

class CustomUser(AbstractUser):
    role = models.CharField(max_length=100, blank=True)
    