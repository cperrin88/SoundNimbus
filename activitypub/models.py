from django.contrib.postgres.fields import JSONField
from django.db import models


class ActivityPubObject(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    type = models.CharField(max_length=255)
    data = JSONField()


class Outbox(models.Model):
    actor = models.CharField(max_length=255)
    data = JSONField()


class Inbox(models.Model):
    actor = models.CharField(max_length=255)
    data = JSONField()
