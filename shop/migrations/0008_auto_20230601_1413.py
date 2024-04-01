# Generated by Django 2.2 on 2023-06-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20230531_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.CharField(max_length=50),
        ),
    ]