from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from parking_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url('', include('parking_app.urls')),
]
