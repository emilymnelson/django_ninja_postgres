from django.db import models

class CME(models.Model):
    year = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    credits = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    class Meta:
        db_table = 'cme'
