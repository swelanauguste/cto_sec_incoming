# Generated by Django 5.1.2 on 2024-11-01 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomings', '0009_incoming_letter_dated_alter_incoming_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incoming',
            name='received_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incoming',
            name='ref',
            field=models.CharField(default='G9Spw5aZLK', max_length=10, unique=True),
        ),
    ]