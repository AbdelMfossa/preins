from django.urls import path
from falshfsfse.views import *

app_name = 'falshfsfse'

urlpatterns = [
    path('civilite/<int:fac>/', civilite, name='civilite'),
    path('civilite/', civilite, name='civilite'),
    path('filiation/', filiation, name='filiation'),
    path('faculte/', faculte, name='faculte'),
    path('diplome/', diplome, name='diplome'),
    path('sport/', sport, name='sport'),
    path('autre/', autres, name='autre'),
    path('searchdom_univ/', search, name='search'),
    path('fiche/<int:code>/', fiche, name='fiche'),
    path('fiche_view/<int:code>/', ViewPDF.as_view(), name='pdf_view'),
    path('fiche_download/<int:code>/', DownloadPDF.as_view(), name='pdf_download'),
    path('get_fields/', get_fields_from_school, name='get_fields'),
    path('get_supstudy/', get_supstudy, name='get_supstudy_link'),
    path('get_departments/', get_departements_from_region, name='get_departments'),
    path('step_1/', validation_step_civilite, name='civilite_step_1'),
    path('step_2/', validation_step_filiation, name='filiation_step_2'),
    path('step_3/', validation_step_etude, name='etude_step_3'),
    path('step_4/', validation_step_diplome, name='diplome_step_4'),
    path('step_5/', validation_step_sport, name='sport_step_5'),
    path('step_6/', validation_step_autre, name='autre_step_6'),
    path('get_step_data/<int:step>/<int:code>', get_step_data, name='get_step_data'),
]