# Generated by Django 3.2.7 on 2021-09-23 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2021, 9, 23))),
                ('entry', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2021, 9, 23))),
                ('entry', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ToDoToday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentDate', models.DateField(default=datetime.date(2021, 9, 23))),
                ('entry', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ToDoWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('expiry', models.DateField()),
                ('is_expired', models.BooleanField(default=False)),
            ],
        ),
    ]
