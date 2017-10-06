from django.conf import settings

SETTINGS = getattr(settings, 'ACTPUB_SETTINGS', {})

ACTPUB_ACTOR_ID_FORMAT = SETTINGS.get('ACTPUB_ACTOR_ID_FORMAT', '{actor}')
ACTPUB_BASE_URL = SETTINGS.get('ACTPUB_BASE_URL', '')
