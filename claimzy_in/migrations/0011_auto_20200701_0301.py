# Generated by Django 3.0.7 on 2020-06-30 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('claimzy_in', '0010_auto_20200701_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='claimzy_in.Devices', unique=True),
        ),
    ]
