from django.db import models
from client.models import Client

class Category(models.Model):
    designation = models.CharField(db_column="designation", max_length=100)
    
    class Meta:
        db_table = 'tbCategory'
        managed = True

class Media(models.Model):
    title = models.CharField(db_column="title", max_length=100)
    auteur = models.CharField(db_column="auteur", max_length=100, null=True, blank=True)
    poster = models.FileField(db_column="poster", upload_to='poster/video/', null=True, blank=True)
    file = models.FileField(db_column="file", upload_to="video/")
    dateAjout = models.DateTimeField(db_column="dateAjout", auto_now_add=True)
    refCategory = models.ForeignKey(Category, db_column="refCategory", on_delete=models.CASCADE)
    refClient = models.ForeignKey(Client, db_column="refClient", on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tbMedia'
        managed = True

