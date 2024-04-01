# Generated by Django 2.2 on 2023-05-31 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20230531_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='phone',
            new_name='address2',
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.CharField(default='', max_length=111),
        ),
    ]