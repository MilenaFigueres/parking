from django.conf.urls import url
from . import views
from parking_app.views import (
    AddVehicle,
)

urlpatterns = [
    url(r'^add_vehicle/', AddVehicle.as_view(template_name='add_vehicle.html'), name='add_vehicle'),
    url('', views.index, name='index'),
]
