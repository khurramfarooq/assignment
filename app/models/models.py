from django.contrib.auth.models import User

from django.conf import settings
from django.db import models
from django.utils import timezone
from enum import Enum

# from app import celery_app
# from ..modules.constant import (
#     MESSAGE_PICK_UP,
#     MESSAGE_DROP_OFF
# )

class Status(Enum):
    UP = 'Up'
    DOWN = 'Down'
    SHUTDOWN = 'Shutdown'


class Router(models.Model):
    router_name = models.CharField(max_length=30, default='')


class Card(models.Model):
    router = models.ForeignKey(Router, on_delete=models.CASCADE, related_name='card')
    slot_number = models.IntegerField()
    card_name = models.CharField(max_length=30, default='')


class Interface(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='interface')
    local_interface = models.CharField(max_length=30, default='')
    remote_interface = models.CharField(max_length=30, default='', null=True)
    status = models.CharField(max_length=50, choices=[(st, st.value) for st in Status],
                                   default=Status.DOWN)
    connected_router = models.CharField(max_length=30, default='', null=True)

