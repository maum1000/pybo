# Generated by Django 3.1.3 on 2024-08-28 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20240828_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
