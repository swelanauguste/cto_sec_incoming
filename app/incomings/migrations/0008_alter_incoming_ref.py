# Generated by Django 5.1.2 on 2024-11-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomings', '0007_incoming_slug_alter_incoming_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incoming',
            name='ref',
            field=models.CharField(default='ulewobipeX', max_length=10, unique=True),
        ),
    ]
