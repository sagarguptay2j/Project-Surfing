# Generated by Django 3.0.3 on 2020-08-29 06:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 29, 6, 21, 52, 878147, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 29, 6, 21, 52, 878147, tzinfo=utc)),
        ),
    ]
