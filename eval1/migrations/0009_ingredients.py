# Generated by Django 3.2.9 on 2021-11-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval1', '0008_alter_history_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField(max_length=100)),
                ('price', models.IntegerField()),
                ('supplier_name', models.TextField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
