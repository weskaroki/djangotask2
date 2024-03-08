from django.db import models

# Create your models here.
class register_form(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    phone_no= models.IntegerField()
    password = models.IntegerField()

    def __str__(self):
        return self.firstname

