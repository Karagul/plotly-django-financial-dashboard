# Generated by Django 2.0.1 on 2018-02-03 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180203_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='document',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
