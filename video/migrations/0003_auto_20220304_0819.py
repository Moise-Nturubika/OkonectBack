# Generated by Django 3.1.5 on 2022-03-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20220303_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(db_column='file', upload_to='media/video/'),
        ),
    ]
