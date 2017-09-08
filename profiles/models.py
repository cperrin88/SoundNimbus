from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext as _


class SNUser(AbstractUser):
    pass


class SNGroup(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    members = models.ManyToManyField("SNUser")


class Follower(models.Model):
    follower_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                      related_name="follower_type")
    follower_id = models.PositiveIntegerField()
    follower = GenericForeignKey('follower_type', 'follower_id')
    followed_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                      related_name="followed_type")
    followed_id = models.PositiveIntegerField()
    followed = GenericForeignKey('followed_type', 'followed_id')


class Post(models.Model):
    FILE_TYPES = (
        (0, _("Video")),
        (1, _("Audio")),
        (2, _("Picture"))
    )

    author_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    author_id = models.PositiveIntegerField()
    author = GenericForeignKey('author_type', 'author_id')
    message = models.TextField()
    file = models.FileField()
    file_type = models.PositiveSmallIntegerField(choices=FILE_TYPES)
