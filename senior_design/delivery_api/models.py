from django.db import models

# Create your models here.
class Destination(models.Model):
	id = models.IntegerField(primary_key=True)
	created = models.DateTimeField(auto_now_add=True)
	lat = models.CharField(max_length=50)
	lon = models.CharField(max_length=50)
	pending = models.BooleanField(default=True)

	class Meta:
	    ordering = ('created', )