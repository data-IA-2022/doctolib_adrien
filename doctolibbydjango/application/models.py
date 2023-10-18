from django.db import models
from authentification.models import Utilisateur

class donneeFormulaire(models.Model):

    idPatient = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='donneeFormulaire')

    CHOICES_RESPONSE = [
        (0, '0'),
        (1, '1'),
        (5, '5'),
        (10, '10'),
    ]

    irritabilite = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    sentiments_depressifs = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    bouche_seche_ou_gorge_seche = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    actions_ou_gestes_impulsifs = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    grincement_des_dents = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    difficulte_a_rester_assis = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    cauchemars = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    diarrhee = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    attaques_verbales_envers_quelquun = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    hauts_et_bas_emotifs = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    grande_envie_de_pleurer = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    grande_envie_de_fuir = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    grande_envie_de_faire_mal = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    pensees_embrouillees = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    debit_plus_rapide = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    fatigue_ou_lourdeur_generalisees = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    sentiment_detre_surchargé = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    sentiment_detre_emotionnellement_fragile = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    sentiment_de_tristesse = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    sentiment_danxiete = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    tension_emotionnelle = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    hostilite_envers_les_autres = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    tremblements_ou_gestes_nerveux = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    begaiements_ou_hesitations_verbales = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    incapacite_ou_difficulte_a_se_concentrer = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    difficulte_a_organiser_ses_pensees = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    difficulte_a_dormir_toute_la_nuit_sans_se_reveiller = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    besoin_frequent_duriner = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    maux_destomac_ou_difficultes_a_digerer = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    geste_ou_sentiment_dimpatience = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    maux_de_tete = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    douleurs_au_dos_ou_a_la_nuque = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    perte_ou_gain_dappetit = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    perte_dinteret_pour_le_sexe = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    oublis_frequents = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    douleurs_ou_serrements_a_la_poitrine = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    conflits_significatifs_avec_les_autres = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    difficultes_a_se_lever_apres_le_someil = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    sentiment_que_les_choses_sont_hors_de_controle = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    difficulte_a_faire_une_longue_activite_continue = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    mouvements_de_retrait_disolement = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    difficulte_a_sendormir = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    difficulte_a_se_remettre_dun_evenement_contrariant = models.IntegerField(choices=CHOICES_RESPONSE, default=0)
    mains_moites = models.IntegerField(choices=CHOICES_RESPONSE, default=0)

    total_impact_du_stress_dans_votre_vie_actuelle = models.IntegerField(default=0)
