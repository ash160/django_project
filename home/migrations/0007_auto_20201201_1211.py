# Generated by Django 3.1.3 on 2020-12-01 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201201_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filesupload',
            name='file',
        ),
        migrations.AddField(
            model_name='filesupload',
            name='document',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
