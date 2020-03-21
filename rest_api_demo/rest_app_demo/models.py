from django.db import models


class Note(models.Model):
    notes = models.Manager()
    note_header = models.CharField(max_length=50)
    note_body = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)
    is_important = models.BooleanField(default=False)