from django import forms
from django.utils.safestring import mark_safe  # import pour mettre une url dans le help text
from django.utils.translation import ugettext_lazy as _ #import pour la traduction d'un texte

class Logement_SearchForm(forms.Form):    
    """ forms pour l'affichage de la fiche de logement l'étudiant """
    #-----------------------------------------------------------------------------------------------------------
    code = forms.CharField(label=_("Votre code de logement"), max_length=100, required=True)

class Logement_CivilForm(forms.Form):    
    """ forms pour l'état civil """

    #Les listes des menus déroulants pour l'état civil de l'étudiant
    listesexe = [('féminin','Féminin'),('masculin','Masculin')]
    listestatutmarital = [('CELIBATAIRE', 'CELIBATAIRE'), ('MARIE(S)', 'MARIE(S)'), ('DIVORCE(E)', 'DIVORCE(E)')]
    listepremierelangue = [('français','Français'),('anglais','Anglais')]
    listestatutprofessionnel = [('SANS EMPLOI', 'SANS EMPLOI'), ('SALARIE(E)', 'SALARIE(E)'),
                                ('EN AUTO-EMPLOI', 'EN AUTO-EMPLOI')]
    listegrade = [('',''),('professeur','Professeur'),('maitreconf','Maître de Conférence'),
                                ('chargecours','Chargé de Cours'),('autre','Autres')]
    listeechelon = [('',''),('1','1'),('2','2'),('3','3'),('4','4')]
    choixhandicap = [('oui','Oui'),('non','Non')]
    dateprecisenaissance = [('oui', 'Oui'), ('non', 'Non')]
    #-----------------------------------------------------------------------------------------------------------
    nom = forms.CharField(label=_("Nom"), max_length=100, required=True)
    prenom = forms.CharField(label=_("Prénom"), max_length=100, required=False)
    datenaissance = forms.DateField(label=_("Date de naissance"), widget=forms.TextInput(attrs={'type': 'date', 'min': '1998-01-01', 'max': '2006-12-31'}),required=True)
    dateprecise = forms.ChoiceField(label=_("Est ce la date marquée sur votre acte de naissance?"),
                                    widget=forms.RadioSelect, choices=dateprecisenaissance, required=True)
    lieunaissance = forms.CharField(label=_("Lieu de naissance"), max_length=100, required=True)
    sexe = forms.CharField(label=_("Sexe"), widget=forms.Select(choices=listesexe), required=True)
    residence_parent = forms.CharField(label=_("Résidence actuelle des parents"), max_length=100, required=True)
    handicap = forms.MultipleChoiceField(label=_("Avez vous un handicap?"), widget=forms.RadioSelect, choices=choixhandicap,
                                        required=True)
    telephone = forms.CharField(label=_("Téléphone"), max_length=100, required=True,
                                help_text=_("Ne pas mettre les espaces. Exemple: 655565758"))
    email = forms.EmailField(label=_("Votre adresse e-mail"), help_text=_("exemple: accueil@univ-yaounde1.cm"), required=False)
    residence = forms.CharField(label=_("Votre résidence actuelle"), max_length=100, required=True,
                                help_text=_("Votre lieu de résidence actuelle. Exple: Obili"))
    
