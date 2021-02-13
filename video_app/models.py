from django.db import models

class Video(models.Model):
    userName = models.CharField(max_length=25, primary_key=True, unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.userName + ' ' + str(self.count))