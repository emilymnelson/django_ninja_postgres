# Generated by Django 5.0.6 on 2024-06-28 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cme_credits'),
    ]

    operations = [
        migrations.AddField(
            model_name='cme',
            name='status',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]