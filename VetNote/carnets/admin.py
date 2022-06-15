from django.contrib import admin

from .models import Carnet, Consultation, CalVac

class CarnetAdmin(admin.ModelAdmin):
    list_display= ('nom','num_id','espece','race','couleur','proprietaire','pedigre','sterilise')
    list_display_links = ('nom','num_id')
    list_filter = ('proprietaire',)
    list_editable = ('pedigre','sterilise')
    search_fields = ('nom','espece','race','proprietaire')
    list_per_page = 3

class ConsultationAdmin(admin.ModelAdmin):
    list_display= ('nom','note','date_cons','poids_cons','taille_cons','prix')
    list_filter = ('nom',)


class CalVacAdmin(admin.ModelAdmin):
    list_display= ('nom','vaccin','daterappel_vac','date_vac','observations','praticien')
    list_filter = ('nom',)


admin.site.register(Carnet, CarnetAdmin)
admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(CalVac, CalVacAdmin)