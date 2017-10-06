from django.conf.urls import url
from activitypub.apps import ActivityPubConfig
from activitypub.views import OutboxView, InboxView

app_name = ActivityPubConfig.name

urlpatterns = [
    url(r'^(?P<actor>.*)/outbox.json$', OutboxView.as_view(), name="inbox"),
    url(r'^(?P<actor>.*)/inbox.json$', InboxView.as_view(), name="outbox"),
]
