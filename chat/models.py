from django.db import models
from client.models import Client
from video.models import Media

class Canal(models.Model):
    designation = models.CharField(db_column="designation", max_length=100)
    description = models.CharField(db_column="description", max_length=255, null=True)
    class Meta:
        db_table = 'tbCanal'
        
class Chat(models.Model):
    message = models.CharField(db_column="message", max_length = 255)
    dateMsg = models.DateTimeField(db_column="dateMsg", auto_now=True)
    refMedia = models.ForeignKey(Media, db_column="refMedia", on_delete=models.CASCADE, null=True)
    isPrivate = models.BooleanField(db_column="isPrivate")
    refCanal = models.ForeignKey(Canal, db_column="refCanal", on_delete=models.CASCADE, null=True)
    refClient = models.ForeignKey(Client, db_column="refClient", on_delete=models.CASCADE, related_name="refClient")
    refDestinateur = models.ForeignKey(Client, db_column="refDestinateur", on_delete=models.CASCADE,related_name="refDestinateur", null=True)
    
    class Meta:
        db_table = 'tbChat'
# message, dateMsg, refCanal, refClient, refDestinateur, file