from django.db import models


class BigBigField(models.TextField):
    def to_python(self, value):
        if isinstance(value, str):
            return int(value)
        if value is None:
            return 0
        return int(str(value))

    def get_prep_value(self, value):
        if value is None:
            return 0
        return str(value)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return 0
        return int(value)


class Auth(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    me = models.BooleanField(default=False)

    def __str__(self):
        return self.url


class Key(models.Model):
    p = BigBigField()
    g = BigBigField()
    y = BigBigField()
    x = BigBigField(blank=True, null=True)

    def __str__(self):
        if self.x:
            return "{},{},{},{}".format(self.p, self.g, self.y, self.x)
        else:
            return "{},{},{}".format(self.p, self.g, self.y)
