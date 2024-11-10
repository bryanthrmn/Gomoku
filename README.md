# Gomoku en Python

![H2x1_NSwitchDS_GomokuLetsGo](https://github.com/bryanthrmn/Gomoku/assets/85101130/7982b377-27f2-4679-ba0a-40188208cfa4)

**Auteurs**: Bryan Thirimanna, Louis Lucas, Raphaël Vey  
**École**: EPF  
**Projet**: Python – 1ère année (2023-2024)  

## Introduction
Ce projet présente notre adaptation en Python du jeu de société Gomoku (puissance 5). Réalisé dans le cadre de notre cours de programmation, il vise à offrir une version simplifiée mais complète du jeu, incluant des fonctionnalités essentielles telles que la gestion de parties, la création de profils, et la vérification des conditions de victoire.

## Fonctionnalités

- **Menu principal** : accès aux options pour démarrer, continuer une partie, afficher les règles et les crédits, ou quitter.
- **Boucle de jeu** : alternance des tours de jeu avec affichage des grilles et vérification des conditions de victoire.
- **Sauvegarde** : option pour sauvegarder et charger une partie (en cours de développement).
- **Affichage des règles et crédits** : informations sur le jeu et les auteurs.
- **Gestion des scores** : suivi des scores des joueurs à travers les parties.

## Structure du Programme

### Variables Importantes
Parmi les variables importantes, on retrouve :
- **jr_1, jr_2** : informations des joueurs (pseudonymes, numéros, scores).
- **grille** : structure principale du jeu, une liste de listes représentant la grille 5x5.
- **max_tour** : limite de tours pour chaque partie.

### Fonctions Clés
Liste des principales fonctions :
- `afficher_grille(grille)`: affiche la grille de jeu.
- `premier_tour(grille)`: détermine le joueur qui commence.
- `tour(grille, joueur)`: gère le tour de chaque joueur.
- `sauvegarde(joueur1, joueur2, grille)`: enregistre l’état de la partie en JSON.
- `chargement()`: charge une partie sauvegardée.

## Fonctionnalités Implémentées

| Fonctionnalité                           | État           |
|------------------------------------------|----------------|
| Nouvelle partie                          | Fonctionnel    |
| Continuer partie                         | Non fonctionnel|
| Afficher les règles du jeu               | Fonctionnel    |
| Afficher les crédits                     | Fonctionnel    |
| Création des profils joueurs             | Fonctionnel    |
| Afficher la grille                       | Fonctionnel    |
| Commande « Stop » pour quitter           | Fonctionnel    |
| Commande « Save » pour sauvegarder       | Non fonctionnel|
| Jeu, tour à tour                         | Fonctionnel    |
| Conditions de victoire                   | Fonctionnel    |
| Gestion des scores                       | Fonctionnel    |
| Mode IA (robot intelligent)              | Non implémenté |
| Interface graphique                      | Non implémenté |

## Conclusion
Notre adaptation de Gomoku a permis de développer nos compétences en programmation Python en concevant un jeu interactif et documenté. Bien que plusieurs fonctionnalités soient fonctionnelles, la gestion des sauvegardes et l’implémentation d’une interface graphique ou d’une IA sont des améliorations envisagées pour rendre le jeu plus complet et attractif.

### Liens
- **Projet sur GitHub** : [Gomoku](https://github.com/bryanthrmn/Gomoku/tree/main)
