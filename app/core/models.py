from django.db import models

from django.db.models import fields
# Create your models here.

from solo.models import SingletonModel


class Settings(models.Model):
    setting1 = fields.BooleanField(default=False)
    setting2 = fields.BooleanField(default=False)
    setting3 = fields.BooleanField(default=False)


class SingletonSettings(SingletonModel):
    setting1 = fields.BooleanField(default=False)
    setting2 = fields.BooleanField(default=False)
    setting3 = fields.BooleanField(default=False)
