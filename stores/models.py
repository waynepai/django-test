# encoding: utf-8
from django.db import models

# Create your models here.

class Store(models.Model):
    name  = models.CharField(max_length = 20)
    notes = models.TextField(blank = True, default = '')

    def __unicode__(self):
        return self.name

class MenuItem(models.Model):
    name  = models.CharField(max_length = 20)
    store = models.ForeignKey('Store', related_name='menu_items')
    price = models.IntegerField()

    def __unicode__(self):
        return self.name

