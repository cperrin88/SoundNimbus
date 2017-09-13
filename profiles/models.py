import magic
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _
from guardian.mixins import GuardianUserMixin


class SNUser(AbstractUser, GuardianUserMixin):
    profile_pic = models.ImageField(upload_to='profiles/pictures', null=True)


class SNGroup(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    profile_pic = models.ImageField(upload_to='profiles/pictures', null=True)

    class Meta:
        permissions = (
            ('member', _('Member')),
            ('editor', _('Editor')),
            ('admin', _('Administrator'))
        )


class Post(models.Model):
    FILE_TYPES = (
        (0, _('Video')),
        (1, _('Audio')),
        (2, _('Picture'))
    )

    message = models.TextField()
    posttime = models.DateTimeField(auto_now_add=True)
    edittime = models.DateTimeField(default=None, null=True, blank=True)
    file = models.FileField(upload_to='posts/files', null=True, blank=True)
    file_type = models.PositiveSmallIntegerField(choices=FILE_TYPES, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.file:
            mime = magic.from_buffer(self.file.read(1024), mime=True)
            if mime in ('image/jpeg', 'image/png',):
                self.file_type = 2
            if mime in ('audio/wave', 'audio/webm', 'audio/ogg', 'audio/mpeg'):
                self.file_type = 1
        else:
            self.file_type = None

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.message