class Logement_FiliationForm(forms.Form):    
    """ forms pour la filiation de l'étudiant """

    #Les listes des menus déroulants pour les informations de filiation
    listenationalite = [('1', 'Cameroun'), ('2', 'Congo'), ('3', 'Gabon'),
                        ('4', 'Guinnée-équatoriale'),
                        ('6', 'République Centraficaine'), ('5', 'Nigeria'), ('8', 'Tchad'), ('7', 'Autre'), ]
    listeregion = [('2', 'ADAMAOUA'), ('1', 'CENTRE'), ('3', 'EST'), ('4', 'EXTREME-NORD'), ('5', 'LITTORAL'),
                   ('8', 'OUEST'),
                   ('6', 'NORD'), ('7', 'NORD-OUEST'), ('9', 'SUD'), ('10', 'SUD-OUEST'), ('11', 'ETRANGER')]
    listedepartement = [('', '')]
    #-----------------------------------------------------------------------------------------------------------
    nationalite = forms.CharField(label=_("Nationalité"), widget=forms.Select(choices=listenationalite), required=True)
    regionorigine = forms.CharField(label=_("Région d'origine"), widget=forms.Select(choices=listeregion), required=True)
    departementorigine = forms.CharField(label=_("Département d'origine"), widget=forms.Select(choices=listedepartement), required=True)
    nompere = forms.CharField(label=_("Nom du père"), max_length=100,help_text=_("Le nom de votre père"),required=False)
    professionpere = forms.CharField(label=_("Profession du père"), max_length=100, required=False)
    nommere = forms.CharField(label=_("Nom de la mère"), max_length=100, help_text=_("Le nom de votre mère"),required=True)
    professionmere = forms.CharField(label=_("Profession de votre mère"), max_length=100, required=True)
    telephoneparents = forms.CharField(label=_("Téléphones des parents"), max_length=100, required=False)
    nomurgence = forms.CharField(label=_("Correspondant à Yaoundé"), max_length=100, 
                                help_text=_("Remettre le nom du père ou de la mère si c'est Correspondant à Yaoundé"),
                                required=True)
    telurgence = forms.CharField(label=_("Téléphone du correspondant"), max_length=15, 
                                help_text=_("Ne pas mettre les espaces. Exemple: 655565758"),required=True)
    villeurgence = forms.CharField(label=_("Ville de résidence du contact pour urgence"), max_length=100,required=True)

class Logement_FaculteForm(forms.Form):    
    """ forms pour la faculté de l'étudiant """

    #Les listes des menus déroulants pour les informations de filiation

    listefaculte = [('1','Falculté des Arts, Lettres et Sciences Humaines'),
                    ('2','Faculté des Sciences'),
                    ('3','Faculté des Sciences de l\'Education'),
                    ('4','Faculté de Médecine et des Sciences Biomédicales'),
                    ('5','Ecole Nationale Supérieure Polytechnique de Yaoundé'),
                    ('6','Ecole Normale Supérieure'),
                    ('7','Ecole Normale Supérieure d\'Enseignement Technique d\'Ebolowa'),
                    ('8','Institut Universitaire de Technologies du Bois de Mbalmayo')
    ]
    listefilierefac = [('','')]
    listefiliere = [('','')]
    listeniveau = [('',''),('1','1'),('2','2'),('3','3'),('4','4'),
                    ('5','5'),('6','6'),('7','7'),('8','8')]
    listestatut = [('0',''),('camerounais','Etudiant camerounais'),('etranger','Etudiant étranger')]
    listeniv = [('', ''), ('TERMINALE', 'TERMINALE'), ('1ERE ANNEE LICENCE', '1ERE ANNEE LICENCE'), ('2EME ANNEE LICENCE', '2EME ANNEE LICENCE'), ('3EME ANNEE LICENCE', '3EME ANNEE LICENCE'),
                    ('MASTER 1', 'MASTER 1'),
                    ('MASTER 2', 'MASTER 2'),
                    ('DOCTORAT', 'DOCTORAT'),
                    ('SPECIALISATION', 'SPECIALISATION'),
                    ('INTERNAT', 'INTERNAT'),
    ]
    listemention = [('', ''), ('1', 'PASSABLE'), ('2', 'ASSEZ BIEN'), ('3', 'BIEN'), ('4', 'TRES BIEN'),
                    ('5', 'EXCELLENT')]
    listecite = [('',' '),('Ancienne cité','Ancienne cité'),('Nouvelle cité','Nouvelle cité'),('Cité de l\'ENS','Cié de l\'ENS'),('Minie-cité conventionnée','Minie-cité conventionnée')]
    listerenouv = [('OUI',' ')]
    listechambre = [('',''),('Individuelle','Individuelle'),('Collective','Collective')]
    #-----------------------------------------------------------------------------------------------------------
    faculte = forms.CharField(label=_("Faculté ou école"), widget=forms.Select(choices=listefaculte), required=True)
    filiere = forms.CharField(label=_("Votre filière"), widget=forms.Select(choices=listefilierefac), required=True)
    niveau  = forms.CharField(label=_("Niveau d'études"), widget=forms.Select(choices=listeniveau), required=True)
    mentionbac  = forms.CharField(label=_("Mention au Baccalauréat/GCE"), widget=forms.Select(choices=listemention), required=True)
    niveaurepris  = forms.CharField(label=_("Niveau ou classe reprise"), widget=forms.Select(choices=listeniv), required=False)
    #niveaurepris  = forms.CharField(label=_("Niveau ou classe reprise"), required=False)
    matricule = forms.CharField(label=_("Votre matricule ou code de préinscription"), max_length=100, required=True)
    nomcite  = forms.CharField(label=_("Dénomination de la Cité sollicitée"), widget=forms.Select(choices=listecite), required=False)
    renouvellement = forms.MultipleChoiceField(label=_("Est-ce un renouvellement?"), widget=forms.CheckboxSelectMultiple, choices=listerenouv,required=False)
    batiment = forms.CharField(label=_("N° Bâtiment"), max_length=100, required=False)
    chambre = forms.CharField(label=_("N° Chambre"), max_length=100, required=False)
    typechambre  = forms.CharField(label=_("Type de chambre"), widget=forms.Select(choices=listechambre), required=False)
    anneepre = forms.CharField(label=_("Votre 1ère année de résidence à la Cité-U"),required=True,
                                help_text=_("Mettez l\'année actuelle si vous n\'avez jamais eu de chambres")) 
    anneeder = forms.CharField(label=_("Votre dernière année de résidence à la Cité-U"),required=True,
                                help_text=_("Mettez l\'année actuelle si vous n\'avez jamais eu de chambres"))
 
