# Generated by Django 3.1.5 on 2022-03-29 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='canal',
            name='description',
            field=models.CharField(db_column='description', max_length=255, null=True),
        ),
    ]