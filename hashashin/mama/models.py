from django.db import models
from django.db import models
class Users(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    password=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.age}"
