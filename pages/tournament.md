
## **3. Gestion des Tournois**
### Écran : Gestion des tournois
```plaintext
====================================
        GESTION DES TOURNOIS
====================================
ID Nom   Lieu   
1  Open  Paris  
2  Open  Toulouse
3  Open  Bordeaux

------------------------------------
1. Créer un nouveau tournoi
2. Afficher les détails d’un tournoi
3. Retour au menu principal

Q. Quitter le programme
------------------------------------
Veuillez sélectionner une option (1-3 / Q) :
```

### 3.1 Créer un nouveau tournoi
```plaintext
====================================
        CRÉER UN NOUVEAU TOURNOI
====================================
Nom du tournoi : [Saisir le nom]
Lieu : [Saisir le lieu]
Remarques (optionnel) : [Saisir des remarques]

------------------------------------
[Nouveau tournoi créé avec succès !]
Appuyez sur Entrée pour continuer...
```

### 3.2 Choisir un tournoi
```plaintext
====================================
      SÉLECTIONNER UN TOURNOI
====================================
ID Nom   Lieu   
1  Open  Paris  
2  Open  Toulouse
3  Open  Bordeaux

------------------------------------
Veuillez sélectionner un tournoi (1-3):
```

### 3.3 Détail d'un tournoi sans joueur

#### 3.3.1 Page détail
```plaintext
====================================
       DÉTAILS D'UN TOURNOI
====================================
Nom : Open
Lieu : Paris
Remarque : Tournois Open de Paris

Joueurs : Aucun joueur inscrit

1. Ajouter des joueurs au tournoi
2. Revenir à la liste des tournois

Q. Quitter le programme
------------------------------------
Veuillez sélectionner une option (1-3 / Q) :
```

#### 3.3.2 Ajout de joueur
```plaintext
====================================
    Ajout des joueurs au tournoi
====================================
Nom : Open
Lieu : Paris
Remarque : Tournois Open de Paris

Sélectionner les joueurs à ajouté au tournoi :

ID       Nom     Prénom  Date de naissance
AB12345  Robert  Arthur  01/01/1900
CD67890  Dupont  Paul    10/11/1900

Rentrer l'id du joueur 1 : 
Rentrer l'id du joueur 2 : 
Rentrer l'id du joueur 3 :
Rentrer l'id du joueur 4 :
Rentrer l'id du joueur 5 :
Rentrer l'id du joueur 6 :
Rentrer l'id du joueur 7 :
Rentrer l'id du joueur 8 :

Les 8 joueurs ont été ajouté avec succés !

1. Aller au détail du tournoi
2. Aller à la liste des tournois
3. Aller au menu principal

Q. Quitter le programme
```


### 3.4 Détail d'un tournoi avec joueur

#### 3.4.1 Page détail
```plaintext
====================================
       DÉTAILS D'UN TOURNOI
====================================
Nom : Open
Lieu : Paris
Remarque : Tournois Open de Paris

Joueurs : 
    ID       Nom        Prénom    Date de naissance
1.  AB12345  Robert     Arthur    12/11/1999       
2.  CD56789  Edouard    Jean      20/05/1982       
3.  FG85236  Berlioz    Hector    30/06/1952       
4.  RF58741  Danemaze   Victor    25/12/1993       
5.  MP65897  Vitelle    Henri     24/07/2002       
6.  FG45623  Mira       Pablo     12/08/2002       
7.  GH85142  Berlioz    Maurice   25/09/1932       
8.  JU58412  Malo       Loan      10/01/2010 

1. Ajouter des joueurs au tournoi
2. Revenir à la liste des tournois

Q. Quitter le programme
------------------------------------
Veuillez sélectionner une option (1-3 / Q) :
```