from django.contrib.auth.models import User, Group
from senior_design.delivery_api.models import Destination
from rest_framework import viewsets
from senior_design.delivery_api.serializers import UserSerializer, GroupSerializer, DestinationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
