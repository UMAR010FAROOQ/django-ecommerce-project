# Generated by Django 2.2 on 2023-07-23 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20230723_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='amount',
        ),
    ]
