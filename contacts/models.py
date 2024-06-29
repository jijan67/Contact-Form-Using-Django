from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    hobbies = models.CharField(max_length=255)

    def __str__(self):
        return self.name