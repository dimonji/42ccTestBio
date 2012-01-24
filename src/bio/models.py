"""
Django database models
"""
from django.db import models


class Human(models.Model):
    """
    Human data
    """
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    biography = models.TextField()


    def __unicode__(self):
        return " ".join([self.name, self.surname])

    class Meta(object):
        verbose_name_plural = "Humans"


class Contacts(models.Model):
    """
    Human contacts model
    """
    pass
