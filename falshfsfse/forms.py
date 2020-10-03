import datetime
from django import forms
from django.utils.safestring import mark_safe  # import pour mettre une url dans le help text
from django.utils.translation import ugettext_lazy as _  # import pour la traduction d'un texte

class SearchForm(forms.Form):
    """ forms pour l'affichage de la fiche de l'étudiant """
    # -----------------------------------------------------------------------------------------------------------
    code = forms.CharField(label=_("Votre code de préinscription ou de demande"), max_length=100, required=True)


class CivilForm(forms.Form):
    """ forms pour l'état civil """

    # Les listes des menus déroulants pour l'état civil de l'étudiant
    listesexe = [('féminin', _('Féminin')), ('masculin', _('Masculin'))]
    listestatutmarital = [('Celibataire', _('CELIBATAIRE')), ('marie', _('MARIE(S)')), ('divorce', _('DIVORCE(E)'))]
    listepremierelangue = [('français', _('Français')), ('anglais', _('Anglais'))]
    listestatutprofessionnel = [('SANS EMPLOI', _('SANS EMPLOI')), ('SALARIE(E)', _('SALARIE(E)')),
                                ('EN AUTO-EMPLOI', _('EN AUTO-EMPLOI'))]
    listegrade = [('0', ' '), ('professeur', _('Professeur')), ('maitreconf', _('Maître de Conférence')),
                  ('chargecours', _('Chargé de Cours')), ('autre', _('Autres'))]
    listeechelon = [('0', ' '), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]
    dateprecisenaissance = [('oui', _('Oui')), ('non', _('Non'))]
    # on suppose qu'il faut au moins avoir 15 ans pour s'inscrire à l'université de Uy1
    diffdate = datetime.date.today() - datetime.timedelta(days=4380)  # 15 ans corresponds à environ 5475 jours

    # ------------------------------------------------------------------------------------------------------------
    nom = forms.CharField(label=_("Nom(s)"), max_length=100, required=True)
    prenom = forms.CharField(label=_("Prénom(s)"), max_length=100, required=False)
    datenaissance = forms.DateField(label=_("Date de naissance"), widget=forms.TextInput(
        attrs={'type': 'date', 'min': '1900-01-01', 'max': diffdate}),
                                    required=True)
    dateprecise = forms.ChoiceField(label=_("Est ce la date marquée sur votre acte de naissance?"),
                                    widget=forms.RadioSelect, choices=dateprecisenaissance, required=True)
    lieunaissance = forms.CharField(label=_("Lieu de naissance"), max_length=100, required=True)
    numerocni = forms.CharField(label=_("Numéro de CNI"), max_length=100, required=False)
    sexe = forms.CharField(label=_("Sexe"), widget=forms.Select(choices=listesexe), required=True)
    adresse = forms.CharField(label=_("Adresse"), max_length=100,
                              help_text=_("Votre quartier de résidence. Exemple: Obili"),
                              required=True)
    telephone = forms.CharField(label=_("Téléphone"), max_length=100, required=True,
                                help_text=_("Ne pas mettre les espaces. Exemple: 655565758"))
    email = forms.EmailField(label=_("Votre adresse e-mail"), help_text=_("exemple: accueil@univ-yaounde1.cm"),
                             required=False)
    statutmarital = forms.CharField(label=_("Statut marital"), widget=forms.Select(choices=listestatutmarital),
                                    required=True)
    premierelangue = forms.CharField(label=_("Première langue"), widget=forms.Select(choices=listepremierelangue),
                                     required=True)
    statutprofessionnel = forms.CharField(label=_("Statut professionnel"),
                                          widget=forms.Select(choices=listestatutprofessionnel),
                                          required=False)
    profession = forms.CharField(help_text=_("Votre profession si vous en avez une."),
                                 label=_("Profession"), max_length=100, required=False)
    lieudujob = forms.CharField(label=_("Lieu de votre emploi"), max_length=100, required=False,
                                help_text=_("Si vous avez un emploi."))
    grade = forms.CharField(label=_("Grade"), widget=forms.Select(choices=listegrade), required=False,
                            help_text=_("Uniquement si vous avez un emploi."))
    echelon = forms.CharField(label=_("Echelon"), widget=forms.Select(choices=listeechelon), required=False,
                              help_text=_("Uniquement si vous avez un emploi."))


