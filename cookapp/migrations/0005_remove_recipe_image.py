# Generated by Django 2.2.4 on 2019-08-09 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookapp', '0004_auto_20190808_0049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
    ]
