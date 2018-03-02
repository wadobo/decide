from django.db import models


class Vote(models.Model):
    voting_id = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()

    a = models.PositiveIntegerField()
    b = models.PositiveIntegerField()

    voted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {}'.format(self.voting_id, self.voter_id)
