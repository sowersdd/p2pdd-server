from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from senior_design.delivery_api.models import Destination, DestinationProgress
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from senior_design.delivery_api.serializers import UserSerializer, GroupSerializer, DestinationSerializer, DestinationProgressSerializer, DestinationAddressSerializer

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

class DestinationProgressViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = DestinationProgress.objects.all()
	serializer_class = DestinationProgressSerializer

def get_pending_destination(request, pk=None):
	if request.method == "GET":
		destination = Destination.objects.filter(pending=True).order_by('created')
		if len(destination) > 0:
			destination = destination[0]
			destination.needs_approval = True
			serializer = DestinationSerializer(destination)
			destination.save()
			return JsonResponse(serializer.data)
		else:
			return HttpResponse(status=418)
	else:
		return HttpResponse(status=400)

def get_destination_progress(request, pk=None):
	if request.method == "GET":
		progress = DestinationProgress.objects.filter(destination_id=pk).order_by('-created')
		if len(progress) > 0:
			progress = progress[0]
			serializer = DestinationProgressSerializer(progress)
			return JsonResponse(serializer.data)
		else:
			return HttpResponse(status=418)
	else:
		return HttpResponse(status=400)

def get_approval(request, pk=None):
	if request.method == "GET":
		dest = Destination.objects.filter(needs_approval=True).order_by('-created')
		if len(dest) > 0:
			dest = dest[0]
			serializer = DestinationAddressSerializer(dest)
			return JsonResponse(serializer.data)
		else:
			return HttpResponse(status=418)
	else:
		return HttpResponse(status=400)

def submit_approval(request, pk=None):
	if request.method == "GET":
		dest = Destination.objects.filter(id=pk).order_by('-created')
		if len(dest) > 0:
			dest = dest[0]
			dest.needs_approval = False
			dest.pending = False
			serializer = DestinationSerializer(dest)
			dest.save()
			return JsonResponse(serializer.data)
		else:
			return HttpResponse(status=418)
	else:
		return HttpResponse(status=400)
