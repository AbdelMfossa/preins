from django.contrib import admin
from django.urls import include, path
from falshfsfse import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path('formulaire/', include('falshfsfse.urls')),
    path('logement/', include('logement.urls')),
    path('ecoledoctorale/', include('ecoledoctorale.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    url(r'^rosetta/', include('rosetta.urls'))
]
