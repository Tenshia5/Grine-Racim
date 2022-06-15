from django.shortcuts import render
from django.http import HttpResponse
from carnets.models import Carnet
from carnets.choices import Vaccins_choices, Espece_choices, Race_choices

def index(request):
    carnets = Carnet.objects.all()

    context = {
        'carnets': carnets,
        'Vaccins_choices' : Vaccins_choices,
        'Espece_choices' : Espece_choices,
        'Race_choices' : Race_choices
    }
    return render(request, 'pages/index.html',context)


#def about(request):
    #return render(request, 'pages/about.html')