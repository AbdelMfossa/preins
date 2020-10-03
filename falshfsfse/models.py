# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
import uuid
import random


class Bilingue(models.Model):
    code_pre = models.CharField(max_length=50, unique=True)
    nom_etudiant = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'bilingue'


# Table not used
class CentreExams(models.Model):
    libelle = models.CharField(max_length=100, blank=True, null=True)
    nbre_candidat = models.IntegerField(blank=True, null=True)
    nbre_candidat_fac = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=2, blank=True, null=True)
    nbre_cand_m1 = models.IntegerField(blank=True, null=True)
    nbre_cand_l2 = models.IntegerField(blank=True, null=True)
    nbre_cand_l3 = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    nbre_cand_specia = models.IntegerField(blank=True, null=True)
    nbre_cand_internat = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'centre_exams'


AGENCES_PAIEMENTS = (
    ('EXPRESS UNION', 'EXPRESS UNION'),
    ('UBA', 'UBA')
)

NIVEAUX = (
    ('L1', 'L1'),
    ('L2', 'L2'),
    ('L3', 'L3'),
    ('M1', 'M1'),
    ('M2', 'M2'),
    ('D1', 'D1'),
    ('D2', 'D2'),
    ('D3', 'D3')
)

STATUTS_MATRIMONIAUX = (
    ('MARIE(E)', 'MARIE(S)'),
    ('CELIBATAIRE', 'CELIBATAIRE'),
    ('DIVORCE(E)', 'DIVORCE(E)')
)

SITUATIONS_PROFESSIONNELLES = (
    ('SANS EMPLOI', 'SANS EMPLOI'),
    ('SALARIE(E)', 'SALARIE(E)'),
    ('EN AUTO-EMPLOI', 'EN AUTO-EMPLOI')
)

REGIMES_ENCADREMENTS = (
    ('DIRECTION', 'DIRECTION'),
    ('CO-DIRECTION', 'CO-DIRECTION'),
    ('CO-TUTELLE', 'CO-TUTELLE')
)
LANGUES = (
    ('FRANCAIS', 'FRANCAIS'),
    ('ANGLAIS', 'ANGLAIS')
)

SEXES = (
    ('MASCULIN', 'MASCULIN'),
    ('FEMININ', 'FEMININ')
)

# Fritz: je commente cette table car elle ne sert plus à rien
""" class DossiersCopy16092019(models.Model):
    inst1_id = models.IntegerField(blank=True, null=True)
    inst2_id = models.IntegerField(blank=True, null=True)
    inst3_id = models.IntegerField(blank=True, null=True)
    fil1_id = models.IntegerField()
    fil2_id = models.IntegerField(blank=True, null=True)
    fil3_id = models.IntegerField(blank=True, null=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_nais = models.DateField()
    lieu_nais = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1)
    langue = models.CharField(max_length=1)
    nato_id = models.IntegerField()
    tel = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    region_origine_id = models.IntegerField()
    region_examen_id = models.IntegerField()
    type_diplome_id = models.IntegerField(blank=True, null=True)
    serie = models.CharField(max_length=1, blank=True, null=True)
    moyenne = models.FloatField(blank=True, null=True)
    annee_obtention = models.IntegerField(blank=True, null=True)
    num_matricule = models.CharField(max_length=20, blank=True, null=True)
    code_centre = models.CharField(max_length=5, blank=True, null=True)
    code_jury = models.CharField(max_length=5, blank=True, null=True)
    mention_id = models.IntegerField(blank=True, null=True)
    grade_bio = models.CharField(max_length=1, blank=True, null=True)
    grade_bio_an = models.IntegerField(blank=True, null=True)
    grade_chim = models.CharField(max_length=1, blank=True, null=True)
    grade_chim_an = models.IntegerField(blank=True, null=True)
    mati_olevel = models.CharField(max_length=1, blank=True, null=True)
    grade_mati_olevel = models.CharField(max_length=1, blank=True, null=True)
    grade_mati_olevel_an = models.IntegerField(blank=True, null=True)
    decl_honneur = models.IntegerField()
    banque = models.CharField(max_length=40, blank=True, null=True)
    num_quittance = models.CharField(max_length=20, blank=True, null=True)
    num_ordre = models.CharField(unique=True, max_length=10, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    stat_matri = models.CharField(max_length=100, blank=True, null=True)
    nom_pere = models.CharField(max_length=100, blank=True, null=True)
    profession_pere = models.CharField(max_length=100, blank=True, null=True)
    nom_mere = models.CharField(max_length=100, blank=True, null=True)
    profession_mere = models.CharField(max_length=100, blank=True, null=True)
    dept_origine_id = models.IntegerField(blank=True, null=True)
    adresse_parent = models.CharField(max_length=100, blank=True, null=True)
    annee_scol1 = models.CharField(max_length=9, blank=True, null=True)
    annee_scol2 = models.CharField(max_length=9, blank=True, null=True)
    annee_scol3 = models.CharField(max_length=9, blank=True, null=True)
    annee_scol4 = models.CharField(max_length=9, blank=True, null=True)
    annee_scol5 = models.CharField(max_length=9, blank=True, null=True)
    annee_scol_etab1 = models.CharField(max_length=100, blank=True, null=True)
    annee_scol_etab2 = models.CharField(max_length=100, blank=True, null=True)
    annee_scol_etab3 = models.CharField(max_length=100, blank=True, null=True)
    annee_scol_etab4 = models.CharField(max_length=100, blank=True, null=True)
    annee_scol_etab5 = models.CharField(max_length=100, blank=True, null=True)
    annee_scol_niv1 = models.CharField(max_length=50, blank=True, null=True)
    annee_scol_niv2 = models.CharField(max_length=50, blank=True, null=True)
    annee_scol_niv3 = models.CharField(max_length=50, blank=True, null=True)
    annee_scol_niv4 = models.CharField(max_length=50, blank=True, null=True)
    annee_scol_niv5 = models.CharField(max_length=50, blank=True, null=True)
    annee_scol_ser1 = models.CharField(max_length=5, blank=True, null=True)
    annee_scol_ser2 = models.CharField(max_length=5, blank=True, null=True)
    annee_scol_ser3 = models.CharField(max_length=5, blank=True, null=True)
    annee_scol_ser4 = models.CharField(max_length=5, blank=True, null=True)
    annee_scol_ser5 = models.CharField(max_length=5, blank=True, null=True)
    annee_scol_dipl1 = models.CharField(max_length=100, blank=True, null=True)
    annee_scol_dipl2 = models.CharField(max_length=100, blank=True, null=True)
    annee_scol_dipl3 = models.CharField(max_length=100, blank=True, null=True)
    annee_scol_dipl4 = models.CharField(max_length=100, blank=True, null=True)
    annee_scol_dipl5 = models.CharField(max_length=100, blank=True, null=True)
    annee_scol_san1 = models.CharField(max_length=50, blank=True, null=True)
    annee_scol_san2 = models.CharField(max_length=50, blank=True, null=True)
    annee_scol_san3 = models.CharField(max_length=50, blank=True, null=True)
    annee_scol_san4 = models.CharField(max_length=50, blank=True, null=True)
    annee_scol_san5 = models.CharField(max_length=50, blank=True, null=True)
    q1 = models.CharField(max_length=100, blank=True, null=True)
    q2 = models.CharField(max_length=100, blank=True, null=True)
    q31 = models.IntegerField(blank=True, null=True)
    q32 = models.CharField(max_length=100, blank=True, null=True)
    q41 = models.IntegerField(blank=True, null=True)
    q42 = models.CharField(max_length=100, blank=True, null=True)
    q52 = models.CharField(max_length=100, blank=True, null=True)
    q61 = models.IntegerField(blank=True, null=True)
    q62 = models.CharField(max_length=100, blank=True, null=True)
    q81 = models.IntegerField(blank=True, null=True)
    q82 = models.CharField(max_length=100, blank=True, null=True)
    q91 = models.CharField(max_length=100, blank=True, null=True)
    q92 = models.CharField(max_length=100, blank=True, null=True)
    q93 = models.CharField(max_length=100, blank=True, null=True)
    q10 = models.CharField(max_length=100, blank=True, null=True)
    q111 = models.CharField(max_length=100, blank=True, null=True)
    q112 = models.CharField(max_length=100, blank=True, null=True)
    q113 = models.CharField(max_length=100, blank=True, null=True)
    q12 = models.CharField(max_length=100, blank=True, null=True)
    q131 = models.IntegerField(blank=True, null=True)
    q132 = models.CharField(max_length=100, blank=True, null=True)
    q14 = models.CharField(max_length=100, blank=True, null=True)
    q51 = models.CharField(max_length=100, blank=True, null=True)
    q9 = models.IntegerField(blank=True, null=True)
    lieu_depot_id = models.IntegerField(blank=True, null=True)
    nom_banque = models.CharField(max_length=100, blank=True, null=True)
    date_paiement = models.DateField(blank=True, null=True)
    deposited = models.IntegerField(blank=True, null=True)
    institution_depot_id = models.IntegerField(blank=True, null=True)
    filiere_depot_id = models.IntegerField(blank=True, null=True)
    user_depot_id = models.IntegerField(blank=True, null=True)
    date_depot = models.DateTimeField(blank=True, null=True)
    dipl_etabl = models.CharField(max_length=100, blank=True, null=True)
    dipl_info_jury = models.CharField(max_length=100, blank=True, null=True)
    dipl_date_deli = models.DateField(blank=True, null=True)
    niv_acad = models.IntegerField(blank=True, null=True)
    examen_id = models.IntegerField(blank=True, null=True)
    accept_prive_etabl_id = models.IntegerField(blank=True, null=True)
    accept_prive = models.IntegerField(blank=True, null=True)
    type_etabl_c = models.CharField(max_length=1, blank=True, null=True)
    code_secret = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'dossiers_copy16092019'

 """


