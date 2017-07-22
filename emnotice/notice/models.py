from django.db import models
from django.conf import settings
# Create your models here.
class Notice(models.Model):
    notice = models.TextField()
    to = models.ForeignKey(settings.AUTH_USER_MODEL)
    date =  models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.notice