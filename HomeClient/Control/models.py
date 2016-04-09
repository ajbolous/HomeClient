from __future__ import unicode_literals

from django.db import models

class Lamp(models.Model):
    pin = models.IntegerField()
    location = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return "Lamp: {},{},{}".format(self.pin, self.location, self.color)

    def __repr__(self):
        return "Lamp: {},{},{}".format(self.pin, self.location, self.color)

