# Generated by Django 2.2 on 2023-07-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_remove_checkout_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='amountt',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
