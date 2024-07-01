# Generated by Django 5.0.6 on 2024-06-27 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CME',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
                ('hospital', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cme',
            },
        ),
    ]