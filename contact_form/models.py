from django.db import models


class ContactFormSubmission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=3000)
