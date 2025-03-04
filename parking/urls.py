"""
URL configuration for parking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from management.api.views import ParkingViewSet, ParkingSpaceViewSet, TicketViewSet, list_parking_spaces, ReservationViewSet


router = SimpleRouter()

router.register("api/parking", ParkingViewSet, basename="parking")
router.register("api/parkingspaces", ParkingSpaceViewSet, basename="parking-spaces")
router.register("api/ticket", TicketViewSet, basename="tickets")
router.register("api/reservation", ReservationViewSet, basename="reservation")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('parking-spaces/<str:parking_id>/', list_parking_spaces, name='list_parking_spaces'),
]+router.urls
