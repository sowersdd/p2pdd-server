from django.conf.urls import url, include
from rest_framework import routers
from senior_design.delivery_api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'destinations', views.DestinationViewSet)
router.register(r'destination_progresses', views.DestinationProgressViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'destinations/pending', views.get_pending_destination),
	url(r'destinations/approval', views.get_approval),
	url(r'destinations/(?P<pk>[0-9]+)/approval', views.submit_approval),
	url(r'destinations/(?P<pk>[0-9]+)/progress', views.get_destination_progress),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]