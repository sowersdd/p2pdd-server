from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from senior_design.delivery_api.models import Destination
from rest_framework import viewsets
from rest_framework.decorators import detail_route
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

def get_pending_destination(request, pk=None):
	if request.method == "GET":
		destination = Destination.objects.filter(pending=True).order_by('created')
		if len(destination) > 0:
			destination = destination[0]
			destination.pending = False
			serializer = DestinationSerializer(destination)
			destination.save()
			return JsonResponse(serializer.data)
		else:
			return HttpResponse(status=418)
	else:
		return HttpResponse(status=400)
