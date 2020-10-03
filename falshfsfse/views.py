from django.shortcuts import render
from django.shortcuts import redirect
from io import BytesIO
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from django.views import View
from falshfsfse.models import Filieres, Institutions, Regions, DossierUnivs, Nations, Departements, Niveaus, TypeDiplomes, Mentions, Papers
from xhtml2pdf import pisa
from .forms import *
from django.core.cache import cache
from django_xhtml2pdf.utils import pdf_decorator
from _datetime import datetime
import random

FACULTE = {
    1: "Faculté des Arts, Lettres et Sciences Humaines (FALSH)",
    2: "Faculté des Sciences (FS)",
    3: "Faculté des Sciences de l'Education (FSE)",
    4: "Faculté de Médecine et des Sciences Biomédicales (FMSB)",
    5: "Ecole Nationale Supérieure Polytechnique de Yaoundé (ENSPY)",
    6: "Ecole Normale Supérieure (ENS)",
    7: "Ecole Normale Supérieure d'Enseignement Technique d'Ebolowa (ENSET)",
    8: "Institut Universitaire de Technologies du Bois de Mbalmayo (IUT Bois)",
}

current_registration = DossierUnivs()


# Create your views here.
def accueil(request):
    return render(request, 'falshfsfse/home.html')


def civilite(request, fac=1):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    # context = {'civilite_form': CivilForm(), 'filiation_form': FiliationForm()}
    fac = int(fac)
    if fac > 8 or fac < 1:
        fac = 1
    request.session['code_fac'] = fac
    request.session['fac'] = FACULTE[fac]
    context = {'civilite_form': CivilForm()}
    return render(request, 'falshfsfse/civilite.html', context)


