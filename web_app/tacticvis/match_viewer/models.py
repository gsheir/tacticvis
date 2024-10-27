from django.db import models

# Create your models here.


class Match(models.Model):
    uuid = models.UUIDField(primary_key=True)
    statsbomb_id = models.IntegerField()
    date = models.DateTimeField()
    home_team = models.ForeignKey(
        "Team", on_delete=models.CASCADE, related_name="home_matches"
    )
    away_team = models.ForeignKey(
        "Team", on_delete=models.CASCADE, related_name="away_matches"
    )
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()

    def __str__(self):
        return self.match_id


class Team(models.Model):
    uuid = models.UUIDField(primary_key=True)
    statsbomb_id = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
