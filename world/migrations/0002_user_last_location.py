# Generated by Django 4.0 on 2022-11-02 20:18

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
