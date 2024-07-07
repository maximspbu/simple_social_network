from django.db import models

# Create your models here.

class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)
    
    def id_less_than_ten(self):
        return True if self.id < 10 else False
