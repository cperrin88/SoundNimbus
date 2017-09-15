from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class ActivityPubObject(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    type = models.CharField(max_length=255)

    class Meta:
        abstract = True


class ActivityPubCollection(ActivityPubObject):
    actor_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='+')
    actor_id = models.CharField(max_length=255)
    actor = GenericForeignKey('actor_type', 'actor_id')

    object_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='+')
    object_id = models.CharField(max_length=255)
    object = GenericForeignKey('object_type', 'object_id')

    class Meta:
        abstract = True


class Outbox(ActivityPubCollection):
    pass


class Inbox(ActivityPubCollection):
    pass
