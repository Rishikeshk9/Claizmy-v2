# Generated by Django 3.0.2 on 2021-02-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claimzy_in', '0013_auto_20200808_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='last updated'),
        ),
    ]
