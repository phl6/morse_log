from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class userScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    score = models.IntegerField(default=0)