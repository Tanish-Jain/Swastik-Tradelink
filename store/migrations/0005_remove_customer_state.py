# Generated by Django 3.1.7 on 2021-03-25 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210325_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='state',
        ),
    ]
