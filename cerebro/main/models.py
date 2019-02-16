from django.db import models

class AGAMember(models.Model):
    """Represents a row in our CSV file, which contains info for one AGA member"""
    name = models.CharField(max_length=30)
    aga_id = models.PositiveIntegerField()
    chapter = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    rating = models.FloatField()
    sigma = models.FloatField()
    expiry = models.DateField()
    updated = models.DateField()
    mtype = models.CharField(max_length=30)

    class Meta:
        db_table = 'aga_members'

