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