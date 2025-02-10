# Centre Échecs - Interface Terminal

## **1. Menu Principal**
```plaintext
====================================
   BIENVENUE DANS LE CENTRE ÉCHECS
====================================
1. Aller au menu joueur
2. Aller au menu tournoi

Q. Quitter le programme
------------------------------------
Veuillez sélectionner une option (1-2 / Q) :
```

## **2. Gestion des Joueurs**
### Écran : Gestion des joueurs
```plaintext
====================================
        GESTION DES JOUEURS
====================================
ID       Nom     Prénom  Date de naissance
AB12345  Robert  Arthur  01/01/1900
CD67890  Dupont  Paul    10/11/1900

------------------------------------
1. Ajouter un joueur
2. Retour au menu principal

Q. Quitter le programme
------------------------------------
Veuillez sélectionner une option (1-2 / Q) :
```

### 2.1 Ajouter un joueur
```plaintext
====================================
       AJOUTER UN NOUVEAU JOUEUR
====================================
Prénom : [Saisir le prénom]
Nom : [Saisir le nom]
Date de naissance (JJ/MM/AAAA) : [Saisir la date]
Identifiant national d’échecs : [Saisir l'identifiant]

------------------------------------
[Nouveau joueur ajouté avec succès !]
Appuyez sur Entrée pour continuer...
```

<!-- 

Si un tournoi est sélectionné :
```plaintext
====================================
       AJOUTER UN NOUVEAU TOUR
====================================
Nom du tour (par ex. Round 1) : [Saisir le nom]
Nombre de matchs : [Saisir le nombre]
Veuillez définir les paires et scores :
1. [Nom joueur 1] vs [Nom joueur 2] - Score : [0.0] [0.0]
2. [Nom joueur 3] vs [Nom joueur 4] - Score : [0.5] [0.5]
...
------------------------------------
[Tour ajouté avec succès !]
Appuyez sur Entrée pour continuer...
```

### 3.3 Afficher les rapports d’un tournoi
```plaintext
====================================
    RAPPORTS POUR LES TOURNOIS
====================================
Liste des tournois :
1. [Nom du tournoi 1]
2. [Nom du tournoi 2]
...
Veuillez sélectionner un tournoi (1-... ou 0 pour retourner) :
```
Si un tournoi est sélectionné :
```plaintext
====================================
   DÉTAILS DU TOURNOI : [Nom]
====================================
Lieu : [Lieu]
Dates : [Date de début] - [Date de fin]
Joueurs inscrits :
  1. [Nom joueur 1] - [Identifiant]
  2. [Nom joueur 2] - [Identifiant]
Tours :
  Round 1 :
    Match 1 : [Nom joueur 1] vs [Nom joueur 2] (1.0 / 0.0)
    Match 2 : ...
------------------------------------
Appuyez sur Entrée pour retourner au menu précédent...
``` -->

### **4. Quitter le programme**
```plaintext
====================================
MERCI D’AVOIR UTILISÉ L’APPLICATION
====================================
```
