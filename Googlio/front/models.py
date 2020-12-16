from django.db import models

# Create your models here.

class Email(models.Model):
    user_name = models.CharField('User Name', unique=True, max_length=200)
    gmail = models.CharField(max_length=200)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    last_updated = models.DateTimeField('Last Updated', auto_now=True)
