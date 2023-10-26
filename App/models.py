from django.db import models

# Create your models here.
class Note(models.Model):
    notes = models.CharField(max_length=100)

    def __str__(self):
        return self.notes
    