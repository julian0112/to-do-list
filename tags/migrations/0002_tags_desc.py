# Generated by Django 5.1 on 2024-08-21 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
