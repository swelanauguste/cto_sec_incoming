# Generated by Django 5.1.2 on 2024-11-01 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incoming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('received_on', models.DateField(blank=True, null=True)),
                ('conf', models.BooleanField(default=False)),
                ('urgent', models.BooleanField(default=False)),
                ('received_from', models.CharField(max_length=100)),
                ('note', models.TextField(blank=True, null=True)),
                ('originally_from', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('dated', models.DateField(blank=True, null=True)),
                ('subject', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='incoming_files/')),
                ('file1', models.FileField(blank=True, null=True, upload_to='incoming_files/')),
            ],
            options={
                'ordering': ['-received_on'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('received', 'Received'), ('forwarded', 'Forwarded'), ('responded', 'Responded'), ('closed', 'Closed')], default='received', max_length=100)),
                ('note', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('incoming', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incomings.incoming')),
            ],
        ),
    ]
