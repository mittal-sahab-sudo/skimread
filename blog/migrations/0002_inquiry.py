# Generated by Django 3.1.4 on 2021-05-14 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
