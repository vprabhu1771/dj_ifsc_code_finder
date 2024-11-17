from django.db import models

# Create your models here.
class Bank(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "bank"

class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "country"

class State(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "state"

class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city'