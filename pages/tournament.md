
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
AB12345  Robert     Arthur    12/11/1999       
CD56789  Edouard    Jean      20/05/1982       
FG85236  Berlioz    Hector    30/06/1952       
RF58741  Danemaze   Victor    25/12/1993       
MP65897  Vitelle    Henri     24/07/2002       
FG45623  Mira       Pablo     12/08/2002       
GH85142  Berlioz    Maurice   25/09/1932       
JU58412  Malo       Loan      10/01/2010 

1. Commencer le tournoi
2. Revenir à la liste des tournois

Q. Quitter le programme
------------------------------------
Veuillez sélectionner une option (1-2 / Q) :
```

### 3.5 Round tournoi

#### 3.5.1 Lancement premier round : 
```plaintext
====================================
       DÉTAILS D'UN TOURNOI
====================================
Nom : Open
Lieu : Paris
Remarque : Tournois Open de Paris

Joueurs : 

ID       Nom        Prénom    Date de naissance
AB12345  Robert     Arthur    12/11/1999       
CD56789  Edouard    Jean      20/05/1982       
FG85236  Berlioz    Hector    30/06/1952       
RF58741  Danemaze   Victor    25/12/1993       
MP65897  Vitelle    Henri     24/07/2002       
FG45623  Mira       Pablo     12/08/2002       
GH85142  Berlioz    Maurice   25/09/1932       
JU58412  Malo       Loan      10/01/2010 

Round 1 : 
    Match 1 : Robert Arthur AB12345 - Edouard Jean CD56789
    Match 2 : Berlioz Hectore FG85236 - Danemaze Victor RF58741
    Match 3 : Vitelle Henri MP65897 - Mira Pablo FG45623
    Match 4 : Bezlioz Maurice GH85142 - Malo Loan JU58412

Résultat Round 1 : 
    1. Entrez le résultat du Match 1
    2. Entrez le résultat du Match 2
    3. Entrez le résultat du Match 3
    4. Entrez le résultat du Match 4

5. Revenir à la liste des tournois

Q. Quitter le programme
------------------------------------
Veuillez sélectionner une option (1-5 / Q) :
```

#### 3.5.2 Résultat premier round : 
```plaintext
====================================
       DÉTAILS D'UN TOURNOI
====================================
Nom : Open
Lieu : Paris
Remarque : Tournois Open de Paris

Joueurs : 

ID       Nom        Prénom    Date de naissance
AB12345  Robert     Arthur    12/11/1999       
CD56789  Edouard    Jean      20/05/1982       
FG85236  Berlioz    Hector    30/06/1952       
RF58741  Danemaze   Victor    25/12/1993       
MP65897  Vitelle    Henri     24/07/2002       
FG45623  Mira       Pablo     12/08/2002       
GH85142  Berlioz    Maurice   25/09/1932       
JU58412  Malo       Loan      10/01/2010 

Round 1 : 
    Match 1 : Robert Arthur AB12345 - Edouard Jean CD56789
    Match 2 : Berlioz Hectore FG85236 - Danemaze Victor RF58741
    Match 3 : Vitelle Henri MP65897 - Mira Pablo FG45623
    Match 4 : Bezlioz Maurice GH85142 - Malo Loan JU58412

Résultat Round 1 : 
    1. Mactch 1 : Résultat saisit
    2. Entrez le résultat du Match 2
    3. Entrez le résultat du Match 3
    4. Entrez le résultat du Match 4

5. Revenir à la liste des tournois

Q. Quitter le programme
------------------------------------
Veuillez sélectionner une option (1-5 / Q) :
```