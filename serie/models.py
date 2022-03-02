from django.db import models
from client.models import Client

class Serie(models.Model):
    title = models.CharField(db_column="title", max_length=100)
    poster = models.FileField(upload_to='media/poster/serie/', db_column="poster")
    refUser = models.ForeignKey(Client, db_column="refClient", on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tbSerie'

class Saison(models.Model):
    rang = models.IntegerField(db_column="rang")
    refSerie = models.ForeignKey(Serie, db_column="refSerie", on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tbSaison'
        managed = True
        
class Episode(models.Model):
    rang = models.IntegerField(db_column="rang")
    file = models.FileField(db_column="file", upload_to="media/serie/")
    dateAjout = models.DateTimeField(db_column="dateAjout", auto_now_add=True)
    refSaison = models.ForeignKey(Saison, db_column="refSaison", on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tbEpisode'
        managed = True
    