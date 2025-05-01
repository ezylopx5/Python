from django.db import models

class Bot(models.Model):
    users_resposnd = models.CharField(max_length=255)
    bot_response = models.TextField()
    