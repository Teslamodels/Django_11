from django.test import TestCase
from django.db import models

# Create your tests here.

class Message(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    