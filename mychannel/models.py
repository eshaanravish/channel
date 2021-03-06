# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from channels.binding.websockets import WebsocketBinding
from django.core.files import File


class IntegerValue(models.Model):

    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField(default=0)


class IntegerValueBinding(WebsocketBinding):

    model = IntegerValue
    stream = "intval"
    fields = ["name", "value"]

    @classmethod
    def group_names(cls, instance):
        return ["intval-updates"]

    def has_permission(self, user, action, pk):
        return True


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender")
    reciever = models.ForeignKey(User, related_name="reciever")
    message = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)
    is_seen = models.BooleanField(default=False)


class ChatboxUser(models.Model):
    user = models.ForeignKey(User)
    picture = models.ImageField(upload_to = 'media/', blank=True, null=True)
    is_online = models.BooleanField(default=False)
    bio = models.CharField(max_length=500)
    block_notifications_from = models.ManyToManyField(User, blank=True, related_name="blocked")