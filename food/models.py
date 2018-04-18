# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
# from django_countries.fields import CountryField
from django.db import models
from datetime import date


class Subscribed(models.Model):
    subscribed_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(blank=False, max_length=16)
    last_name = models.CharField(blank=False, max_length=16)
    age = models.PositiveIntegerField(blank=False)
    address = models.CharField(blank=False, max_length=64)
    # country = CountryField()
    postal_code = models.PositiveIntegerField()
    subscription_date = models.DateField(default=date.today)


class Food(models.Model):
    type = models.CharField(blank=False, max_length=32)
    name = models.CharField(blank=False, max_length=32)
    calories = models.PositiveIntegerField(blank=False)
    fats = models.PositiveIntegerField(blank=False)
    protein = models.PositiveIntegerField(blank=False)


class FoodOfer(models.Model):
    owner = models.ForeignKey(Subscribed, related_name='created_by')
    purchaser = models.ForeignKey(Subscribed, blank=True, null=True, related_name='bidded_by')
    food = models.ForeignKey(Food, related_name='contains')

    start_price = models.PositiveIntegerField(blank=False)
    actual_price = models.PositiveIntegerField(blank=False)
    last_price = models.PositiveIntegerField(blank=False)
    description = models.CharField(blank=False, max_length=64)
    available_time = models.PositiveIntegerField(blank=False)


class Bid(models.Model):
    bidder = models.ForeignKey(Subscribed, related_name='made_by')
    offer = models.ForeignKey(FoodOfer, related_name='done_on')

    amount = models.PositiveIntegerField(blank=False)


class Message(models.Model):
    send_by = models.ForeignKey(Subscribed, related_name='send_by')
    send_to = models.ForeignKey(Subscribed, related_name='send_to')
    body = models.CharField(blank=False, max_length=512)
    date = models.DateField(default=date.today)