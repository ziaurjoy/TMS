# Generated by Django 3.1.2 on 2020-10-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20201008_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='title',
            field=models.TextField(max_length=200),
        ),
    ]
