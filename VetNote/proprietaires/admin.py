from django.contrib import admin

from .models import Proprietaire

class ProprietaireAdmin(admin.ModelAdmin):
    list_display= ('nom','prenom','email','num_phone','adresse','is_vet')
    list_display_links = ('nom','prenom')
    list_filter = ('nom','adresse')
    list_editable = ('is_vet',)
    list_per_page = 25

admin.site.register(Proprietaire, ProprietaireAdmin)