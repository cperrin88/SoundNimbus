import json
from collections import OrderedDict

from django.http import HttpResponse
from django.views import View
from pyld import jsonld

from activitypub.models import Outbox
from activitypub.settings import ACTPUB_ACTOR_ID_FORMAT


class InboxView(View):
    def post(self, request, actor):
        pass


class OutboxView(View):
    def get(self, request, actor, *args, **kwargs):
        actor = request.build_absolute_uri(ACTPUB_ACTOR_ID_FORMAT.format(actor=actor))

        outbox = Outbox.objects.filter(actor=actor).values_list('data', flat=True)[:10]

        doc = {
            '@context': 'https://www.w3.org/ns/activitystreams',
            'id': actor,
            'type': 'OrderedCollection',
            'totalItems': len(outbox),
            'orderedItems': list(outbox)
        }

        out = json.dumps(doc)

        return HttpResponse(content=out, content_type='application/activity+json')
