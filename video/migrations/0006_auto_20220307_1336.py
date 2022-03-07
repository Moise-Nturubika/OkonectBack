# Generated by Django 3.1.5 on 2022-03-07 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_media_refclient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='auteur',
            field=models.CharField(blank=True, db_column='auteur', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='poster',
            field=models.FileField(blank=True, db_column='poster', null=True, upload_to='poster/video/'),
        ),
    ]