class Logement_SportForm(forms.Form):    
    """ forms pour les activités sportives de l'étudiant """

    #Les listes des menus déroulants pour les informations de filiation
    listesport = [('athlétisme',_('Athlétisme')),('basketball',_('BasketBall')),('boxe',_('Boxe')),('football',_('Football')),
                ('gymnastique',_('Gymnastique')),('handball',_('Handball')),('judo',_('Judo')),('karate',_('Karaté')),
                ('lutte',_('Lutte')),('nambudo',_('Nambudo')),('tennistable',_('Tennis de table')),('volleyball',_('Volley-ball'))]
    listeart = [('artsplastiques',_('Arts plastiques')),('chanson',_('Chanson')),('chorale',_('Chorale')),
                ('dansetrad',_('Danse traditionnelle et moderne')),('dessinpeinture',_('Dessin et peinture')), 
                ('litterature',_('Littérature écrite et orale')),('majorette',_('Majorette')),('musique',_('Musique')),
                ('orchestre',_('Orchestre moderne et traditionnel')),('photographie',_('Photographie')),('theatre',_('Théâtre'))]

    #-----------------------------------------------------------------------------------------------------------  
    sport = forms.MultipleChoiceField(label=_("Sport pratiqué"), widget=forms.CheckboxSelectMultiple, choices=listesport,
                                        required=False)
    autresport = forms.CharField(label=_("Si autre, indiquez le sport"), max_length=300, required=False,
                                 help_text=_("Mettre le sport que vous pratiquez et qui n'est pas cité au dessus"))
    art = forms.MultipleChoiceField(label=_("Art pratiqué"), widget=forms.CheckboxSelectMultiple, choices=listeart,
                                        required=False)
    autreart = forms.CharField(label=_("Si autre, indiquez l'art"), max_length=300, required=False,
                                 help_text=_("Mettre l'art que vous pratiquez et qui n'est pas cité au dessus"))