# Generated by Django 2.1.2 on 2018-10-17 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='data',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
