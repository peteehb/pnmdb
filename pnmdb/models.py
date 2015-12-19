from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return "%s" % self.name


class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return "%s" % self.name


class Player(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    team = models.ForeignKey(Team)

    POSITION_CHOICES = (
        ('Goalkeeper', 'Goalkeeper'),
        ('Defender', 'Defender'),
        ('Midfielder', 'Midfielder'),
        ('Forward', 'Forward')
    )
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
