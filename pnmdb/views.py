from django.contrib.auth.models import User, Group
from .models import Team, Club, Player
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, ClubSerializer, TeamSerializer, PlayerSerializer


class UserViewSet(viewsets.ModelViewSet):
	"""API endpoint that allows users to be viewed or edited."""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ClubViewSet(viewsets.ModelViewSet):
    """Club endpoint
    """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """Teams endpoint
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
	"""Players endpoint
    """
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer
