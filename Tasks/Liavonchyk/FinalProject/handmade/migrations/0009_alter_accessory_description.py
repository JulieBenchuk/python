# Generated by Django 3.2.16 on 2023-01-17 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handmade', '0008_auto_20230114_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='description',
            field=models.TextField(),
        ),
    ]
