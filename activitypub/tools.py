from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def resolve_actor(actor: str):
    val = URLValidator(verify_exists=False)
    try:
        val(actor)
        return
    except ValidationError:
        return actor
