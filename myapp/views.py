from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView


from .models import Zvire, Chovatel, Oceneni


def index(request):

 zvirata = Zvire.objects.all()

 context = {
 'zvirata': zvirata,

 }

 return render(request, 'index.html', context=context)

class ChovateleListView(ListView):
 model = Chovatel
 context_object_name = 'chovatele'
 template_name = 'chovatel/chovatele_list.html'


class ChovatelDetailView(DetailView):
 model = Chovatel
 context_object_name = 'chovatel'
 template_name = 'chovatel/chovatel_detail.html'