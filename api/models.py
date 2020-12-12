from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=50)
    card_no = models.IntegerField()
    expiry = models.DateField()
    cvv = models.IntegerField()

    def __str__(self):
        return self.name
