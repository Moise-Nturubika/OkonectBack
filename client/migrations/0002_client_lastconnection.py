# Generated by Django 3.1.5 on 2022-03-04 11:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='lastConnection',
            field=models.DateTimeField(db_column='lastConnection', default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]