from django.contrib import admin
from falshfsfse.models import *


# Register your models here.

class InstitutionsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(DossierUnivs)
admin.site.register(Regions)
admin.site.register(Departements)
admin.site.register(Arrondissements)
admin.site.register(Institutions, InstitutionsAdmin)
admin.site.register(Filieres)
admin.site.register(Nations)
admin.site.register(TypeDiplomes)
admin.site.register(Niveaus)
admin.site.register(Specialites)
admin.site.register(Users)
admin.site.register(LieuDepots)
admin.site.register(Mentions)
admin.site.register(Papers)
