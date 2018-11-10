from django.conf.urls import url
from . import views
from parking_app.views import (
    AddVehicle,
    AddComplain,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^add_complain/', AddComplain.as_view(template_name='add_complain.html'), name='add_complain'),
    url(r'^add_vehicle/', AddVehicle.as_view(template_name='add_vehicle.html'), name='add_vehicle'),
    url('', views.index, name='index'),
]
