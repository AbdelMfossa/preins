from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from falshfsfse.models import Filieres, Institutions, Regions, Nations, Departements, Niveaus, TypeDiplomes, Mentions, DemandeChambres
from .forms import *
from django.core.cache import cache
from _datetime import datetime
import random
from xhtml2pdf import pisa
from django_xhtml2pdf.utils import pdf_decorator


# Create your views here.
current_registration = DemandeChambres()

def logement_search(request):
    # Page qui affiche le champs de recherche pour afficher ses infos
    context = {'search_form': Logement_SearchForm()}
    return render(request, 'logement/logement_search.html', context)

def logement_civilite(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    context = {'logement_civilite_form': Logement_CivilForm()}
    return render(request, 'logement/logement_civilite.html', context)

def logement_filiation(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    context = {'logement_filiation_form': Logement_FiliationForm()}
    return render(request, 'logement/logement_filiation.html', context)

def logement_faculte(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    context = {'logement_faculte_form': Logement_FaculteForm()}
    return render(request, 'logement/logement_faculte.html', context)

def logement_sport(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    context = {'logement_sport_form': Logement_SportForm()}
    return render(request, 'logement/logement_sport.html', context)

def logement_fiche(request, code):
    # Page qui affiche les informations d'un étudiant
    context = {}
    try:
        dossier_chambre = DemandeChambres.objects.get(num_ordre=code)
        context['dossier'] = dossier_chambre
    except DemandeChambres.DoesNotExist:
        import traceback
        traceback.print_exc()

    return render(request, 'logement/logement_fiche.html', context)


def generate_unique_code(date_of_birth):
    """
    Function use to generate a unique code form registration based on birth date of the user
    """
    date_of_birth = date_of_birth[::-1]  # Reverse date of birth
    date = date_of_birth.split('-')  # Remove - in date of birt
    date.pop(1)  # Remove month
    partial_code_1 = ''.join(date)  # Get the first partial code with on reversed day and year

    # Get current time to construct seed for random generation
    now = str(datetime.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '')
    seed = int(now + partial_code_1)  # Compose seed with current time and partial_code_1
    random.seed(seed)  # Feed random generator with the constructed seed

    # Generate random number of 4 digits based on the previous seed
    add_random = str(random.randint(1000, 9999))

    # Construct the second partial code by adding the last digit of the random number at the beginning of partial_code_1
    # And the first digit of the random number at the end of partial_code_1
    partial_code_2 = add_random[-1] + partial_code_1 + add_random[0]

    # Generate random position within the actual partial_code_2 to insert the 2 middle digits of random number
    random_index = random.randint(0, len(partial_code_2))

    # Construct the total code
    code = "1" + partial_code_2[:random_index] + add_random[1:3] + partial_code_2[random_index:]

    return code


def validation_step_civilite(request):
    """
        Partially save of data for step 1.
    """

    response = {}
    if request.method == 'POST':
        try:
            current_registration.prenom = request.POST['prenom']
            current_registration.nom = request.POST['nom']
            current_registration.date_nais = request.POST['datenaissance']
            current_registration.dateprecise = True if 'oui' in request.POST['dateprecise'] else False
            current_registration.handicap = True if 'oui' in request.POST['handicap'] else False
            current_registration.lieu_nais = request.POST['lieunaissance']
            current_registration.sexe = request.POST['sexe']
            current_registration.adresse_parent = request.POST['residence_parent']
            current_registration.tel = request.POST['telephone']
            current_registration.email = request.POST['email']
            current_registration.residence_actuelle = request.POST['residence']
            current_registration.num_ordre = generate_unique_code(str(current_registration.date_nais))

            cache.set(f'step_1_{current_registration.num_ordre}', request.POST)

            response['success'] = True
            response['code'] = current_registration.num_ordre
            return JsonResponse(response, status=200)
        except Exception as e:
            import traceback
            traceback.print_exc()
            response['success'] = False
            response['message'] = str(e)
            return JsonResponse(response, status=500)
    else:
        response['success'] = False
        response['message'] = 'Only available with POST method'
        return JsonResponse(response, status=405)


def validation_step_filiation(request):
    """
        Partially save of data for step 2.
    """
    code = 200
    response = {}
    if request.method == 'POST':
        try:
            nationality = Nations.objects.get(pk=request.POST['nationalite'])
            region = Regions.objects.get(pk=request.POST['regionorigine'])
            departement = Departements.objects.get(pk=request.POST['departementorigine'])

            current_registration.nationality = nationality
            current_registration.region_origine = region
            current_registration.dept_origine = departement
            current_registration.nom_pere = request.POST['nompere']
            current_registration.profession_pere = request.POST['professionpere']
            current_registration.nom_mere = request.POST['nommere']
            current_registration.telephone_parent = request.POST['professionmere']
            current_registration.profession_mere = request.POST['telephoneparents']
            current_registration.nom_urgence = request.POST['nomurgence']
            current_registration.tel_urgence = request.POST['telurgence']
            current_registration.adresse_urgence = request.POST['villeurgence']

            cache.set(f'step_2_{current_registration.num_ordre}', request.POST)

            response['success'] = True
            return JsonResponse(response, status=code)
        except Nations.DoesNotExist:
            code = 404
            response['success'] = False
            response['message'] = "This nationality doesn't exist"
        except Regions.DoesNotExist:
            code = 404
            response['success'] = False
            response['message'] = "This region doesn't exist"
        except Departements.DoesNotExist:
            code = 404
            response['success'] = False
            response['message'] = "This department doesn't exist"
        except Exception as e:
            code = 500
            response['success'] = False
            response['message'] = str(e)
        finally:
            return JsonResponse(response, status=code)
    else:
        response['success'] = False
        response['message'] = 'Only available with POST method'
        return JsonResponse(response, status=405)


def validation_step_etude(request):
    """
        Partially save of data for step 3.
    """
    code = 200
    response = {}
    if request.method == 'POST':
        try:
            faculte = Institutions.objects.get(pk=request.POST['faculte'])
            filiere = Filieres.objects.get(pk=request.POST['filiere'])
            mention = Mentions.objects.get(pk=request.POST['mentionbac'])

            current_registration.institution = faculte
            current_registration.filiere = filiere
            current_registration.niveau = request.POST['niveau']
            current_registration.mention = mention        
            current_registration.niveau_redouble = request.POST['niveaurepris']    
            current_registration.nmat = request.POST['matricule']         
            current_registration.cite = request.POST['nomcite']         
            current_registration.ancien_residant = True if 'OUI' in request.POST['renouvellement'] else False           
            current_registration.bat_no = request.POST['batiment']            
            current_registration.chambre_no = request.POST['chambre']            
            current_registration.chambre_type = request.POST['typechambre']            
            current_registration.premiere_annee_resi = request.POST['anneepre']         
            current_registration.derniere_annee_resi = request.POST['anneeder']

            cache.set(f'step_3_{current_registration.num_ordre}', request.POST)

            response['success'] = True
            return JsonResponse(response, status=code)
        except Institutions.DoesNotExist:
            code = 404
            response['success'] = False
            response['message'] = "This institution doesn't exist"
        except Filieres.DoesNotExist:
            code = 404
            response['success'] = False
            response['message'] = "This field of study doesn't exist"
        except Exception as e:
            import traceback
            traceback.print_exc()
            code = 500
            response['success'] = False
            response['message'] = str(e)
        finally:
            return JsonResponse(response, status=code)
    else:
        response['success'] = False
        response['message'] = 'Only available with POST method'
        return JsonResponse(response, status=405)


def validation_step_sport(request):
    """
        Partially save of data for step 4.
    """

    response = {}
    code = 200
    if request.method == 'POST':
        try:
            current_registration.list_sports = request.POST['sports']
            current_registration.list_arts = request.POST['arts']

            cache.set(f'step_4_{current_registration.num_ordre}', request.POST)

            response['success'] = True
            new_registration = current_registration
            new_registration.save()
            response['code'] = new_registration.num_ordre

            # Remove user cache
            cache.delete_many([f'step_1_{new_registration.num_ordre}',
                               f'step_2_{new_registration.num_ordre}',
                               f'step_3_{new_registration.num_ordre}',
                               f'step_4_{new_registration.num_ordre}'
                               ])
            return JsonResponse(response, status=code)
        except Exception as e:
            response['success'] = False
            response['message'] = str(e)
            code = 500
        finally:
            return JsonResponse(response, status=code)
    else:
        response['success'] = False
        response['message'] = 'Only available with POST method'
        code = 405
        return JsonResponse(response, status=code)



def get_step_data(request, step, code):
    """
    Endpoint to get step 1 data from cache
    """
    data = cache.get(f'step_{step}_{code}')
    if data is not None:
        data = dict(data)
        data.pop('csrfmiddlewaretoken')
    else:
        data = {}
    return JsonResponse(data)



""" GENERATEUR DE PDF POUR LA FICHE D'INSCRIPTION
    -----------------------------------------------------------------------
"""

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

data = { }

# Opens up page as PDF
class Logement_ViewPDF(View):
    def get(self, request, code, *args, **kwargs):
        # pdf qui affiche les informations d'un étudiant
        context = {}
        try:
            dossier_univ = DemandeChambres.objects.get(num_ordre=code)
            context['dossier'] = dossier_univ
        except DemandeChambres.DoesNotExist:
            import traceback
            traceback.print_exc()

        pdf = render_to_pdf('logement/logement_pdf_template.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


# Automaticaly downloads to PDF file
class Logement_DownloadPDF(View):
    def get(self, request, code, *args, **kwargs):

        context = {}
        try:
            dossier_univ = DemandeChambres.objects.get(num_ordre=code)
            context['dossier'] = dossier_univ
        except DemandeChambres.DoesNotExist:
            import traceback
            traceback.print_exc()

        pdf = render_to_pdf('logement/logement_pdf_template.html', context)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Fiche_preinscription_%s.pdf" % (code)
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response