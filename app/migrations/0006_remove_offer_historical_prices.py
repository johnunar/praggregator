# Generated by Django 3.1.2 on 2020-10-17 18:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0005_auto_20201017_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='historical_prices',
        ),
    ]
