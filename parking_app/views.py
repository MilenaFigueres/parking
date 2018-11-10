from django.shortcuts import render
from django.http import HttpResponse
from parking_app.models import Vehicle, Own, Complain
from django.views.generic.base import TemplateView, View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


def index(request):
    return render(request, './index.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, '/registration/signup.html', {'form': form})
    

class AddVehicle(CreateView):
   template_name = 'add_vehicle.html'
   model = Vehicle
   fields = ['patent', 'color', 'model']

   def get_context_data(self, **kwargs):
       context = super(AddVehicle, self).get_context_data(**kwargs)
       own = Own.objects.get(id=1)
       context['own'] = own
       return context


class AddComplain(CreateView):
    template_name = 'add_complain.html'
    model = Complain
    vehicle = Vehicle.objects.get(id=1)
    fields = '__all__'

    def form_valid(self, form):
        form.instance.vehicle_id = self.kwargs.get('pk')
        return super(AddComplain, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddComplain, self).get_context_data(**kwargs)
        complain = Complain.objects.get(id=1)
        context['complain'] = complain
        return context

