# Generated by Django 2.2 on 2023-06-27 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.IntegerField(default=''),
        ),
    ]
