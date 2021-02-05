from django.db import models


class ContactFormSubmission(models.Model):
    SUBJECT_CHOICES = [
        ('Account',) * 2,
        ('Payment',) * 2,
        ('General feedback',) * 2,
        ('Other',) * 2,
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField()
    subject = models.CharField(max_length=200, choices=SUBJECT_CHOICES)
    message = models.CharField(max_length=3000)
