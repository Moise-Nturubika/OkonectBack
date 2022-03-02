from django.db import models

class Client(models.Model):
    fullname = models.CharField(db_column="fullname", max_length=100)
    phone = models.CharField(db_column="phone", max_length=20)

    class Meta:
        db_table = 'tbClient'
        managed = True