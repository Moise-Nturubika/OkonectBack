# Generated by Django 3.1.5 on 2022-03-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_client_lastconnection'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='image',
            field=models.FileField(db_column='image', null=True, upload_to='client/profil/'),
        ),
    ]