class FiliationForm(forms.Form):
    """ forms pour la filiation de l'étudiant """

    # Les listes des menus déroulants pour les informations de filiation
    listenationalite = [('1', _('Cameroun')), ('2', _('Congo')), ('3', _('Gabon')),
                        ('4', _('Guinnée-équatoriale')), ('5', _('Nigeria')),
                        ('6', _('République Centraficaine')), ('8', _('Tchad')),('7', _('Autre'))]
    listeregion = [('2', _('ADAMAOUA')), ('1', _('CENTRE')), ('3', _('EST')), ('4', _('EXTREME-NORD')), ('5', _('LITTORAL')),
                   ('8', _('OUEST')),('6', _('NORD')), ('7', _('NORD-OUEST')), ('9', _('SUD')), 
                   ('10', _('SUD-OUEST')), ('11', _('ETRANGER'))]
    listedepartement = [('', '')]

    # -----------------------------------------------------------------------------------------------------------
    nationalite = forms.CharField(label=_("Nationalité"), widget=forms.Select(choices=listenationalite), required=True)
    regionorigine = forms.CharField(label=_("Région d'origine"), widget=forms.Select(choices=listeregion),
                                    required=True)
    departementorigine = forms.CharField(label=_("Département d'origine"),
                                         widget=forms.Select(choices=listedepartement),
                                         required=True)
    nompere = forms.CharField(label=_("Nom du père"), max_length=100,
                              help_text=_("Le nom de votre père"), required=False)
    professionpere = forms.CharField(label=_("Profession du père"), max_length=100, required=False)
    nommere = forms.CharField(label=_("Nom de la mère"), max_length=100,
                              help_text=_("Le nom de votre mère"), required=True)
    professionmere = forms.CharField(label=_("Profession de votre mère"), max_length=100, required=True)
    nomurgence = forms.CharField(label=_("Nom du contact pour urgence"), max_length=100,
                                 help_text=_("Remettre le nom du père ou de la mère si c'est la personne à contacter en cas d'urgence"),
                                 required=True)
    telurgence = forms.CharField(label=_("Téléphone du contact pour urgence"), max_length=15,
                                 help_text=_("Ne pas mettre les espaces. Exemple: 655565758"), required=True)
    villeurgence = forms.CharField(label=_("Ville de résidence du contact pour urgence"), max_length=100, required=True)


class FaculteForm(forms.Form):
    """ forms pour la faculté de l'étudiant """

    # Les listes des menus déroulants pour les informations de filiation
    listefilierefac = [('', '')]
    listefiliere = [('', '')]
    listeniveau = [('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3'), ('M1', 'M1')]
    listestatut = [('camerounais', _('Etudiant camerounais')), ('etranger', _('Etudiant étranger'))]

    # -----------------------------------------------------------------------------------------------------------
    faculte = forms.CharField(label=_("Votre faculté"), required=True, widget=forms.TextInput(attrs={'disabled': 'disabled'}))
    questionnaire = forms.CharField(help_text=mark_safe(
        "Cliquez <a href='https://orientation.omdes.cm/#/orientation' target='_blank'>ici pour faire le questionnaire et obtenir votre code.</a>"),
        label=_("Code du Questionnaire d'orientation"), max_length=10,
        widget=forms.TextInput(attrs={'placeholder': _('Obtenez le code en cliquant sur le lien ci dessous')}),
        required=True)
    niveau = forms.CharField(label=_("Niveau souhaité"), widget=forms.Select(choices=listeniveau), required=True)
    premierchoix = forms.CharField(help_text=mark_safe(" "), label=_("Premier choix de filière"),
                                   widget=forms.Select(choices=listefilierefac), required=True)
    secondchoix = forms.CharField(help_text=mark_safe(" "), label=_("Second choix de filière"),
                                  widget=forms.Select(choices=listefiliere), required=True)
    troisiemechoix = forms.CharField(help_text=mark_safe(" "), label=_("Troisième choix de filière"),
                                     widget=forms.Select(choices=listefiliere), required=True)
    niveau = forms.CharField(label=_("Niveau souhaité"), widget=forms.Select(choices=listeniveau), required=True)
    statutdesire = forms.CharField(label=_("Votre Statut"), widget=forms.Select(choices=listestatut), required=True)


