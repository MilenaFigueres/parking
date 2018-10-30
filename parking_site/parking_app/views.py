from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from parking_app.models import Car, Own


class Home():
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super(Home, self).get_context_data(**kwargs)
    #     own = Own.objects.all()
    #     car = Car.objects.filter()
    #     # context['pagination'] = pagination
    #     pass
