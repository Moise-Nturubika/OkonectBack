# Generated by Django 3.1.5 on 2022-03-04 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20220304_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(db_column='file', upload_to='video/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='poster',
            field=models.FileField(db_column='poster', null=True, upload_to='poster/video/'),
        ),
    ]
