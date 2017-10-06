from django.contrib import admin

# Register your models here.
from django import forms

from activitypub.models import Outbox



class OutboxAdmin(admin.ModelAdmin):
    pass


admin.site.register(Outbox, OutboxAdmin)
