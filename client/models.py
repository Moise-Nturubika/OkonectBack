from django.db import models

class Client(models.Model):
    fullname = models.CharField(db_column="fullname", max_length=100)
    phone = models.CharField(db_column="phone", max_length=20)
    password = models.CharField(db_column="password", max_length=255)
    image = models.FileField(db_column="image", upload_to='client/profil/', null=True)
    lastConnection = models.DateTimeField(db_column="lastConnection")

    class Meta:
        db_table = 'tbClient'
        managed = True
        