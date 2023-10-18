import random
from application.models import donneeFormulaire
from authentification.models import Utilisateur
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    LISTE_ATTR = [
        "irritabilite",
        "sentiments_depressifs",
        "bouche_seche_ou_gorge_seche",
        "actions_ou_gestes_impulsifs",
        "grincement_des_dents",
        "difficulte_a_rester_assis",
        "cauchemars",
        "diarrhee",
        "attaques_verbales_envers_quelquun",
        "hauts_et_bas_emotifs",
        "grande_envie_de_pleurer",
        "grande_envie_de_fuir",
        "grande_envie_de_faire_mal",
        "pensees_embrouillees",
        "debit_plus_rapide",
        "fatigue_ou_lourdeur_generalisees",
        "sentiment_detre_surchargé",
        "sentiment_detre_emotionnellement_fragile",
        "sentiment_de_tristesse",
        "sentiment_danxiete",
        "tension_emotionnelle",
        "hostilite_envers_les_autres",
        "tremblements_ou_gestes_nerveux",
        "begaiements_ou_hesitations_verbales",
        "incapacite_ou_difficulte_a_se_concentrer",
        "difficulte_a_organiser_ses_pensees",
        "difficulte_a_dormir_toute_la_nuit_sans_se_reveiller",
        "besoin_frequent_duriner",
        "maux_destomac_ou_difficultes_a_digerer",
        "geste_ou_sentiment_dimpatience",
        "maux_de_tete",
        "douleurs_au_dos_ou_a_la_nuque",
        "perte_ou_gain_dappetit",
        "perte_dinteret_pour_le_sexe",
        "oublis_frequents",
        "douleurs_ou_serrements_a_la_poitrine",
        "conflits_significatifs_avec_les_autres",
        "difficultes_a_se_lever_apres_le_someil",
        "sentiment_que_les_choses_sont_hors_de_controle",
        "difficulte_a_faire_une_longue_activite_continue",
        "mouvements_de_retrait_disolement",
        "difficulte_a_sendormir",
        "difficulte_a_se_remettre_dun_evenement_contrariant",
        "mains_moites",
    ]

    CHOICES = [0, 1, 5, 10]

    def handle(self, *args, **options):
        # Créer 20 objets donneeFormulaire avec des valeurs d'exemple
        for i in range(1, 21):

            dict_attr = {}
            total_stress = 0

            for k in Command.LISTE_ATTR:

                r = random.choice(Command.CHOICES)

                dict_attr[k] = r
                total_stress += r

            utilisateur = Utilisateur.objects.get(pk=i)
            donnee_formulaire = donneeFormulaire.objects.create(
                idPatient = utilisateur,
                **dict_attr,
                total_impact_du_stress_dans_votre_vie_actuelle = total_stress
            )
            print(utilisateur)

            # Sauvegarder l'objet dans la base de données
            donnee_formulaire.save()
