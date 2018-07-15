from django.db import models

class Message(models.Model):
    user = models.ForeignKey('auth.User')
    createtion_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()