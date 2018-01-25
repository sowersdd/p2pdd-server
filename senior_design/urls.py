from django.conf.urls import url, include
from rest_framework import routers
from senior_design.delivery_api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'destinations_pending', views.get_pending_destination)
router.register(r'destinations', views.DestinationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]