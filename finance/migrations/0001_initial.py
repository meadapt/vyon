import os
from dotenv import load_dotenv
from django.db import migrations
from django.contrib.auth import get_user_model

def create_superuser(apps, schema_editor):
    User = get_user_model()
    load_dotenv()
    username = os.environ.get('ADMIN_USER')
    password = os.environ.get('ADMIN_PWD')
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            password=password,
            email='admin@meadapt.com'
        )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
