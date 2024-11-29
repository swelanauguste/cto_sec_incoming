# Generated by Django 5.1.2 on 2024-11-08 17:33

import django.db.models.deletion
import django.utils.timezone
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
                ('ref', models.CharField(default='v6JvOwWNKb', max_length=10, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=10, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('received_on', models.DateField(blank=True, null=True)),
                ('conf', models.BooleanField(default=False, verbose_name='confidential')),
                ('urgent', models.BooleanField(default=False)),
                ('received_from', models.CharField(blank=True, max_length=100, null=True, verbose_name='from')),
                ('note', models.TextField(blank=True, null=True)),
                ('originally_from', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('letter_dated', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('subject', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='incoming_files/')),
            ],
            options={
                'ordering': ['-received_on'],
            },
        ),
        migrations.CreateModel(
            name='ChangeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('received', 'Received'), ('forwarded', 'Forwarded'), ('responded', 'Responded'), ('closed', 'Closed')], default='received', max_length=100)),
                ('note', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='updated_files/')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('created', models.DateField(auto_now_add=True)),
                ('incoming', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='incomings.incoming')),
            ],
            options={
                'verbose_name_plural': 'Change Statuses',
                'ordering': ['-date'],
            },
        ),
    ]