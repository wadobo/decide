from django.db import models

from django.contrib.auth.models import User


class Census(models.Model):
    voting_id = models.PositiveIntegerField()
    voters = models.ManyToManyField(User, related_name='census')

    def __str__(self):
        return self.voting_id
