from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
