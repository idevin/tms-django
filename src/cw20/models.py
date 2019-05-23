from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    age = models.IntegerField()
    profession = models.CharField(max_length=100, null=False)
