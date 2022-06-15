from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from carnets.choices import Vaccins_choices, Espece_choices, Race_choices
from proprietaires.models import Proprietaire
from .models import CalVac


from .models import Carnet, Consultation

def index(request):
    carnets = Carnet.objects.all()

    paginator = Paginator(carnets, 3)
    page = request.GET.get('page')
    paged_carnets = paginator.get_page(page)

    context = {
        'carnets': paged_carnets
    }

    return render(request, 'carnets/carnets.html',context)

def carnet(request, carnet_id):
    carnet = get_object_or_404(Carnet, pk=carnet_id, )


    context = {
        'carnet' : carnet
    }
    return render(request, 'carnets/carnet.html',context)

def consultation(request, carnet_id):

    consultation = Consultation.objects.filter(nom__nom__iexact='Pichou')[:1]

    context = {
        'consultation' : consultation
    }

    return render(request, 'carnets/carnet.html',context)

def search(request):
    queryset_list = Carnet.objects.order_by('-nom')

    #proprietaire
    if 'proprietaire' in request.GET:
        proprietaire = request.GET['proprietaire']
        if proprietaire:
            queryset_list = queryset_list.filter(proprietaire__nom__iexact=proprietaire)

    #nom
    if 'nom' in request.GET:
        nom = request.GET['nom']
        if nom:
            queryset_list = queryset_list.filter(nom__iexact=nom)

    #race
    if 'race' in request.GET:
        race = request.GET['race']
        if race:
            queryset_list = queryset_list.filter(race__iexact=race)

    #espece
    if 'espece' in request.GET:
        espece = request.GET['espece']
        if espece:
            queryset_list = queryset_list.filter(espece__iexact=espece)

    context = {
        'Vaccins_choices' : Vaccins_choices,
        'Espece_choices' : Espece_choices,
        'Race_choices' : Race_choices,
        'carnets' : queryset_list
    }
    return render(request, 'carnets/search.html',context)

