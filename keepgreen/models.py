from django.db import models

# Create your models here.

class keepGreen(models.Model):
    fname = models.CharField(max_length=255, null=True)
    lname = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=13, unique=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.email