def filiation(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    context = {'filiation_form': FiliationForm()}
    return render(request, 'falshfsfse/filiation.html', context)


def faculte(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    context = {'faculte_form': FaculteForm()}
    return render(request, 'falshfsfse/faculte.html', context)


def diplome(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    context = {'diplome_form': DiplomeForm()}
    return render(request, 'falshfsfse/diplome.html', context)


def sport(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    context = {'sport_form': SportForm()}
    return render(request, 'falshfsfse/sport.html', context)


def autres(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    context = {'autre_form': AutreForm()}
    return render(request, 'falshfsfse/autre.html', context)


def search(request):
    # Page qui affiche le champs de recherche pour afficher ses infos
    context = {'search_form': SearchForm()}
    return render(request, 'falshfsfse/search.html', context)


def fiche(request, code):
    # Page qui affiche les informations d'un étudiant
    context = {}
    try:
        dossier_univ = DossierUnivs.objects.get(num_ordre=code)
        context['dossier'] = dossier_univ
    except DossierUnivs.DoesNotExist:
        import traceback
        traceback.print_exc()

    return render(request, 'falshfsfse/fiche.html', context)


def get_fields_from_school(request):
    """
        :school_id: argument needed in POST dict
        Endpoint to get all fields concerning a specific school.
        :return
        {
            'success': True of False,
            'message': 'Error message in case of success `False`,
            data:   [
                        {
                            'id': ...,
                            'name': ...,
                        }
                    ]
        }
    """
    response = {}
    data = []
    if request.method == 'POST':
        try:
            s_id = request.POST['school_id']
            school = Institutions.objects.prefetch_related('filieres').get(id=s_id)
            for field in school.filieres.all():
                data.append(
                    {
                        'id': field.id,
                        'name': field.libelle
                    }
                )
            response['success'] = True
            response['message'] = ''
            response['data'] = data
            return JsonResponse(response, status=200)
        except Institutions.DoesNotExist:
            response['success'] = False
            response['message'] = "This school doesn't exist"
            return JsonResponse(response, status=404)
        except Exception as e:
            response['success'] = False
            response['message'] = e
            return JsonResponse(response, status=500)
    else:
        response['success'] = False
        response['message'] = 'Only available with POST method'
        return JsonResponse(response, status=405)


def get_supstudy(request):
    """
        :name: Name of the filiere it must be well spelled
        :return
        {
            'success': True of False,
            'message': 'Error message in case of success `False`,
            link: supstudy's link of the required filiere, or empty if Error
        }
    """
    response = {}
    if request.method == 'POST':
        try:
            name = request.POST['name']
            filiere = Filieres.objects.get(pk=name)
            response['success'] = True
            response['link'] = filiere.descprition_url
            response['name'] = filiere.libelle
            return JsonResponse(response, status=200)
        except Filieres.DoesNotExist:
            response['success'] = False
            response['error'] = 'This field of study does not exist'
            return JsonResponse(response, status=404)
        except Exception as e:
            response['success'] = False
            response['error'] = str(e)
            return JsonResponse(response, status=500)
    else:
        response['success'] = False
        response['message'] = 'Only available with POST method'
        return JsonResponse(response, status=405)


def get_departements_from_region(request):
    """
        :region_id: argument needed in POST dict
        Endpoint to get all departments concerning a specific region.
        :return
        {
            'success': True of False,
            'message': 'Error message in case of success `False`,
            data:   [
                        {
                            'id': ...,
                            'name': ...,
                        }
                    ]
        }
    """
    response = {}
    data = []
    if request.method == 'POST':
        try:
            r_id = request.POST['region_id']
            region = Regions.objects.prefetch_related('departements').get(id=r_id)
            for dep in region.departements.all():
                data.append(
                    {
                        'id': dep.id,
                        'name': dep.nom
                    }
                )
            response['success'] = True
            response['message'] = ''
            response['data'] = data
            return JsonResponse(response, status=200)
        except Regions.DoesNotExist:
            response['success'] = False
            response['message'] = "This region doesn't exist"
            return JsonResponse(response, status=404)
        except Exception as e:
            response['success'] = False
            response['message'] = str(e)
            return JsonResponse(response, status=500)
    else:
        response['success'] = False
        response['message'] = 'Only available with POST method'
        return JsonResponse(response, status=405)


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
    code = "2" + partial_code_2[:random_index] + add_random[1:3] + partial_code_2[random_index:]

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
            current_registration.lieu_nais = request.POST['lieunaissance']
            current_registration.num_cni = request.POST['numerocni']
            # current_registration.sexe = request.POST['sexe'].upper()
            current_registration.sexe = request.POST['sexe']
            current_registration.adresse_perso = request.POST['adresse']
            current_registration.tel = request.POST['telephone']
            current_registration.email = request.POST['email']
            current_registration.stat_matri = request.POST['statutmarital'].upper()
            current_registration.langue = request.POST['premierelangue']
            current_registration.sit_prof = request.POST['statutprofessionnel']
            current_registration.profession = request.POST['profession']
            current_registration.lieu_affectation = request.POST['lieudujob']
            current_registration.grade = request.POST['grade']
            current_registration.ech = request.POST['echelon']
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
            current_registration.profession_mere = request.POST['professionmere']
            current_registration.nom_urgence = request.POST['nomurgence']
            current_registration.tel_urgence = request.POST['telurgence']
            current_registration.ville_urgence = request.POST['villeurgence']

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
            choix_1 = Filieres.objects.get(pk=request.POST['premierchoix'])
            choix_2 = Filieres.objects.get(pk=request.POST['secondchoix'])
            choix_3 = Filieres.objects.get(pk=request.POST['troisiemechoix'])

            current_registration.institution = faculte
            current_registration.code_questionnaire = request.POST['questionnaire']
            current_registration.fil1 = choix_1
            current_registration.fil2 = choix_2
            current_registration.fil3 = choix_3
            current_registration.niv_acad = request.POST['niveau']
            current_registration.nature_candidat = request.POST['statutdesire']

            cache.set(f'step_3_{current_registration.num_ordre}', request.POST)

            # print(current_registration.institution)
            # current_registration.save()
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


def validation_step_diplome(request):
    """
            Partially save of data for step 1.
        """
    response = {}
    code = 200
    if request.method == 'POST':
        try:
            diplome = TypeDiplomes.objects.get(pk=request.POST['diplome'])
            mention = Mentions.objects.get(pk=request.POST['mention'])
            current_registration.type_diplome = diplome
            current_registration.serie = request.POST['serie']
            current_registration.annee_obtention = request.POST['anneeobtention']
            if request.POST['diplome'] != 3 or request.POST['diplome'] != 4:
                current_registration.moyenne = request.POST['moyenne']
            current_registration.mention = mention
            current_registration.dipl_etabl = request.POST['emetteur']
            current_registration.dipl_date_deli = request.POST['date_emission']
            if request.POST['diplome'] == 3 or request.POST['diplome'] == 4:
                current_registration.nbre_paper = request.POST['nombresoumis']
                current_registration.paper_1 = request.POST['papier1']
                current_registration.paper1_grade = request.POST['grade1']
                current_registration.paper_2 = request.POST['papier2']
                current_registration.paper2_grade = request.POST['grade2']
                current_registration.paper_3 = request.POST['papier3']
                current_registration.paper3_grade = request.POST['grade3']

            cache.set(f'step_4_{current_registration.num_ordre}', request.POST)

            response['success'] = True
            return JsonResponse(response, status=code)
        except TypeDiplomes.DoesNotExist:
            response['success'] = False
            response['message'] = "This diplome doesn't exist"
            code = 404
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
            current_registration.handicap = False if 'non' in request.POST['handicap'] else True
            current_registration.num_certifmedical = request.POST['numcertifmedical']
            current_registration.lieu_certifmedical = request.POST['etabcertifmedical']

            cache.set(f'step_5_{current_registration.num_ordre}', request.POST)

            response['success'] = True
            new_registration = current_registration
            new_registration.save()
            response['code'] = new_registration.num_ordre

            # Remove user cache
            cache.delete_many([f'step_1_{new_registration.num_ordre}',
                               f'step_2_{new_registration.num_ordre}',
                               f'step_3_{new_registration.num_ordre}',
                               f'step_4_{new_registration.num_ordre}',
                               f'step_5_{new_registration.num_ordre}',
                               f'step_6_{new_registration.num_ordre}'
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


def validation_step_autre(request):
    """
        Partially save of data for step 6.
    """
    response = {}
    code = 200
    if request.method == 'POST':
        try:
            current_registration.agence_paiement = request.POST['paiement']
            current_registration.transaction_number = request.POST['numerotransaction']

            cache.set(f'step_6_{current_registration.num_ordre}', request.POST)

            response['success'] = True
            response['code'] = current_registration.num_ordre

            return JsonResponse(response, status=code)
        except Exception as e:
            import traceback
            traceback.print_exc()
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


""" 
    GENERATEUR DE PDF POUR LA FICHE D'INSCRIPTION
    -----------------------------------------------------------------------
"""


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


data = {}


# Opens up page as PDF
class ViewPDF(View):
    def get(self, request, code, *args, **kwargs):
        # pdf qui affiche les informations d'un étudiant
        context = {}
        try:
            dossier_univ = DossierUnivs.objects.get(num_ordre=code)
            context['dossier'] = dossier_univ
        except DossierUnivs.DoesNotExist:
            import traceback
            traceback.print_exc()

        pdf = render_to_pdf('falshfsfse/pdf_template.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


# Automaticaly downloads to PDF file
class DownloadPDF(View):
    def get(self, request, code, *args, **kwargs):

        context = {}
        try:
            dossier_univ = DossierUnivs.objects.get(num_ordre=code)
            context['dossier'] = dossier_univ
        except DossierUnivs.DoesNotExist:
            import traceback
            traceback.print_exc()

        pdf = render_to_pdf('falshfsfse/pdf_template.html', context)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Fiche_preinscription_%s.pdf" % (code)
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response
