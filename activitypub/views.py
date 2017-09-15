from django.views import View

from activitypub.models import Inbox


class InboxView(View):
    def post(self, request, actor):
        pass

class OutboxView(View):
    def get(self, request, actor, *args, **kwargs):
        Inbox.objects.filter(actor_id=actor)