from django.db import models

# Create your models here.
class Destination(models.Model):
	id = models.AutoField(primary_key=True)
	created = models.DateTimeField(auto_now_add=True)
	pending = models.BooleanField(default=True)
	lat = models.CharField(max_length=50)
	lon = models.CharField(max_length=50)

	class Meta:
	    ordering = ('created', )