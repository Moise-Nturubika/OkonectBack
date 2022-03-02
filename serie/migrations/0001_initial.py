# Generated by Django 3.1.5 on 2022-03-02 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=100)),
                ('poster', models.FileField(db_column='poster', upload_to='media/poster/serie/')),
                ('refUser', models.ForeignKey(db_column='refClient', on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
            options={
                'db_table': 'tbSerie',
            },
        ),
        migrations.CreateModel(
            name='Saison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rang', models.IntegerField(db_column='rang')),
                ('refSerie', models.ForeignKey(db_column='refSerie', on_delete=django.db.models.deletion.CASCADE, to='serie.serie')),
            ],
            options={
                'db_table': 'tbSaison',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rang', models.IntegerField(db_column='rang')),
                ('file', models.FileField(db_column='file', upload_to='media/serie/')),
                ('dateAjout', models.DateTimeField(auto_now_add=True, db_column='dateAjout')),
                ('refSaison', models.ForeignKey(db_column='refSaison', on_delete=django.db.models.deletion.CASCADE, to='serie.saison')),
            ],
            options={
                'db_table': 'tbEpisode',
                'managed': True,
            },
        ),
    ]