class Examen(models.Model):
    libelle = models.CharField(max_length=200, blank=True, null=True)
    reference = models.CharField(max_length=20, blank=True, null=True)
    annee = models.IntegerField(blank=True, null=True)
    date_lancement = models.DateField(blank=True, null=True)
    date_limite_depot_do = models.DateField(blank=True, null=True)
    age_limite = models.IntegerField(blank=True, null=True)
    date_ref_age_limit = models.DateField(blank=True, null=True)
    compte_bancaire = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'examen'


class Institutions(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)
    type_inst = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    type_fac = models.CharField(max_length=1, blank=True, null=True)
    type_etbl = models.CharField(max_length=1, blank=True, null=True)
    code_fil1 = models.IntegerField(blank=True, null=True)
    code_fil2 = models.IntegerField(blank=True, null=True)
    code_fil3 = models.IntegerField(blank=True, null=True)
    compte_bancaire = models.CharField(max_length=45, blank=True, null=True)
    nred = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'institutions'
        verbose_name_plural = 'Institutions'

    # def __str__(self):
    #     return self.libelle

    def __str__(self):
        return '{}'.format(self.libelle)


class Filieres(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    type_inst = models.CharField(max_length=1, blank=True, null=True)
    type_fac = models.CharField(max_length=1, blank=True, null=True)
    id_institution = models.ForeignKey(Institutions, on_delete=models.DO_NOTHING, related_name='filieres', null=True)
    desc = models.CharField(max_length=400, blank=True, null=True)
    mission = models.CharField(max_length=400, blank=True, null=True)
    diplome_entre = models.CharField(max_length=400, blank=True, null=True)
    debouche = models.CharField(max_length=400, blank=True, null=True)
    condition_entree = models.CharField(max_length=400, blank=True, null=True)
    descprition_url = models.URLField(max_length=100, default='http://supstudy.cm')

    class Meta:
        db_table = 'filieres'
        verbose_name_plural = 'Filieres'

    # def __str__(self):
    #     return self.libelle

    def __str__(self):
        return '{}'.format(self.libelle)


class FxDiplomes(models.Model):
    ref_acte = models.CharField(max_length=255, blank=True, null=True)
    date_acte = models.DateField(blank=True, null=True)
    type_diplome_id = models.IntegerField(blank=True, null=True)
    institution_id = models.IntegerField(blank=True, null=True)
    date_obtention = models.DateField(blank=True, null=True)
    nom_detenteur = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'fx_diplomes'


class GradeAcas(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'grade_acas'


class Informatique(models.Model):
    matricule = models.CharField(max_length=10, blank=True, null=True)
    nom_etudiant = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'informatique'


class Klasses(models.Model):
    libelle = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'klasses'


class Lettres(models.Model):
    let = models.CharField(max_length=1, blank=True, null=True)
    ordre = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'lettres'


class LieuDepots(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    institution_id = models.IntegerField(blank=True, null=True)
    filiere_id = models.IntegerField(blank=True, null=True)
    type_op = models.CharField(max_length=2, blank=True, null=True)
    journee_du = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'lieu_depots'


class MasterOptions(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)
    master_id = models.IntegerField(blank=True, null=True)
    nb_place = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'master_options'


class Masters(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)
    urfd_id = models.IntegerField(blank=True, null=True)
    dept_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'masters'


class Mentions(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mentions'
        verbose_name_plural = 'mentions'

    # def __str__(self):
    #     return self.libelle

    def __str__(self):
        return '{}'.format(self.libelle)


class Nations(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'nations'
        verbose_name_plural = 'Nations'

    # def __str__(self):
    #     return self.libelle

    def __str__(self):
        return '{}'.format(self.libelle)


class Niveaus(models.Model):
    code = models.CharField(max_length=3)
    libelle = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type_op = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'niveaus'
        verbose_name_plural = 'niveaux'

    # def __str__(self):
    #     return self.libelle

    def __str__(self):
        return '{}'.format(self.libelle)


class PaiementMomoFmCopy(models.Model):
    paiement_from = models.CharField(db_column='paiement_From', max_length=255)  # Field name made lowercase.
    paiement_amount = models.CharField(db_column='paiement_Amount', max_length=255)  # Field name made lowercase.
    paiement_currency = models.CharField(db_column='paiement_Currency', max_length=255)  # Field name made lowercase.
    paiement_datetime = models.CharField(db_column='paiement_DateTime', max_length=255)  # Field name made lowercase.
    paiement_operator = models.CharField(db_column='paiement_Operator', max_length=255)  # Field name made lowercase.
    paiement_credittype = models.CharField(db_column='paiement_CreditType',
                                           max_length=255)  # Field name made lowercase.
    paiement_payment_id = models.CharField(db_column='paiement_Payment_ID', primary_key=True,
                                           max_length=255)  # Field name made lowercase.
    paiement_setlement = models.CharField(db_column='paiement_Setlement', max_length=255)  # Field name made lowercase.
    paiement_category = models.CharField(db_column='paiement_Category', max_length=255)  # Field name made lowercase.
    paiement_item_designation = models.CharField(db_column='paiement_Item_Designation',
                                                 max_length=255)  # Field name made lowercase.
    paiement_item_description = models.CharField(db_column='paiement_Item_Description',
                                                 max_length=255)  # Field name made lowercase.
    paiement_item_setled = models.CharField(db_column='paiement_Item_Setled',
                                            max_length=255)  # Field name made lowercase.
    paiement_payment_id_mtn = models.CharField(db_column='paiement_Payment_ID_MTN', max_length=255, blank=True,
                                               null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'paiement_momo_fm_copy'


class Papers(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'papers'


class Rdvs(models.Model):
    lieu_depot_id = models.IntegerField(blank=True, null=True)
    date_rdv = models.DateField(blank=True, null=True)
    nbre_cand = models.IntegerField(blank=True, null=True)
    closed = models.IntegerField(blank=True, null=True)
    closed_at = models.DateTimeField(blank=True, null=True)
    closed_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'rdvs'


class Regions(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nbre_candidat = models.IntegerField(default=0)
    code = models.CharField(max_length=2, blank=True, null=True)
    nbre_candidat_fac = models.IntegerField(default=0)
    nbre_cand_m1 = models.IntegerField(default=0)
    nbre_cand_l2 = models.IntegerField(default=0)
    nbre_cand_l3 = models.IntegerField(default=0)

    class Meta:
        db_table = 'regions'
        verbose_name_plural = 'regions'

    # def __str__(self):
    #     return self.libelle

    def __str__(self):
        return '{}'.format(self.libelle)


class Departements(models.Model):
    nom = models.CharField(max_length=255)
    chef_lieu = models.CharField(max_length=255)
    region_id = models.ForeignKey(Regions, on_delete=models.DO_NOTHING, related_name='departements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'departements'
        verbose_name_plural = 'departements'

    # def __str__(self):
    #     return self.nom

    def __str__(self):
        return '{}'.format(self.nom)


class Arrondissements(models.Model):
    nom = models.CharField(max_length=255)
    chef_lieu = models.CharField(max_length=255, blank=True, null=True)
    departement_id = models.ForeignKey(Departements, on_delete=models.DO_NOTHING, related_name='arrondissements',
                                       db_column='departement_id')
    region_id = models.ForeignKey(Regions, on_delete=models.DO_NOTHING, related_name='arrondissements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'arrondissements'
        verbose_name_plural = 'arrondissements'

    # def __str__(self):
    #     return self.nom

    def __str__(self):
        return '{}'.format(self.nom)


class ResultatAptitude(models.Model):
    # id = models.CharField(max_length=30, blank=True, null=True)
    num_ordre = models.CharField(max_length=50, blank=True, null=True)
    nom = models.CharField(max_length=300, blank=True, null=True)
    date_nais = models.CharField(max_length=50, blank=True, null=True)
    lieu_nais = models.CharField(max_length=100, blank=True, null=True)
    mationalite = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    departement = models.CharField(max_length=100, blank=True, null=True)
    centre_examen = models.CharField(max_length=200, blank=True, null=True)
    etablissement = models.CharField(max_length=200, blank=True, null=True)
    filiere = models.CharField(max_length=200, blank=True, null=True)
    cod_region = models.CharField(max_length=20, blank=True, null=True)
    genre = models.CharField(max_length=20, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    annee = models.CharField(max_length=20, blank=True, null=True)
    note_bacc = models.CharField(max_length=20, blank=True, null=True)
    nbre_annee_sec = models.CharField(max_length=20, blank=True, null=True)
    note_age = models.CharField(max_length=20, blank=True, null=True)
    note_mention = models.CharField(max_length=20, blank=True, null=True)
    note_cycle_sec = models.CharField(max_length=20, blank=True, null=True)
    note_sur_20 = models.CharField(max_length=20, blank=True, null=True)
    observations = models.CharField(max_length=20, blank=True, null=True)
    biology = models.CharField(max_length=20, blank=True, null=True)
    chemestry = models.CharField(max_length=20, blank=True, null=True)
    physics = models.CharField(max_length=20, blank=True, null=True)
    maths = models.CharField(max_length=20, blank=True, null=True)
    other = models.CharField(max_length=20, blank=True, null=True)
    notes = models.CharField(max_length=20, blank=True, null=True)
    notes_bcp = models.CharField(max_length=20, blank=True, null=True)
    notes_cg = models.CharField(max_length=20, blank=True, null=True)
    notes_bcp_sur_80 = models.CharField(max_length=20, blank=True, null=True)
    notes_cg_sur_20 = models.CharField(max_length=20, blank=True, null=True)
    total_sur_120 = models.CharField(max_length=20, blank=True, null=True)
    total_sur_20 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'resultat_aptitude'


class ResultatSynthese(models.Model):
    # id = models.CharField(max_length=50, blank=True, null=True)
    num_ordre = models.CharField(max_length=50, blank=True, null=True)
    nom = models.CharField(max_length=200, blank=True, null=True)
    date_nais = models.CharField(max_length=50, blank=True, null=True)
    lieu_nais = models.CharField(max_length=50, blank=True, null=True)
    filiere = models.CharField(max_length=200, blank=True, null=True)
    etablissement = models.CharField(max_length=200, blank=True, null=True)
    notes_epreuve1 = models.CharField(max_length=200, blank=True, null=True)
    notes_epreuve2 = models.CharField(max_length=200, blank=True, null=True)
    notes_cas_courts = models.CharField(max_length=200, blank=True, null=True)
    notes_cas_longs = models.CharField(max_length=200, blank=True, null=True)
    notes_epreuve1_sur_50 = models.CharField(max_length=200, blank=True, null=True)
    notes_epreuve2_sur_50 = models.CharField(max_length=200, blank=True, null=True)
    notes_cas_cours_sur_30 = models.CharField(max_length=200, blank=True, null=True)
    notes_cas_longs_sur_70 = models.CharField(max_length=200, blank=True, null=True)
    total_sur_200 = models.CharField(max_length=200, blank=True, null=True)
    total_sur_20 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'resultat_synthese'


class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=255)

    class Meta:
        db_table = 'schema_migrations'


class Specialites(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'specialites'
        verbose_name_plural = 'specialités'

    # def __str__(self):
    #     return self.libelle

    def __str__(self):
        return '{}'.format(self.libelle)


class TypeDiplomes(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)
    total_note = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    niv_inscription_id = models.IntegerField(blank=True, null=True)
    type_op = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'type_diplomes'
        verbose_name_plural = 'type_diplomes'

    # def __str__(self):
    #     return self.libelle

    def __str__(self):
        return '{}'.format(self.libelle)


class TypeExams(models.Model):
    code = models.CharField(max_length=8, blank=True, null=True)
    libelle = models.CharField(max_length=100, blank=True, null=True)
    sessione_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'type_exams'

    # def __str__(self):
    #     return self.libelle

    def __str__(self):
        return '{}'.format(self.libelle)


class Users(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    password_digest = models.CharField(max_length=255, blank=True, null=True)
    remember_token = models.CharField(max_length=255, blank=True, null=True)
    lieu_depot_id = models.IntegerField(blank=True, null=True)
    admin = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255)
    encrypted_password = models.CharField(max_length=255)
    reset_password_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    sign_in_count = models.IntegerField()
    current_sign_in_at = models.DateTimeField(blank=True, null=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    current_sign_in_ip = models.CharField(max_length=255, blank=True, null=True)
    last_sign_in_ip = models.CharField(max_length=255, blank=True, null=True)
    etabl_id = models.IntegerField(blank=True, null=True)
    nom = models.CharField(max_length=255, blank=True, null=True)
    prenom = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    dauq = models.IntegerField(blank=True, null=True)
    b_validation_dauq = models.IntegerField(blank=True, null=True)
    langue = models.CharField(max_length=2, blank=True, null=True)
    code_val = models.CharField(max_length=10, blank=True, null=True)
    centre_id = models.IntegerField(blank=True, null=True)
    s_note_rp_stage = models.IntegerField(blank=True, null=True)
    s_note_anno = models.IntegerField(blank=True, null=True)
    s_note_cahier = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=10, blank=True, null=True)
    roles_mask = models.IntegerField(blank=True, null=True)
    s_fr_ano = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'users'

    # def __str__(self):
    #     return self.name

    def __str__(self):
        return '{}'.format(self.name)


# class DemandeChambres(models.Model): 
#     nom = models.CharField(max_length=50, blank=True, null=True)
#     prenom = models.CharField(max_length=50, blank=True, null=True)
#     date_nais = models.DateField(blank=True, null=True)
#     lieu_nais = models.CharField(max_length=50, blank=True, null=True)
#     sexe = models.CharField(max_length=20, choices=SEXES)
#     dateprecise = models.BooleanField(default=True)
#     #nato_id = models.ForeignKey(Nations, on_delete=models.DO_NOTHING)
#     nationality = models.CharField(max_length=20, blank=True, null=True)
#     # region_origine_id = models.ForeignKey(Regions, on_delete=models.DO_NOTHING)
#     region_origine = models.CharField(max_length=20, blank=True, null=True)
#     # dept_origine_id = models.ForeignKey(Departements, on_delete=models.DO_NOTHING)
#     dept_origine = models.CharField(max_length=20, blank=True, null=True)
#     tel = models.CharField(max_length=20, blank=True, null=True)
#     email = models.CharField(max_length=50, blank=True, null=True)
#     sit_prof = models.CharField(max_length=100, blank=True, null=True)
#     stat_matri = models.CharField(max_length=100, blank=True, null=True)
#     nbre_enfant = models.IntegerField(null=True)
#     # institution = models.ForeignKey(Institutions, on_delete=models.DO_NOTHING)
#     institution = models.CharField(max_length=100, blank=True, null=True)
#     ancien_de_uy1 = models.IntegerField(null=True)
#     nmat = models.CharField(max_length=10, blank=True, null=True)
#     niveau = models.IntegerField()
#     # filiere = models.ForeignKey(Filieres, on_delete=models.DO_NOTHING)
#     filiere = models.CharField(max_length=100, blank=True, null=True)
#     niveau_redouble = models.CharField(max_length=25, null=True)
#     ancien_residant = models.BooleanField(default=False)
#     annee_residence = models.IntegerField()
#     bat_no = models.CharField(max_length=13, null=True)
#     chambre_no = models.CharField(max_length=14, null=True)
#     chambre_type = models.CharField(max_length=20, null=True)
#     premiere_annee_resi = models.IntegerField(null=True)
#     derniere_annee_resi = models.IntegerField(null=True)
#     handicap = models.BooleanField(default=False)
#     orphan = models.BooleanField(default=False)
#     orphan_status = models.CharField(max_length=1, blank=True, null=True)
#     pratique_sport = models.BooleanField(default=False)
#     athlete = models.BooleanField(default=False)
#     judo = models.BooleanField(default=False)
#     tennis_lawn = models.BooleanField(default=False)
#     tennis_table = models.BooleanField(default=False)
#     foot_ball = models.BooleanField(default=False)
#     basket_ball = models.BooleanField(default=False)
#     hand_ball = models.BooleanField(default=False)
#     volley_ball = models.BooleanField(default=False)
#     autre_sport = models.CharField(max_length=100, blank=True, null=True)
#     medaille = models.BooleanField(default=False)
#     or_field = models.BooleanField(db_column='or',
#                                    default=False)  # Field renamed because it was a Python reserved word.
#     argent = models.BooleanField(default=False)
#     bronze = models.BooleanField(default=False)
#     pratique_art = models.BooleanField(default=False)
#     theatre = models.BooleanField(default=False)
#     ballet_moderne = models.BooleanField(default=False)
#     ballet_tradi = models.BooleanField(default=False)
#     chorale = models.BooleanField(default=False)
#     art_plast_dessin = models.BooleanField(default=False)
#     art_plast_peintre = models.BooleanField(default=False)
#     majorette = models.BooleanField(default=False)
#     musique = models.BooleanField(default=False)
#     nom_pere = models.CharField(max_length=100, blank=True, null=True)
#     nom_mere = models.CharField(max_length=100, blank=True, null=True)
#     profession_pere = models.CharField(max_length=100, blank=True, null=True)
#     profession_mere = models.CharField(max_length=100, blank=True, null=True)
#     adresse_parent = models.CharField(max_length=100, blank=True, null=True)
#     telephone_parent = models.CharField(max_length=50, blank=True, null=True)
#     residence_actuelle = models.CharField(max_length=100, blank=True, null=True)
#     nom_urgence = models.CharField(max_length=100, blank=True, null=True)
#     tel_urgence = models.CharField(max_length=30, blank=True, null=True)
#     decl_honneur = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     email_urgence = models.EmailField(max_length=50, blank=True, null=True)
#     adresse_urgence = models.CharField(max_length=50, blank=True, null=True)
#     num_ordre = models.CharField(max_length=10, blank=True, null=True, unique=True)
#     lieu_depot_id = models.ForeignKey(LieuDepots, on_delete=models.DO_NOTHING)
#     deposited = models.BooleanField(default=False)
#     user_depot_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
#     date_depot = models.DateTimeField()
#     # mention = models.ForeignKey(Mentions, on_delete=models.DO_NOTHING)
#     mention = models.CharField(max_length=100, blank=True, null=True)
#     cite = models.CharField(max_length=100, null=True)
#     doublon = models.IntegerField(blank=True, null=True)
#     list_sports = models.CharField(max_length=200,null=True, blank=True)
#     list_arts = models.CharField(max_length=200,null=True, blank=True)

#     class Meta:
#         db_table = 'demande_chambres'

class DemandeChambres(models.Model): 
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    date_nais = models.DateField(blank=True, null=True)
    lieu_nais = models.CharField(max_length=50, blank=True, null=True)
    sexe = models.CharField(max_length=20, choices=SEXES)
    dateprecise = models.BooleanField(default=True)
    nationality = models.ForeignKey(Nations, on_delete=models.DO_NOTHING, blank=True, null=True,related_name='nationalites')
    # nationality = models.CharField(max_length=20, blank=True, null=True)
    region_origine = models.ForeignKey(Regions, on_delete=models.DO_NOTHING, blank=True, null=True,related_name='reg_origine')
    # region_origine = models.CharField(max_length=20, blank=True, null=True)
    dept_origine = models.ForeignKey(Departements, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='dep_origine')
    # dept_origine = models.CharField(max_length=20, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    sit_prof = models.CharField(max_length=100, blank=True, null=True)
    stat_matri = models.CharField(max_length=100, blank=True, null=True)
    nbre_enfant = models.IntegerField(null=True)
    institution = models.ForeignKey(Institutions, on_delete=models.DO_NOTHING, related_name='chambre_institutions')
    # institution = models.CharField(max_length=100, blank=True, null=True)
    ancien_de_uy1 = models.IntegerField(null=True)
    nmat = models.CharField(max_length=10, blank=True, null=True)
    #niveau = models.IntegerField()
    niveau = models.CharField(max_length=1)
    filiere = models.ForeignKey(Filieres, on_delete=models.DO_NOTHING, related_name='chambre_filiere', blank=True, null=True)
    # filiere = models.CharField(max_length=100, blank=True, null=True)
    niveau_redouble = models.CharField(max_length=25, null=True)
    ancien_residant = models.BooleanField(default=False)
    annee_residence = models.IntegerField(null=True)
    bat_no = models.CharField(max_length=13, null=True)
    chambre_no = models.CharField(max_length=14, null=True)
    chambre_type = models.CharField(max_length=20, null=True)
    premiere_annee_resi = models.CharField(max_length=4,null=True)
    derniere_annee_resi = models.CharField(max_length=4,null=True)
    handicap = models.BooleanField(default=False)
    orphan = models.BooleanField(default=False)
    orphan_status = models.CharField(max_length=1, blank=True, null=True)
    pratique_sport = models.BooleanField(default=False)
    athlete = models.BooleanField(default=False)
    judo = models.BooleanField(default=False)
    tennis_lawn = models.BooleanField(default=False)
    tennis_table = models.BooleanField(default=False)
    foot_ball = models.BooleanField(default=False)
    basket_ball = models.BooleanField(default=False)
    hand_ball = models.BooleanField(default=False)
    volley_ball = models.BooleanField(default=False)
    autre_sport = models.CharField(max_length=100, blank=True, null=True)
    medaille = models.BooleanField(default=False)
    or_field = models.BooleanField(db_column='or',
                                   default=False)  # Field renamed because it was a Python reserved word.
    argent = models.BooleanField(default=False)
    bronze = models.BooleanField(default=False)
    pratique_art = models.BooleanField(default=False)
    theatre = models.BooleanField(default=False)
    ballet_moderne = models.BooleanField(default=False)
    ballet_tradi = models.BooleanField(default=False)
    chorale = models.BooleanField(default=False)
    art_plast_dessin = models.BooleanField(default=False)
    art_plast_peintre = models.BooleanField(default=False)
    majorette = models.BooleanField(default=False)
    musique = models.BooleanField(default=False)
    nom_pere = models.CharField(max_length=100, blank=True, null=True)
    nom_mere = models.CharField(max_length=100, blank=True, null=True)
    profession_pere = models.CharField(max_length=100, blank=True, null=True)
    profession_mere = models.CharField(max_length=100, blank=True, null=True)
    adresse_parent = models.CharField(max_length=100, blank=True, null=True)
    telephone_parent = models.CharField(max_length=50, blank=True, null=True)
    residence_actuelle = models.CharField(max_length=100, blank=True, null=True)
    nom_urgence = models.CharField(max_length=100, blank=True, null=True)
    tel_urgence = models.CharField(max_length=30, blank=True, null=True)
    decl_honneur = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    email_urgence = models.EmailField(max_length=50, blank=True, null=True)
    adresse_urgence = models.CharField(max_length=50, blank=True, null=True)
    num_ordre = models.CharField(max_length=15, blank=True, null=True, unique=True)
    #lieu_depot_id = models.ForeignKey(LieuDepots, on_delete=models.DO_NOTHING)
    deposited = models.BooleanField(default=False)
    #user_depot_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    #date_depot = models.DateTimeField()
    mention = models.ForeignKey(Mentions, on_delete=models.DO_NOTHING, blank=True, null=True)
    #mention = models.CharField(max_length=100, blank=True, null=True)
    cite = models.CharField(max_length=100, null=True)
    doublon = models.IntegerField(blank=True, null=True)
    list_sports = models.CharField(max_length=200,null=True, blank=True)
    list_arts = models.CharField(max_length=200,null=True, blank=True)

    class Meta:
        db_table = 'demande_chambres'

    # def __str__(self):
    #     return f'Dossier logement de {self.nom}'

    def __str__(self):
        return 'Dossier logement de {}'.format(self.nom)


class DossierUnivs(models.Model):
    institution = models.ForeignKey(Institutions, on_delete=models.DO_NOTHING, related_name='institutions', blank=True, null=True)
    fil1 = models.ForeignKey(Filieres, on_delete=models.DO_NOTHING, related_name='premier_choix', blank=True, null=True)
    fil2 = models.ForeignKey(Filieres, on_delete=models.DO_NOTHING, related_name='second_choix', blank=True, null=True)
    fil3 = models.ForeignKey(Filieres, on_delete=models.DO_NOTHING, related_name='troisieme_choix', blank=True, null=True)
    code_orientation = models.CharField(max_length=20, blank=True, null=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    date_nais = models.DateField()
    dateprecise = models.BooleanField(default=True)
    lieu_nais = models.CharField(max_length=50, blank=True, null=True)
    num_cni = models.CharField(max_length=100, blank=True, null=True)
    sexe = models.CharField(max_length=20, choices=SEXES)
    stat_matri = models.CharField(max_length=100, choices=STATUTS_MATRIMONIAUX)
    sit_prof = models.CharField(max_length=100,
                                choices=SITUATIONS_PROFESSIONNELLES)  # Diplay profession en fonction de ce champs
    nationality = models.ForeignKey(Nations, on_delete=models.DO_NOTHING)
    langue = models.CharField(max_length=20, choices=LANGUES)
    tel = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    region_origine = models.ForeignKey(Regions, on_delete=models.DO_NOTHING)
    dept_origine = models.ForeignKey(Departements, on_delete=models.DO_NOTHING)
    # arr_origine = models.ForeignKey(Arrondissements, on_delete=models.DO_NOTHING)
    nom_pere = models.CharField(max_length=100, blank=True, null=True)
    profession_pere = models.CharField(max_length=100, blank=True, null=True)
    nom_mere = models.CharField(max_length=100)
    profession_mere = models.CharField(max_length=100)
    nom_urgence = models.CharField(max_length=100)
    tel_urgence = models.CharField(max_length=20)
    ville_urgence = models.CharField(max_length=100)
    type_diplome = models.ForeignKey(TypeDiplomes, on_delete=models.DO_NOTHING, blank=True, null=True)
    serie = models.CharField(max_length=3, blank=True, null=True)
    moyenne = models.FloatField(default=10.0)
    annee_obtention = models.IntegerField(default=0)
    num_matricule = models.CharField(max_length=20)
    code_centre = models.CharField(max_length=7)
    code_jury = models.CharField(max_length=5)
    mention = models.ForeignKey(Mentions, on_delete=models.DO_NOTHING, blank=True, null=True)
    nbre_paper = models.IntegerField(default=0)
    paper1 = models.ForeignKey(Papers, on_delete=models.DO_NOTHING, related_name='papers_1', blank=True, null=True)
    paper_1 = models.CharField(max_length=10, null=True)
    paper1_grade = models.CharField(max_length=1, null=True)
    paper1_an = models.IntegerField(default=0)
    paper2 = models.ForeignKey(Papers, on_delete=models.DO_NOTHING, related_name='papers_2', blank=True, null=True)
    paper_2 = models.CharField(max_length=10, null=True)
    paper2_grade = models.CharField(max_length=1)
    paper2_an = models.IntegerField(default=0)
    paper3 = models.ForeignKey(Papers, on_delete=models.DO_NOTHING, related_name='papers_3', blank=True, null=True)
    paper_3 = models.CharField(max_length=10, null=True)
    paper3_grade = models.CharField(max_length=1, null=True)
    paper3_an = models.IntegerField(default=0)
    paper4 = models.ForeignKey(Papers, on_delete=models.DO_NOTHING, related_name='papers_4', blank=True, null=True)
    paper4_grade = models.CharField(max_length=1, null=True)
    paper4_an = models.IntegerField(default=0)
    paper5 = models.ForeignKey(Papers, on_delete=models.DO_NOTHING, related_name='papers_5', blank=True, null=True)
    paper5_grade = models.CharField(max_length=1, null=True)
    paper5_an = models.IntegerField(default=0)
    pratique_sport = models.BooleanField(default=False)
    pratique_art = models.BooleanField(default=False)
    desire_assurance = models.BooleanField(default=False)
    desire_logement = models.BooleanField(default=False)
    decl_honneur = models.IntegerField(default=0)
    # num_ordre = models.IntegerField(default=123456789)
    num_ordre = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    lang_olevel = models.CharField(max_length=1, null=True)
    grade_lang_olevel = models.CharField(max_length=1, null=True)
    grade_lang_olevel_an = models.IntegerField(default=0)
    num_bordereau = models.CharField(max_length=40, null=True)
    agence_paiement = models.CharField(max_length=100, choices=AGENCES_PAIEMENTS)
    date_paiement = models.DateField(null=True, blank=True)
    transaction_number = models.CharField(max_length=100, default="000000000")
    list_sports = models.CharField(max_length=200, blank=True, null=True)
    list_arts = models.CharField(max_length=200, blank=True, null=True)
    num_certifmedical = models.CharField(max_length=200, blank=True, null=True)
    lieu_certifmedical = models.CharField(max_length=200, blank=True, null=True)
    vaccine = models.BooleanField(default=False)
    vaccin_fiev_jaun = models.BooleanField(default=False)
    vaccin_tub = models.BooleanField(default=False)
    vaccin_chol = models.BooleanField(default=False)
    vaccin_hepatite = models.BooleanField(default=False)
    vaccin_autre = models.BooleanField(default=False)
    vaccin_autre_desc = models.CharField(max_length=100, blank=True, null=True)
    handicap = models.BooleanField(default=True)
    handicap_mental = models.BooleanField(default=False)
    handicap_physique = models.BooleanField(default=False)
    handicap_physique_desc = models.CharField(max_length=100, blank=True, null=True)
    malchro = models.BooleanField(default=False)  # Maladie chronique
    malhere_asthme = models.BooleanField(default=False)
    malhere_drepa = models.BooleanField(default=False)
    malchro_epileptique = models.BooleanField(default=False)
    malchro_autre = models.BooleanField(default=False)
    malchro_autre_desc = models.CharField(max_length=100, blank=True, null=True)
    malhere = models.IntegerField(default=0)  # Maladie Hereditaire
    malchro_hta = models.BooleanField(default=True)
    malchro_diabete = models.BooleanField(default=False)
    malchro_goutte = models.BooleanField(default=False)
    malhere_epileptique = models.BooleanField(default=False)
    malhere_autre = models.BooleanField(default=False)
    malhere_autre_desc = models.CharField(max_length=100, blank=True, null=True)
    vaccin_tetanos = models.BooleanField(default=False)
    vaccin_meningite = models.BooleanField(default=False)
    nature_candidat = models.CharField(max_length=100, null=True)  # (E) Etranger ou (C) Camerounais
    nature_paiement = models.CharField(max_length=1, blank=True, null=True)
    nature_paiement_mnt = models.FloatField(blank=True, null=True)
    nature_paiement_paid = models.FloatField(blank=True, null=True)
    deposited = models.BooleanField(default=False)
    institution_depot = models.ForeignKey(Institutions, on_delete=models.DO_NOTHING,
                                          related_name='institutions_depot', null=True, blank=True)
    code_questionnaire = models.CharField(max_length=100, null=True)
    filiere_depot = models.ForeignKey(Filieres, on_delete=models.DO_NOTHING, blank=True, null=True)
    user_depot = models.ForeignKey(Users, on_delete=models.DO_NOTHING, blank=True, null=True)
    date_depot = models.DateTimeField(blank=True, null=True)
    lieu_depot = models.ForeignKey(LieuDepots, on_delete=models.DO_NOTHING, related_name='lieux_depot', blank=True,
                                   null=True)
    poste_rdv = models.ForeignKey(LieuDepots, on_delete=models.DO_NOTHING, related_name='postes_depot', blank=True,
                                  null=True)
    date_rdv = models.DateField(blank=True, null=True)  # Date de rendez vous
    date_position_rdv = models.DateTimeField(blank=True, null=True)  # Date de creation du rendez vous (champs date_rdv)
    dipl_etabl = models.CharField(max_length=100, blank=True, null=True)  # Organisme de delivrance du diplome(OBC, FS, ...)
    dipl_info_jury = models.CharField(max_length=300, null=True)  # Voir sur le relevé, devoir renseigner un exemple
    dipl_date_deli = models.DateField(blank=True, null=True)
    niv_acad = models.CharField(max_length=5, choices=NIVEAUX, blank=True, null=True)
    matricule = models.CharField(max_length=10, blank=True, null=True)  # Matricule de l'ancien etablissement ou du BACC
    nbre_enfant = models.IntegerField(default=0)
    niv_redoublee = models.ForeignKey(Niveaus, on_delete=models.DO_NOTHING, blank=True, null=True)

    # ---------- INFORMATIONS ETUDIANTS CITE -------------------
    ancien_dela_cite_u = models.BooleanField(blank=True, null=True)
    annee_citeu = models.IntegerField(default=0)  # Nombre d'années passées à la Cité
    ancien_uv = models.IntegerField(default=0)
    nmat = models.CharField(unique=True, max_length=7, blank=True, null=True)  # Matricule Etudiant
    date_nmat = models.DateTimeField(blank=True,
                                     null=True)  # Date de generation de matricule en cas de nouveau etudiant
    profession = models.CharField(max_length=100, blank=True, null=True)
    lieu_affectation = models.CharField(max_length=100, blank=True, null=True)  # En cas d'etudiant travailleur
    grade = models.CharField(max_length=255, null=True)  # Grade au travail
    ech = models.CharField(max_length=2, blank=True, null=True)
    adresse_perso = models.CharField(max_length=100)
    duree_licence = models.IntegerField(default=3)  # Nombre d'années passées en licence
    duree_master1 = models.IntegerField(default=1)  # Nombre d'années en M1

    # ----------- INFORMATIONS ETUDIANT POUR THESE ET MASTER --------------
    matricule_doc_uy1 = models.CharField(max_length=10, blank=True, null=True) #pour le matricule de candidats internes à Uy1
    matricule_doc_ext = models.CharField(max_length=10, blank=True, null=True) #pour le matricule de candidats externes à Uy1
    ecoledoc = models.CharField(max_length=100, blank=True, null=True)
    uniterecherche = models.CharField(max_length=100, blank=True, null=True)
    disponibilite = models.CharField(max_length=100, blank=True, null=True)
    formationinitiale = models.CharField(max_length=100, blank=True, null=True)
    naturelicence = models.CharField(max_length=100, blank=True, null=True)
    optionlicence = models.CharField(max_length=100, blank=True, null=True)
    anneelicence = models.CharField(max_length=100, blank=True, null=True)
    naturemasterun = models.CharField(max_length=100, blank=True, null=True)
    specialitemasterun = models.CharField(max_length=100, blank=True, null=True)
    etablissementmasterun = models.CharField(max_length=100, blank=True, null=True)
    departementmasterun = models.CharField(max_length=100, blank=True, null=True)
    anneemasterun = models.CharField(max_length=100, blank=True, null=True)
    sourcefinancement = models.CharField(max_length=100, blank=True, null=True)
    motivationthese = models.TextField(blank=True, null=True)
    resumethese = models.TextField(blank=True, null=True) 
    cycle = models.CharField(max_length=100, blank=True, null=True)
    encadreur1 = models.CharField(max_length=100, blank=True, null=True)
    encadreur2 = models.CharField(max_length=100, blank=True, null=True)

    reg_encadrement = models.CharField(max_length=100, blank=True, null=True, choices=REGIMES_ENCADREMENTS)
    these_sujet = models.CharField(max_length=255, blank=True, null=True)
    these_dt_nom = models.CharField(max_length=100, null=True)  # Nom du directeur de thèse
    these_dt_grade = models.ForeignKey(GradeAcas, on_delete=models.DO_NOTHING, blank=True, null=True)
    ante_sujet = models.CharField(max_length=254, blank=True,
                                  null=True)  # Sujet anterieur
    ante_dt_nom = models.CharField(max_length=255, blank=True, null=True)  # Directeur anterieur
    ante_dt_grade = models.IntegerField(default=0)  # Grade du directeur anterieur
    ante_dt_eta = models.CharField(max_length=100, blank=True, null=True)  # Etablissement anterieur
    ante_arti1 = models.CharField(max_length=100, blank=True, null=True)
    ante_arti2 = models.CharField(max_length=100, blank=True, null=True)
    ante_arti3 = models.CharField(max_length=100, blank=True, null=True)
    ante_arti4 = models.CharField(max_length=100, blank=True, null=True)
    ante_arti1_j = models.CharField(max_length=100, blank=True, null=True)  # Journal de publication
    ante_arti2_j = models.CharField(max_length=100, blank=True, null=True)
    ante_arti3_j = models.CharField(max_length=100, blank=True, null=True)
    ante_arti4_j = models.CharField(max_length=100, blank=True, null=True)
    avis_dt = models.IntegerField(default=0)  # Avis du directeur de thèse concernant le sujet anterieur
    date_avis_dt = models.DateField(blank=True, null=True)  # Not used
    avis_ce = models.IntegerField(default=0)  # Not used
    date_avis_ce = models.DateField(blank=True, null=True)  # Not used
    avis_cc = models.IntegerField(default=0)  # Not used
    date_avis_cc = models.DateField(blank=True, null=True)  # Not used
    specialite_these = models.CharField(max_length=255, blank=True, null=True)
    labo_these = models.CharField(max_length=255, blank=True, null=True)
    nature_m1 = models.CharField(max_length=255, blank=True, null=True)
    specialite_m1 = models.CharField(max_length=255, blank=True, null=True)
    nature_l3 = models.CharField(max_length=255, blank=True, null=True)
    specialite_l3 = models.CharField(max_length=255, blank=True, null=True)
    specialite_dt = models.CharField(max_length=255, blank=True, null=True)
    ante_arti1_auteur = models.CharField(max_length=255, blank=True, null=True)
    ante_arti1_an_pub = models.IntegerField(default=0)
    ante_arti2_auteur = models.CharField(max_length=255, blank=True, null=True)
    ante_arti2_an_pub = models.IntegerField(default=0)
    ante_arti3_auteur = models.CharField(max_length=255, blank=True, null=True)
    ante_arti3_an_pub = models.IntegerField(default=0)
    ante_arti4_auteur = models.CharField(max_length=255, blank=True, null=True)
    ante_arti4_an_pub = models.IntegerField(default=0)
    motivation = models.TextField()
    annee_inscription = models.CharField(max_length=4, blank=True, null=True)
    date_sel_m2 = models.DateField(blank=True, null=True)
    date_sou_m2 = models.DateField(blank=True, null=True)
    sujet_master2 = models.CharField(max_length=255)
    these_codt_nom = models.CharField(max_length=100, blank=True, null=True)
    these_codt_grade = models.IntegerField(default=0)
    specialite_codt = models.CharField(max_length=255, blank=True, null=True)
    m2_diro = models.CharField(max_length=255, blank=True, null=True)
    m1_etabl = models.CharField(max_length=255, blank=True, null=True)
    m1_dept = models.CharField(max_length=255, blank=True, null=True)
    comm_seminar = models.IntegerField(default=0)
    comm_conf = models.IntegerField(default=0)
    comm_societe_savante = models.IntegerField(default=0)
    m2_etabl = models.CharField(max_length=255, blank=True, null=True)
    m2_dept = models.CharField(max_length=255, blank=True, null=True)
    cursus_ante = models.IntegerField(default=0)
    these_deposited = models.IntegerField(default=0)
    these_deposited_dt = models.DateField(blank=True, null=True)
    dispo = models.IntegerField(default=0)
    source_fi = models.CharField(max_length=100)
    memo_titre = models.CharField(max_length=100, blank=True, null=True)
    memo_auteur = models.CharField(max_length=100, blank=True, null=True)
    memo_etabl = models.CharField(max_length=100, blank=True, null=True)
    memo_dept = models.CharField(max_length=100, blank=True, null=True)
    memo_annee = models.IntegerField(default=0)
    oeuvre_titre_1 = models.CharField(max_length=100, blank=True, null=True)
    oeuvre_auteur_1 = models.CharField(max_length=100, blank=True, null=True)
    oeuvre_etabl_1 = models.CharField(max_length=100, blank=True, null=True)
    oeuvre_dept_1 = models.CharField(max_length=100, blank=True, null=True)
    oeuvre_annee_1 = models.IntegerField(default=0)
    oeuvre_titre_2 = models.CharField(max_length=100, blank=True, null=True)
    oeuvre_auteur_2 = models.CharField(max_length=100, blank=True, null=True)
    oeuvre_etabl_2 = models.CharField(max_length=100, blank=True, null=True)
    oeuvre_dept_2 = models.CharField(max_length=100, blank=True, null=True)
    oeuvre_annee_2 = models.IntegerField(default=0)
    oeuvre_titre_3 = models.CharField(max_length=100, blank=True, null=True)
    oeuvre_auteur_3 = models.CharField(max_length=100, blank=True, null=True)
    oeuvre_etabl_3 = models.CharField(max_length=100, blank=True, null=True)
    oeuvre_dept_3 = models.CharField(max_length=100, blank=True, null=True)
    oeuvre_annee_3 = models.IntegerField(default=0)
    memo_diro = models.CharField(max_length=45, blank=True, null=True)
    code_secret = models.CharField(max_length=50, blank=True, null=True)
    cni_num = models.CharField(max_length=12, blank=True, null=True)
    cni_date_del = models.DateField(blank=True, null=True)
    cni_par = models.CharField(max_length=100, blank=True, null=True)
    annee_1 = models.IntegerField(default=0)
    serie_1 = models.CharField(max_length=5, blank=True, null=True)
    mention_1 = models.CharField(max_length=30, blank=True, null=True)
    annee_2 = models.IntegerField(default=0)
    serie_2 = models.CharField(max_length=5, blank=True, null=True)
    mention_2 = models.CharField(max_length=30, blank=True, null=True)
    annee_3 = models.IntegerField(blank=True, null=True)
    serie_3 = models.CharField(max_length=5, blank=True, null=True)
    mention_3 = models.CharField(max_length=30, blank=True, null=True)
    note_phy = models.IntegerField(default=0)
    note_mat = models.IntegerField(default=0)
    note_ch = models.IntegerField(default=0)
    note_bio = models.IntegerField(default=0)
    centre_exam = models.IntegerField(default=0)
    master = models.IntegerField(default=0)
    master_option = models.IntegerField(default=0)
    athlete = models.BooleanField(default=False)
    judo = models.BooleanField(default=False)
    tennis_lawn = models.BooleanField(default=False)
    tennis_table = models.BooleanField(default=False)
    foot_ball = models.BooleanField(default=False)
    basket_ball = models.BooleanField(default=False)
    hand_ball = models.BooleanField(default=False)
    volley_ball = models.BooleanField(default=False)
    medaille = models.BooleanField(default=False)
    or_field = models.BooleanField(db_column='or', blank=True,
                                   null=True)  # Field renamed because it was a Python reserved word.
    argent = models.BooleanField(default=False)
    bronze = models.BooleanField(default=False)
    sport_paralympique = models.BooleanField(default=False)
    nanbudo = models.BooleanField(default=False)
    karate = models.BooleanField(default=False)
    lutte = models.BooleanField(default=False)
    gymnastique = models.BooleanField(default=False)
    boxe = models.BooleanField(default=False)

    class Meta:
        db_table = 'dossier_univs'
        verbose_name_plural = 'Dossiers universitaires'

    # def __str__(self):
    #     return f'Dossier de {self.nom}'

    def __str__(self):
        return 'Dossier de {}'.format(self.nom)
