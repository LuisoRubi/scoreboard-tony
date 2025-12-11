from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20, blank=True)
    points = models.IntegerField(default=0)
    MAX_POINTS = 200

    @property
    def progress(self) -> int:
        if self.MAX_POINTS <= 0:
            return 0
        pct = (self.points / self.MAX_POINTS) * 100
        pct = max(0, min(100, pct))
        return int(pct)

    def __str__(self):
        return f"{self.name} ({self.points})"
