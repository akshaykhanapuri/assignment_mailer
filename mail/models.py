from django.db import models

# Create your models here.
class Mail(models.Model):
    rec_id = models.TextField()
    bcc = models.TextField()
    cc = models.TextField()
    sub = models.TextField()
    message = models.TextField()
    csv = models.FileField(upload_to='files/')
    mail_time = models.DateTimeField(auto_now = True)
