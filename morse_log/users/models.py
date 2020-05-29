from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class userScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    score = models.IntegerField(default=0)

# Create your models here.
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     description = models.CharField(max_length=100, default='')
#     #score = models.CharField(User, max_length=10, default=0)
#
#
# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
#     post_save.connect(create_profile, sender=User)
#
#
# class UserScore(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     #user = models.ForeignKey(User, on_delete=models.CASCADE)
#     score = models.IntegerField(default=0)

    # def __str__(self):
    #     """Returns a string representation of the model"""
    #     return str(self.score)
