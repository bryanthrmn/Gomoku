# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:01:30 2024

@author: Bryan Thirimanna
"""

import random
import json
import os

jr_1 = {"pseudo": "", "nb": 1, "fin du match": "", "score": 0}
jr_2 = {"pseudo": "", "nb": -1, "fin du match": "", "score": 0}

max_tour = 225

Alphabet = "ABCDEFGHIJKLMNO"

# Création de la grille et définition des unicodes qui seront utilisés par les joueurs
def afficher_grille(grille):
    s = "   │"
    for i in range(len(grille)):
        s += "{:^3}│".format(i+1)
    print(s)

    line = len(grille)*(3*"─"+"┼") + 3*"─"+"┤"

    nligne = 65
    for ligne in grille:
        print(line)
        s= "{:^3}│".format(chr(nligne))
        for case in ligne:
            if case==0:
                s += "{:3}│".format(3*" ")
            elif case == 1:
                s += "{:3}│".format(" \u25CF")
            else :
                s += "{:3}│".format(" \u25CB")
        print(s)
       
        nligne += 1
   
    lastline = len(grille)*(3*"─"+"┴") + 3*"─"+"┘"
    print(lastline)

# Tirage aléatoire pour déterminer qui sera le joueur avec les jetons noirs et celui avec les jetons blancs
def premier_tour(grille):
    grille[7][7] = 2
    var = random.randint(1,2)
    if var == 1:
        saisie = input()
        print("Vous êtes le joueur 1")
        print("")
        premier_jr = 1
    else:
        print("Vous êtes le joueur 2")
        print("")
        premier_jr = 2
    return var

# Définition de l'ordre des joueurs
def ordre(der_jr, jr_1, jr_2):
    if(der_jr == 2):
        der_jr = 1
        print(f"C'est à {jr_1} de jouer.")
    else:
        der_jr = 2
        print(f"C'est à {jr_2} de jouer.")
    return(der_jr)
   
# Affichage d'un message utile pour la fonction Coords
def Afficher_msg(msg):
    print(msg)

# Vérification des coordonnées rentrées / "save" pour sauvegarder la partie / "help" pour regarder les règles du jeu
def Coords(Joue, grille):
    Afficher_msg("Entrez vos coordonnées:")
    saisie = input()

    while True:
        saisie = saisie.upper()
        
        if saisie == "SAVE" and Joue > 1:  # Modifier cette ligne
            sauvegarde(jr_1, jr_2, grille, Joue)
        elif saisie == "STOP":
            print("La partie a été interrompue !")
            print("")
            main()
        elif saisie == "HELP":
            afficher_aide()
        elif len(saisie) >=2 and len(saisie) <=3:
            if saisie[0] in 'ABCDEFGHIJKLMNO':
                if saisie[1:].isdigit() and int(saisie[1:])>=1 and int(saisie[1:])<=15:
                    return saisie
        else:
            Afficher_msg("Commande invalide (tapez 'help' si besoin d'aide)")
            Afficher_msg("Entrez vos coordonnées:")
        
        saisie = input()


           
# Affichage règles du jeu
def afficher_aide():
    print("============= Règles du jeu =============")
    print("Le but du jeu est d'aligner cinq pions horizontalement, verticalement ou en diagonale.")
    print("Pour placer un pion, entrez les coordonnées de la case où vous souhaitez le placer.")
    print("Les coordonnées sont composées d'une lettre de A à O et d'un nombre de 1 à 15, sans espaces entre les deux.")
    print("Par exemple, pour placer un pion à la case A1, tapez simplement 'A1'.")
    print("Le premier joueur joue automatiquement sur la case du milieu (H8).")
    print("Amusez-vous bien !")
    print("")
    print("")      
    
# Chiffrer les coordonnées du joueurs : exemple : "B6" ==> "1, 5"
def Coords2Nums(pos):
    return ord(pos[0])-65, int(pos[1:])-1

# Vérification de l'état de la case
def verif(grille, coordonee_x, coordonee_y):
        valeur_case_tirée = int(grille[coordonee_x][coordonee_y])
        i = valeur_case_tirée
        if i == 0 :
            return 1
        else :
            return 0
           
# Si les coordonnées sont bien rentrées ; ajout du pion du joueur dans la case
def tour(grille, der_jr, Joue):
    pion_posable = 0
    while (pion_posable == 0):
        Coordonees_saisie = Coords(Joue, grille)
        coords_pos_x, coords_pos_y = Coords2Nums(Coordonees_saisie)
        pion_posable = verif(grille, coords_pos_x, coords_pos_y)
        if pion_posable == 0:
            print("Erreur : la case est déjà occupée. Veuillez choisir une autre case.")
    grille[coords_pos_x][coords_pos_y] = der_jr


# Vérifie les alignements dans la grille pour déterminer le gagnant. Si un joueur aligne cinq jetons, il gagne ; s'il en aligne six, il perd. Les scores sont ensuite mis à jour.r
def condition_pour_gagner(grille, jr_1, jr_2, scores):
    longueur_grille = len(grille)
    largeur_grille = len(grille[0])

    for i in range(0, longueur_grille):
        for j in range(0, largeur_grille - 6):
            if (grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3] == grille[i][j+4] == grille[i][j+5] == 1):
                print(f"Il est interdit d'alligner 6 jetons de même couleurs {jr_2} a gagné")
                scores[1] += 1
                return 2
            elif (grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3] == grille[i][j+4] == grille[i][j+5] == 2):
                print(f"Il est interdit d'alligner 6 jetons de même couleurs {jr_1} a gagné")
                scores[0] += 1
                return 1
    for j in range(0, largeur_grille):
        for i in range(0, longueur_grille - 6):
            if (grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j] == grille[i+4][j] == grille[i+5][j] == 1):
                print(f"Il est interdit d'alligner 6 jetons de même couleurs {jr_2} a gagné")
                scores[1] += 1
                return 2
            elif (grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j] == grille[i+4][j] == grille[i+5][j] == 2):
                print(f"Il est interdit d'alligner 6 jetons de même couleurs {jr_1} a gagné")
                scores[0] += 1
                return 1
    for i in range(0, longueur_grille - 6):
        for j in range(0, largeur_grille - 6):
            if (grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3] == grille[i+4][j+4] == grille[i+5][j+5] == 1):
                print(f"Il est interdit d'alligner 6 jetons de même couleurs {jr_2} a gagné")
                scores[1] += 1
                return 2
            elif (grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3] == grille[i+4][j+4] == grille[i+5][j+5] == 2):
                print(f"Il est interdit d'alligner 6 jetons de même couleurs {jr_1} a gagné")
                scores[0] += 1
                return 1
    for i in range(0, longueur_grille - 6):
        for j in range(5, largeur_grille):
            if (grille[i][j] == grille[i+1][j-1] == grille[i+2][j-2] == grille[i+3][j-3] == grille[i+4][j-4] == grille[i+5][j-5] == 1):
                print(f"Il est interdit d'alligner 6 jetons de même couleurs {jr_2} a gagné")
                scores[1] += 1
                return 2
            elif (grille[i][j] == grille[i+1][j-1] == grille[i+2][j-2] == grille[i+3][j-3] == grille[i+4][j-4] == grille[i+5][j-5] == 2):
                print(f"Il est interdit d'alligner 6 jetons de même couleurs {jr_1} a gagné")
                scores[0] += 1
                return jr_1
           
    # Check horizontal
    for i in range(0, longueur_grille):
        for j in range(0, largeur_grille - 5):
            if (grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3] == grille[i][j+4] == 1):
                print(f"{jr_1} a gagné")
                scores[0] += 1
                return 1
            elif (grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3] == grille[i][j+4] == 2):
                print(f"{jr_2} a gagné")
                scores[1] += 1
                return 2

    # Check vertical
    for j in range(0, largeur_grille):
        for i in range(0, longueur_grille - 5):
            if (grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j] == grille[i+4][j] == 1):
                print(f"{jr_1} a gagné")
                scores[0] += 1
                return 1
            elif (grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j] == grille[i+4][j] == 2):
                print(f"{jr_2} a gagné")
                scores[1] += 1
                return 2

    # Check diagonal
    for i in range(0, longueur_grille - 5):
        for j in range(0, largeur_grille - 5):
            if (grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3] == grille[i+4][j+4] == 1):
                print(f"{jr_1} a gagné")
                scores[0] += 1
                return 1
            elif (grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3] == grille[i+4][j+4] == 2):
                print(f"{jr_2} a gagné")
                scores[1] += 1
                return 2
    for i in range(0, longueur_grille - 5):
        for j in range(5, largeur_grille):
            if (grille[i][j] == grille[i+1][j-1] == grille[i+2][j-2] == grille[i+3][j-3] == grille[i+4][j-4] == 1):
                print(f"{jr_1} a gagné")
                scores[0] += 1
                return 1
            elif (grille[i][j] == grille[i+1][j-1] == grille[i+2][j-2] == grille[i+3][j-3] == grille[i+4][j-4] == 2):
                print(f"{jr_2} a gagné")
                scores[1] += 1
                return 2
    return 0

# Fonctionnement du programme le long d'une partie jusqu'à ce qu'il y ait un vainqueur ou une égalité
def partie(grille, max_tour, premier_jr, jr_1, jr_2, joueur_gagnant, scores, Joue):
    if (premier_jr == 0):
        premier_jr = premier_tour(grille)
    else:
        grille[7][7] = 2
        if (premier_jr == 1):
            premier_jr = 2
            print(f"{jr_2} commence")
        else:
            premier_jr = 1
            print(f"{jr_1} commence")
    der_jr = premier_jr
    for i in range (max_tour):
        der_jr = ordre(der_jr, jr_1, jr_2)
        tour(grille, der_jr, Joue)
        afficher_grille(grille)
        gagnant = condition_pour_gagner(grille, jr_1, jr_2, scores)
        if (gagnant > 0):
            print ("Fin de la partie")
            break
        if (i == max_tour):
            print ("Partie nulle")
            break
    replay = restart(joueur_gagnant, scores)
    return replay, premier_jr

# Demande aux joueurs s'ils veulent rejouer
def restart(joueur_gagnant, scores):
  while True:
    print("")
    print("Tableau de scores :")
    print (scores)
    print("")
    reponse = input("Voulez-vous continuer ? (oui/non) ").lower()
    if reponse in ["oui", "non"]:
        if (reponse == "oui"):
            return 1
        if (reponse == "non"):
            return 0
    else:
      print("Saisie invalide. Veuillez saisir 'oui' ou 'non'.")
      print("")

# Fonction principale qui gère chaque partie ainsi que le score au fur des parties et permet aux joueurs de choisir au début de la première parties leurs pseudo en vérifiant qu'ils soient bien différents
def main():
    while True:
        print("============= Bienvenue dans Gomoku ! =============")
        print("Un projet Python réalisé par 3 étudiants de l'EPF")
        print("Bryan THIRIMANNA, Louis LUCAS et Raphaël VEY")
        print("")
        print("[1] Nouvelle partie")
        print("[2] Continuer partie")
        print("[3] Règles du jeu")
        print("[4] Crédits")
        print("[5] Quitter")
        print("")
        choix = input("Que souhaitez-vous faire ? ")
        print("")
        print("")
        
        if choix == "1":
            main_nouvelle_partie()
        elif choix == "2":
            main_continuer_partie()
        elif choix == "3":
            afficher_aide()
        elif choix == "4":
            afficher_credits()
        elif choix == "5":
            print("=================== Quitter ===================") # Quitte la boucle de la fonction principale
            print("Merci d'avoir joué à Gomoku ! Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide (1-5).")
            print()

def main_nouvelle_partie():
    global jr_1, jr_2, max_tour, grille
    # Demande aux joueurs leurs pseudos
    print("=================== Nouvelle Partie ==================")
    print("")
    print("Avant de commencer la partie, nous aurions besoin de 2 pseudos !")
    print("")
    player1 = input("Nom du joueur 1: ")
    player2 = input("Nom du joueur 2: ")
    while player1 == player2:
        print("Ce pseudo est déjà utilisé")
        player2 = input("Entrez un nouveau pseudo: ")
    print("")
    print("Nouvelle partie entre %s et %s" %(player1, player2))
    jr_1 = player1
    jr_2 = player2
    main_partie()

# Cherche s'il existe un fichier pour reprendre une partie 
def main_continuer_partie():
    global jr_1, jr_2, max_tour, grille, Joue
    grille = init_grille()  # Initialise grille avant l'appel à chargement
    Joue = 0  # Initialise Joue
    jr_1, jr_2, grille, Joue = chargement(jr_1, jr_2, grille, Joue)
    if Joue == 0:  # Vérification de la sauvegarde
        print("Aucune sauvegarde trouvée.")
        print("")
        main()
    else:
        print("================= Continuer Partie ==================")
        print("Chargement de la partie...")
        print("Partie en cours entre %s et %s" %(jr_1, jr_2))


# Affichage
def afficher_credits():
    print("====================== Crédits ======================")
    print("Ce jeu a été conçu par 3 étudiants de l'EPF dans le cadre d'un projet semestriel.")
    print("Bryan THIRIMANNA - Louis LUCAS - Raphaël VEY")
    print("1A - FB - Semestre 2 - 2024")
    print("")

def main_partie():
    global jr_1, jr_2, max_tour, grille
    Joue = 0
    joueur_gagnant = None
    scores = [0, 0]
    premier_jr = 0
    rejouer = 1
    while (rejouer == 1):
        grille = [[0] * 15 for _ in range(15)]  # Réinitialisation de la grille
        rejouer, premier_jr = partie(grille, max_tour, premier_jr, jr_1, jr_2, joueur_gagnant, scores, Joue)

# Initialise la grille de départ, pour qu'elle soit vide à chaque début de partie
def init_grille():
    grille = [[0] * 15 for _ in range(15)]
    return grille

# Effectuer une sauvegarde dans un fichier extérieur
def sauvegarde(jr_1, jr_2, grille, Joue):
    dossier_gomoku = "dossier_gomoku"
    if not os.path.exists(dossier_gomoku):
        os.mkdir(dossier_gomoku)
    data = [jr_1, jr_2, grille, Joue]
    fichier_path = os.path.join(dossier_gomoku, "sauvegarde.json")
    with open(fichier_path, "w") as fichier:
        json.dump(data, fichier)


# Fonction permettant de charger une nouvelle partie avec en entrée un tableau, 2 dictionnaires et un chiffre et en sortie les mêmes variables
def chargement(jr_1, jr_2, grille, Joue):
    fichier_path = os.getcwd() + "/dossier_gomoku/sauvegarde.json"
    if os.path.exists(fichier_path):  # Vérifie si le fichier de sauvegarde existe
        fichier = open(fichier_path, "r")
        data = json.load(fichier)
        print("Une ancienne partie a été chargée.")
        return data[0], data[1], data[2], data[3]
    else:
        return jr_1, jr_2, grille, Joue

main()