class DiplomeForm(forms.Form):
    """ forms pour les diplomes de l'étudiant """

    # Les listes des menus déroulants pour les informations de filiation
    listediplome = [('1', _('BACC CAMEROUNAIS')), ('2', _('BACC ETRANGER')), ('3', _('GCE A LEVEL')),
                    ('4', _('GCE O LEVEL')), ('5', _('DEUG')), ('6', _('LICENCE')), ('7', _('LICENCE PROFESSIONNELLE')),
                    ('8', _('LICENCE EN SCIENCES BIOMEDICALES')), ('9', _('MASTER 1')), ('10', _('MASTER 2')),
                    ('11', _('DIPES 1')), ('12', _('CSCT')), ('13', _('RELEVE DE NOTES')),
                    ('14', _('DIPLÔME D\'ETAT D\'INFIRMIER')), ('15', _('DOCTORAT')),
                    ('16', _('DOCTORAT EN MEDECINE OU EN PHARMACIE')),('16', _('PROBATOIRE'))]
    listespebacc = [('',''), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('TI', 'TI'), ('E', 'E')]
    listeniveau = [('', ''), ('1', _('Licence 1')), ('2', _('Licence 2')), ('3', _('Licence 3')), ('4', _('Master 1')),
                   ('5', _('Master 2'))]
    listestatut = [('camerounais', 'Etudiant camerounais'), ('etranger', 'Etudiant étranger')]
    listemention = [('1', 'PASSABLE'), ('2', 'ASSEZ BIEN'), ('3', 'BIEN'), ('4', 'TRES BIEN'),
                    ('5', 'EXCELLENT'),('6', 'PASSED')]
    listegrade = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')]
    annee = datetime.date.today().year
    # -----------------------------------------------------------------------------------------------------------
    diplome = forms.CharField(label=_("Nom du diplôme soumis"), widget=forms.Select(choices=listediplome),
                              required=True)
    serie = forms.CharField(label=_("Nom de la série"), widget=forms.Select(choices=listespebacc),
                              required=False)
    anneeobtention = forms.IntegerField(label=_("Année d'obtention"), min_value=1980, max_value=annee, required=True,
                                        help_text=_("Saississez juste l'année. Exple: 2020"))
    moyenne = forms.FloatField(label=_("Moyenne obtenue"), min_value=0, max_value=20, required=True,
                                widget=forms.NumberInput(attrs={'value': 0.0}),
                               help_text=_("Entrez votre moyenne sur 20. Exemple: 12.8"))
    detailjury = forms.CharField(label=_("Observation du jury ou mention"), max_length=100, required=True,
                                 widget=forms.Select(choices=listemention))
    emetteur = forms.CharField(label=_("Emetteur du diplôme"), max_length=100, required=True,
                               help_text=_("Mentionnez l'institution qui a fourni votre diplôme. Exple: OBC, GCE Board"))
    date_emission = forms.DateField(label=_("Date de délivrance du diplôme"), widget=forms.TextInput(
        attrs={'type': 'date', 'min': '1900-01-01', 'max': datetime.date.today()}),
                                    required=True)
    nombresoumis = forms.IntegerField(label=_("Nombre de matières validées"), min_value=0, max_value=10, required=False,
                                    widget=forms.NumberInput(attrs={'value': 0}),
                                    help_text=_("Uniquement pour GCE A/L"))
    papier1 = forms.CharField(label=_("Papier 1"), required=False,
                                      help_text=_("Mettre l\'abreviation de la matière. Example: BIO pour biologie"))
    grade1 = forms.CharField(label=_("Grade 1"), max_length=100, required=False, widget=forms.Select(choices=listegrade))
    papier2 = forms.CharField(label=_("Papier 2"), required=False,
                                      help_text=_("Mettre l\'abreviation de la matière. Example: CH pour chimie"))
    grade2 = forms.CharField(label=_("Grade 2"), max_length=100, required=False, widget=forms.Select(choices=listegrade))
    papier3 = forms.CharField(label=_("Papier 3"), required=False,
                                      help_text=_("Mettre l\'abreviation de la matière. Example: ICT pour informatique"))
    grade3 = forms.CharField(label=_("Grade 3"), max_length=100, required=False, widget=forms.Select(choices=listegrade))
                

