from django.db import models


class Auth(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    me = models.BooleanField(default=False)

    def __str__(self):
        return self.url


class Key(models.Model):
    p = models.IntegerField()
    g = models.IntegerField()
    y = models.IntegerField()
    x = models.IntegerField(blank=True, null=True)

    def __str__(self):
        if self.x:
            return "{},{},{},{}".format(self.p, self.g, self.y, self.x)
        else:
            return "{},{},{}".format(self.p, self.g, self.y)
