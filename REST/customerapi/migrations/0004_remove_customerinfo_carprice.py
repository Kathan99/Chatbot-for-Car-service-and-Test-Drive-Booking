# Generated by Django 3.1.1 on 2020-09-23 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerapi', '0003_auto_20200923_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerinfo',
            name='carprice',
        ),
    ]
