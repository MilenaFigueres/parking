from django.conf.urls import url
from . import views
from parking_app.views import (
    AddVehicle,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^add_vehicle/', AddVehicle.as_view(template_name='add_vehicle.html'), name='add_vehicle'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url('', views.index, name='index'),
]
