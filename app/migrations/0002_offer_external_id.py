# Generated by Django 3.1.2 on 2020-10-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='external_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
