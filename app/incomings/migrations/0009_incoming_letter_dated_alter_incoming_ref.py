# Generated by Django 5.1.2 on 2024-11-01 21:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomings', '0008_alter_incoming_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='incoming',
            name='letter_dated',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='incoming',
            name='ref',
            field=models.CharField(default='TyvMETBrqK', max_length=10, unique=True),
        ),
    ]
