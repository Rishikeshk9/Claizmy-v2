# Generated by Django 3.0.7 on 2020-08-07 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claimzy_in', '0011_auto_20200701_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.CharField(choices=[('Under Review', 'Under Review'), ('Rejected', 'Rejected'), ('Being Processed', 'Being Processed'), ('Approved', 'Approved'), ('Complete', 'Complete')], default='Under Review', max_length=30),
        ),
    ]