class SportForm(forms.Form):
    """ forms pour les activités sportives de l'étudiant """

    #Les listes des menus déroulants pour les informations de filiation
    listesport = [('athlétisme',_('Athlétisme')),('basketball',_('BasketBall')),('boxe',_('Boxe')),('football',_('Football')),
                ('gymnastique',_('Gymnastique')),('handball',_('Handball')),('judo',_('Judo')),('karate',_('Karaté')),
                ('lutte',_('Lutte')),('nambudo',_('Nambudo')),('tennistable',_('Tennis de table')),('volleyball',_('Volley-ball'))]
    listeart = [('artsplastiques',_('Arts plastiques')),('chanson',_('Chanson')),('chorale',_('Chorale')),
                ('dansetrad',_('Danse traditionnelle et moderne')),('dessinpeinture',_('Dessin et peinture')), 
                ('litterature',_('Littérature écrite et orale')),('majorette',_('Majorette')),('musique',_('Musique')),
                ('orchestre',_('Orchestre moderne et traditionnel')),('photographie',_('Photographie')),('theatre',_('Théâtre'))]
    listehandicap = [('oui',_('Oui')),('non',_('Non'))]

    #-----------------------------------------------------------------------------------------------------------  
    sport = forms.MultipleChoiceField(label=_("Sport pratiqué"), widget=forms.CheckboxSelectMultiple, choices=listesport,
                                        required=False)
    autresport = forms.CharField(label=_("Si autre, indiquez le sport"), max_length=300, required=False,
                                 help_text=_("Mettre le sport que vous pratiquez et qui n'est pas cité au dessus"))
    art = forms.MultipleChoiceField(label=_("Art pratiqué"), widget=forms.CheckboxSelectMultiple, choices=listeart,
                                        required=False)
    autreart = forms.CharField(label=_("Si autre, indiquez l'art"), max_length=300, required=False,
                                 help_text=_("Mettre l'art que vous pratiquez et qui n'est pas cité au dessus"))
    handicap = forms.ChoiceField(label=_("Avez vous un handicap?"),
                                    widget=forms.RadioSelect, choices=listehandicap, required=True)
    numcertifmedical = forms.CharField(label=_("Numéro du certificat médical"), max_length=300, required=False,
                                 help_text=_("Vous avez 1 mois pour donner cette information"))
    etabcertifmedical = forms.CharField(label=_("Lieu du certificat médical"), max_length=300, required=False,
                                 help_text=_("Centre de santé ayant délivré le certificat médical"))


class AutreForm(forms.Form):
    """ forms pour les autres informations de l'étudiant """

    # Les listes des menus déroulants pour les informations de filiation
    listepaiement = [('EU', 'Express Union'), ('UBA', 'UBA')]
    choixassurance = [('oui', _('Oui')), ('non', _('Non'))]
    # -----------------------------------------------------------------------------------------------------------

    paiement = forms.CharField(label=_("Lieu de paiement"), widget=forms.Select(choices=listepaiement), required=True)
    numerotransaction = forms.CharField(label=_("Numéro de transaction"), max_length=100, required=True)
    # assurance = forms.CharField(label="Lieu de paiement", widget=forms.Select(choices=listepaiement), required=False)

