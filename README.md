# **DOCTOLIB**

**Application web permettant à des médecins de pratiquer des suivies de patient via des questionnaires périodiques.**

## *Rappel du brief*

[Lien du brief](https://simplonline.co/briefs/3e2826a1-ad1b-4543-b6d0-68e01d0a46a6)

Vous êtes embauché en tant que consultant Data pour DoctoLib, une entreprise française qui met en relation des  professionnels de la santé et des patients au travers d’une interface web ainsi qu’une application mobile.

Votre responsable, Mark Musk, veut ajouter de nouvelles fonctionnalités pour attirer encore plus de professionnels de la santé. Il souhaite leur permettre de mener des enquêtes de santé publique sur un échantillon de patients consentants pour arriver à des conclusions qui seront publiées dans des magazines de santé.

## *Compétences visées*

- Concevoir une base de données analytique avec l’approche orientée requêtes en vue de la mise à disposition des données pour un traitement analytique ou d’intelligence artificielle.

- Programmer l’import de données initiales nécessaires au projet en base de données, afin de les rendre exploitables par un tiers, dans un langage de programmation adapté et à partir de la stratégie de nettoyage des données préalablement définie.

- Préparer les données disponibles depuis la base de données analytique en vue de leur utilisation par les algorithmes d’intelligence artificielle.

## *Base de données*

![img](https://media.discordapp.net/attachments/499624490016440350/1174646025525407774/db.sqlite3.png?ex=6568595c&is=6555e45c&hm=b48a626bec8cdab4fce182a1824068c5e610cc2d08fb00ae883741700e234c1d&=&width=810&height=483 "Schéma de la base de données associé au site")

Il y a trois types d'utilisateur : responsable, médecin et patient.

- Le responsable peut assigner des patients à un médecin
- Le médecin a accès au résultat de ses patients
- Le patient peut répondre aux formulaires

## *Initialisation du projet*

Pour démarrer le projet, voici les étapes à suivre :

***Optionnel :** Vous pouvez créer un environnement virtuel pour votre projet.*

1. **Installer les librairies**  
`pip install -r requirements.txt`

2. **Effectuer les migrations**  
`python manage.py migrate`

3. **Créer un super user**  
`python manage.py createsuperuser`

4. **Lancer le serveur**  
`python manage.py runserver`

5. **Attribuer le rôle de responsable au super user**
   - Aller sur la page administrateur  
[`http://127.0.0.1:8000/admin`](http://127.0.0.1:8000/admin)

   - Se connecter avec le super user

   - Aller dans la liste des utilisateurs

   - Cliquer sur l'Id du super user pour le modifier

   - Attribuer le rôle "responsable" au super user  
![img](https://media.discordapp.net/attachments/499624490016440350/1174640893068849212/image.png?ex=65685494&is=6555df94&hm=d5c37d7bcc73e42d9e1343af89392f72c436bb2a0bd56a6fdaa0cfe0624d82c7&= "Image du site montrant le changement de rôle du super user")
