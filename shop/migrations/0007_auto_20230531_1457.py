# Generated by Django 2.2 on 2023-05-31 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20230531_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address1',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address2',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
    ]
