# Generated by Django 2.0.10 on 2019-04-30 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alertas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idAlert', models.IntegerField()),
                ('titulo', models.TextField()),
                ('descrip', models.TextField()),
                ('estado', models.TextField(max_length=1)),
                ('falta', models.DateTimeField(default=django.utils.timezone.now)),
                ('ffin', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField()),
            ],
        ),
    ]
