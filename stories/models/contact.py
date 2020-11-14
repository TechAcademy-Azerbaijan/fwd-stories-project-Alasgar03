from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=500)


    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
 