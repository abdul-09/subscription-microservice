
# ModelViewSet-based view
from django.urls import include, path
from rest_framework import routers
from .views import AddressViewSet

ver = 'v1'

router = routers.DefaultRouter()
router.register(f'api/{ver}/addresses', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

