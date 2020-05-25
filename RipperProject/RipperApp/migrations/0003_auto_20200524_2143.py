# Generated by Django 3.0 on 2020-05-25 02:43

import RipperApp.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RipperApp', '0002_delete_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=RipperApp.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])]),
        ),
    ]
