# Generated by Django 3.0.2 on 2020-02-25 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claimzy_in', '0004_auto_20200226_0311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devices',
            name='invoice_date',
        ),
    ]
