# Generated by Django 2.1.2 on 2018-10-24 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0003_auto_20181019_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]
