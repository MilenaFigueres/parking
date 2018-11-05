from django.shortcuts import render
from django.http import HttpResponse
from parking_app.models import Vehicle, Own
from django.views.generic.base import TemplateView, View
from django.contrib.auth.forms import UserCreationForm



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
    

class AddVehicle(TemplateView):
    template_name = 'add_vehicle.html'

    def get_context_data(self, **kwargs):
        context = super(AddVehicle, self).get_context_data(**kwargs)
        own = Own.objects.filter(id=1)
        context['own'] = own
        return context

    #def post(self, request, *args, **kwargs):
   		#crear vehiculo

# class AddComplain(TemplateView, LoginRequiredMixin):
#     template_name = 'add_complain.html'

#     def get_context_data(self, **kwargs):
#         context = super(AddComplain, self).get_context_data(**kwargs)
#         complain = 
#     	return render(request, './add_complain.html', {})

