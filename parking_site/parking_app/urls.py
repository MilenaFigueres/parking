from django.conf.urls import url
from parking_app.views import (
    Home,
)

urlpatterns = [
    url('', Home.as_view(template_name='index.html'), name='index'),
]
