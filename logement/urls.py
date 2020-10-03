from django.urls import path
from logement.views import *

app_name = 'logement'

urlpatterns = [
    path('logement_civilite/', logement_civilite, name='logement_civilite'),
    path('logement_filiation/', logement_filiation, name='logement_filiation'),
    path('logement_faculte/', logement_faculte, name='logement_faculte'),
    path('logement_sport/', logement_sport, name='logement_sport'),
    path('logement_search/', logement_search, name='logement_search'),
    
    path('logement_fiche/<int:code>/', logement_fiche, name='logement_fiche'),
    path('logement_fiche_download/<int:code>/', Logement_DownloadPDF.as_view(), name="logement_pdf_download"),
    path('logement_fiche_view/<int:code>/', Logement_ViewPDF.as_view(), name="logement_pdf_view"),

    path('step_1/', validation_step_civilite, name='civilite_step_1'),
    path('step_2/', validation_step_filiation, name='filiation_step_2'),
    path('step_3/', validation_step_etude, name='etude_step_3'),
    path('step_4/', validation_step_sport, name='sport_step_4'),
    path('get_step_data/<int:step>/<int:code>', get_step_data, name='get_step_data'),
]