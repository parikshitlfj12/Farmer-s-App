# Generated by Django 3.0.4 on 2020-07-18 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_auto_20200718_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorders',
            name='totalprice',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]