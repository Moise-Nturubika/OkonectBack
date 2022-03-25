from django.db import models
from client.models import Client

class Canal(models.Model):
    designation = models.CharField(db_column="designation", max_length=100)
    
    class Meta:
        db_table = 'tbCanal'
        
class Chat(models.Model):
    message = models.CharField(db_column="message", max_length = 255)
    dateMsg = models.DateTimeField(db_column="dateMsg", auto_now=True, auto_now_add=True)
    file = models.CharField(db_column="file", max_length=255, null=True)
    refCanal = models.ForeignKey(Canal, db_column="refCanal", on_delete=models.CASCADE, null=True)
    refClient = models.ForeignKey(Client, db_column="refClient", on_delete=models.CASCADE)
    refDestinateur = models.ForeignKey(Client, db_column="refDestinateur", on_delete=models.CASCADE, null=True)
    
    
    
# message, dateMsg, refCanal, refClient, refDestinateur, file