from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20, blank=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.points})"
