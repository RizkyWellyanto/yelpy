from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.ForeignKey(User)

class Rating(models.Model):
    for_user = models.ForeignKey(User, help_text="User being rated", related_name='ratings')
    rater = models.ForeignKey(User, help_text="User submitting rating", related_name='submitted_ratings')

    review = models.TextField()
    score = models.FloatField()