# Generated by Django 3.1.5 on 2022-03-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_client_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='lastConnection',
            field=models.DateTimeField(db_column='lastConnection', null=True),
        ),
    ]
