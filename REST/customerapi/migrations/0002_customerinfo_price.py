# Generated by Django 3.1.1 on 2020-09-23 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinfo',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]