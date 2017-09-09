from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _
from guardian.mixins import GuardianUserMixin

from profiles.validators import MimetypeValidator


class SNUser(AbstractUser, GuardianUserMixin):
    profile_pic = models.FileField(upload_to='profiles/pictures',
                                   validators=(
                                       MimetypeValidator(
                                           ('image/jpeg', 'image/png')
                                       ),
                                   ))


class SNGroup(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    profile_pic = models.FileField(upload_to='profiles/pictures',
                                   validators=(
                                       MimetypeValidator(
                                           ('image/jpeg', 'image/png')
                                       ),
                                   ))

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
    file = models.FileField(upload_to='posts/files')
    file_type = models.PositiveSmallIntegerField(choices=FILE_TYPES)

    def save(self, *args, **kwargs):
        pass
        #self.file_type = file.
