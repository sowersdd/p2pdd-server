from django.db import models

# Create your models here.
class Destination(models.Model):
	id = models.AutoField(primary_key=True)
	created = models.DateTimeField(auto_now_add=True)
	pending = models.BooleanField(default=True)
	lat = models.CharField(max_length=50)
	lon = models.CharField(max_length=50)
	needs_approval = models.BooleanField(default=False)

	class Meta:
	    ordering = ('created', )
	    
class DestinationProgress(models.Model):
	id = models.AutoField(primary_key=True)
	created = models.DateTimeField(auto_now_add=True)
	current_lat = models.CharField(max_length=50)
	current_lon = models.CharField(max_length=50)
	destination_id = models.ForeignKey(Destination, on_delete=models.CASCADE)

	class Meta:
	    ordering = ('created',)