# Generated by Django 5.1 on 2024-09-03 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.lists')),
            ],
        ),
    ]
