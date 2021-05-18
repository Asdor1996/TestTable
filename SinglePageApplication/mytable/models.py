from django.db import models


class mytable(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    distance = models.IntegerField()
