# Generated by Django 3.0.2 on 2021-02-26 18:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('claimzy_in', '0017_auto_20210222_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
