from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
    user = models.ForeignKey(User, related_name='club', null=True)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return "%s" % self.name


class Team(models.Model):
    club = models.ForeignKey(Club, related_name='teams', null=True)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return "%s" % self.name


class Player(models.Model):
    team = models.ManyToManyField(Team, related_name='players')
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    POSITION_CHOICES = (
        ('Goalkeeper', 'Goalkeeper'),
        ('Defender', 'Defender'),
        ('Midfielder', 'Midfielder'),
        ('Forward', 'Forward')
    )
    position = models.CharField(max_length=64, choices=POSITION_CHOICES)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
