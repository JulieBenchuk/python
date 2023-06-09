# Generated by Django 4.1.5 on 2023-01-14 13:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
