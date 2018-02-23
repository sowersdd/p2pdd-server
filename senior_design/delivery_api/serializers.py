from django.contrib.auth.models import User, Group
from senior_design.delivery_api.models import Destination, DestinationProgress
from rest_framework import serializers
import requests
import os


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class DestinationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Destination
        fields = ('id', 'lat', 'lon', 'pending', 'needs_approval', 'created')

class DestinationAddressSerializer(serializers.HyperlinkedModelSerializer):
    address = serializers.SerializerMethodField()

    class Meta:
        model = Destination
        fields = ('id', 'lat', 'lon', 'pending', 'needs_approval', 'address', 'created')

    def get_address(self, obj):
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}".format(obj.lat,obj.lon,os.environ['MAPS_KEY'])
        response = requests.get(url).json()
        return "{} {}".format(response['results'][0]['address_components'][0]['short_name'],response['results'][0]['address_components'][1]['short_name'])

class DestinationProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationProgress
        fields = ('id', 'current_lat', 'current_lon', 'destination_id', 'created')