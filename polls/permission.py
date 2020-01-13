from .models import Choice
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(Choice)
permission = Permission.objects.create(
    codename='can_view_and_delete_choice',
    name='Can View and Delete Choice',
    content_type=content_type,
)