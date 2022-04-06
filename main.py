import cmd
import textwrap
import time 
import sys
import os
import random
from classes import Joueur

#### Carte ####
"""
Le joueur commence a la case a1
-------------
|a1|a2|a3|a4|
|b1|b2|b3|b4|
|c1|c2|c3|c4|
|d1|d2|d3|d4|
|  |e2|e3|e4|
-------------
"""

def creer_carte():
                #Cases a
    zones_carte = {"a1":{"NOMZONE":"Maison","DESCRIPTION":"Jamais aussi bien que chez soi!","EXAMINATION":"Votre maison n'a pas bougé","RESOLUE":True,"HAUT":"","BAS":"b1","GAUCHE":"","DROITE":"a2"},
                "a2":{"NOMZONE":"Jardin","DESCRIPTION":"Jamais aussi bein servi que par son jardin!","EXAMINATION":"Vos tomates sont bien rouges","RESOLUE":True,"HAUT":"","BAS":"b2","GAUCHE":"a1","DROITE":"a3"},
                "a3":{"NOMZONE":"Bosquet de Ronces","DESCRIPTION":"Nuisibles et Epineuses","EXAMINATION":"C est un ennemi","RESOLUE":False,"HAUT":"","BAS":"","GAUCHE":"a2","DROITE":"a4"},
                "a4":{"NOMZONE":"Pasage Caché","DESCRIPTION":"Sombre et Suspicieux","EXAMINATION":"Pasage trouvé arés avoir exterminer les Ronces","RESOLUE":False,"HAUT":"","BAS":"","GAUCHE":"a3","DROITE":""},
                #Cases b
                "b1":{"NOMZONE":"Long Chemin","DESCRIPTION":"Un kilométre a pied ça use, ça use, deux kilométres a pieds ça use les souliers !!","EXAMINATION":"Chemin qui méne a la ville la plus proche","RESOLUE":True,"HAUT":"a1","BAS":"c1","GAUCHE":"","DROITE":"c2"},
                "b2":{"NOMZONE":"Passage vers la forêt","DESCRIPTION":"Attention au grand méchant loup!","EXAMINATION":"Simple chemin","RESOLUE":False,"HAUT":"a2","BAS":"c2","GAUCHE":"c1","DROITE":"c3"},
                "b3":{"NOMZONE":"Taniére du Loup solitaire","DESCRIPTION":"Le grand méchant loup se repose dans son antre!","EXAMINATION":"C est un ennemi","RESOLUE":False,"HAUT":"a3","BAS":"c3","GAUCHE":"c2","DROITE":"c4"},
                "b4":{"NOMZONE":"Caverne des Loups","DESCRIPTION":"Escarpé et Humide","EXAMINATION":"Caverne trouvé sous un tas d'os","RESOLUE":False,"HAUT":"a4","BAS":"c4","GAUCHE":"c3","DROITE":""},
                #Cases c
                "c1":{"NOMZONE":"Long Chemin","DESCRIPTION":"Trois kilométres a pieds ça use, ça use, quatre kilométres a pieds ça use les souliers !!","EXAMINATION":"Fin du chemin vous arriverez a la ville!","RESOLUE":True,"HAUT":"b1","BAS":"d1","GAUCHE":"","DROITE":"c2"},
                "c2":{"NOMZONE":"Plaines","DESCRIPTION":"Un bel étalon s'y cache peut-être!?","EXAMINATION":"Trouvez une monture!","RESOLUE":False,"HAUT":"","BAS":"","GAUCHE":"c1","DROITE":"c3"},
                "c3":{"NOMZONE":"Ruche","DESCRIPTION":"Mmmh du miel!!","EXAMINATION":"Le miel soigne!","RESOLUE":False,"HAUT":"","BAS":"d3","GAUCHE":"c2","DROITE":""},
                "c4":{"NOMZONE":"Cavenre des Loups 1er étage","DESCRIPTION":"Vous entrez dans un donjon restez sur vos gardes!","EXAMINATION":"Ennemi présents: Gobelin (niv1)","RESOLUE":False,"HAUT":"b4","BAS":"d4","GAUCHE":"","DROITE":""},
                #Cases d
                "d1":{"NOMZONE":"Ville de ","DESCRIPTION":"Capitale du continent de Glims, des sons joyeux et une odeur de repas agréable s'en échape. Lorsque vous penetrez dans la ville les bâtisses sont magnifiquement décorées et un aubergiste vous interpelle pour vous proposez des couverts et un toit ! Vous acceptez de bon coeur et recouvez tout vos PV et MP.","EXAMINATION":"Vous entendez des brides de conversations a propos d une caverne remplie d or. Poursuivez votre chemin pour vous y rendre. ","RESOLUE":False,"HAUT":"c1","BAS":"","GAUCHE":"","DROITE":"d2"},
                "d2":{"NOMZONE":"Montagnes escarpées","DESCRIPTION":"De très hautes montagnes tout aussi dangereuses qu'imposantes","EXAMINATION":"RAS","RESOLUE":False,"HAUT":"c2","BAS":"","GAUCHE":"d1","DROITE":"d3"},
                "d3":{"NOMZONE":"Repére des brigants","DESCRIPTION":"Une tour très grande où vivent des brigants cachant probablement un grand trésor!","EXAMINATION":"Fouillez bien!","RESOLUE":False,"HAUT":"","BAS":"e3","GAUCHE":"d2","DROITE":""},
                "d4":{"NOMZONE":"Cavenre des Loups second étage","DESCRIPTION":"Vous entrez dans le deuxiéme étage du donjon les monstres seront de plus en plus forts!","EXAMINATION":"Ennemi présents: Gobelin (niv2) & Orc(niv2)","RESOLUE":False,"HAUT":"c4","BAS":"e4","GAUCHE":"","DROITE":""},
                #Cases e
                "e2":{"NOMZONE":"Caverne d'Alibaba","DESCRIPTION":"De l'or! Beaucoup d'or! Même Midas n'en avait pas autant!","EXAMINATION":"Fin de l'aventure!","RESOLUE":False,"HAUT":"","BAS":"","GAUCHE":"","DROITE":""},
                "e3":{"NOMZONE":"Porte Inconnue","DESCRIPTION":"Un mur!?","EXAMINATION":"Vous avez le mot de passe?","RESOLUE":False,"MOTDEPASSE":False,"HAUT":"d3","BAS":"","GAUCHE":"e2","DROITE":""},
                "e4":{"NOMZONE":"Cavenre des Loups troisiéme étage","DESCRIPTION":"Vous entrez dans le troisiéme étage du donjon! Le Boss fait son entrée!","EXAMINATION":"Ennemi présents: Seigneur Orc(niv10)","RESOLUE":False,"HAUT":"d4","BAS":"","GAUCHE":"","DROITE":""},}
    return zones_carte


    
#### Menu Principal ####
def selections_menu_principal():
    quitter = False
    while not quitter:
        option = input("> ")
        if option.lower() == ("jouer"):
            lancer_jeu()
        elif option.lower() == ("aide"):
            menu_aide()
        elif option.lower() == ("quitter"):
            quitter = True
    sys.exit()
    
def menu_principal():
    #os.system("clear")
    print("#######################")
    print("# Bienvenu dans Glims #")
    print("#######################")
    print("  -  Jouer  -")
    print("  -  Aide   -")
    print("  - Quitter -")
    selections_menu_principal()
    
def menu_aide():
    os.system("clear")
    print("###################################")
    print("# Bienvenu dans le guide de Glims #")
    print("###################################")
    print("  - Ecrivez Se Deplacer, Bouger ou Aller a pour selectionner l'option avancer puis Haut, Bas, Gauche, Droite pour vous déplacer -")
    print("  - Ecrivez Examiner, Regarder, Inspecter pour avoir plus d'informations sur une zone -")
    print("  - Les mots ont une importance! Peut-être que des commandes sont cachées! -")
    print("  - Bonne Chance et Bon Jeu -")
    print("Appuyer sur Entrée pour quitter le menu")
    menu_principal()

#### Fonctionalités du Jeu ####
def afficher_question(question, vitesse):
    for caractere in question:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(vitesse)
    
def initialiser_jeu():
    os.system('clear')
    #Creation de la carte#
    zones_carte = creer_carte()
    
    ### Fabrication du perso ###
    ## Nom ##
    question1 = "Bonjour, comment souhaitez-vous vous appeler? \n"
    afficher_question(question1, 0.05)
    nom = input("> ")
    
    ## Classe ##
    question2 = "Quel rôle souhaitez-vous avoir?\n"
    question2precisions = "(Vous pouvez jouer en tant que Guerrier, Prêtre, Magicien ou Nécromencien)\n"
    
    afficher_question(question2, 0.05)
    afficher_question(question2precisions, 0.01)
    classe_joueur = input("> ")
    classes_valides = ["guerrier", "prêtre", "magicien", "nécromencien"]
    if classe_joueur.lower() in classes_valides:
        print("Voue êtes un", classe_joueur, "\n")
    while classe_joueur.lower() not in classes_valides:
        classe_joueur = input("> ")
        if classe_joueur.lower() in classes_valides:
            print("Vous êtes un", classe_joueur, "\n")
    
    ### Stats du Joueur ###
    if classe_joueur.lower() == "guerrier":
        point_vie = 120
        point_magie = 20
    elif classe_joueur.lower() == "mage":
        point_vie = 20
        point_magie = 120
    elif classe_joueur.lower() == "prêtre":
        point_vie = 70
        point_magie = 70
    elif classe_joueur.lower() == "nécromencien":
        point_vie = 10
        point_magie = 140
    
    joueur1 = Joueur(nom, point_vie, point_magie, zones_carte["a1"], classe = classe_joueur.lower())
    return zones_carte, joueur1

def lancer_jeu():
    ### Mise en place du personnage & carte ###
    zones_carte, joueur1 = initialiser_jeu()
    nom_joueur = joueur1.get_nom()
    classe_joueur = joueur1.get_classe()
    
    ### INTRODUCTION ###
    phrase1 = f'Bienvenue {nom_joueur} le {classe_joueur} dans ce jeu de Fantaisie RPG!. \n'
    phrase2 = "J'éspére que tu vas l'apprécier\n"
    phrase3 = "Ne te pers pas ...\n"
    phrase4 = "HaHaHa...\n"
    afficher_question(phrase1, 0.03)
    afficher_question(phrase2, 0.03)
    afficher_question(phrase3, 0.1)
    afficher_question(phrase4, 0.2)
    
    os.system('clear')
    print("##########################")
    print("# Commençons maintenant! #")
    print("##########################")
    
    ### Lancement du jeu ###
    boucle_principale_jeu(zones_carte, joueur1)
    

def boucle_principale_jeu(zones_carte,joueur1):
    while joueur1.get_etat_partie() is False:
        interactions(zones_carte,joueur1)


#### Interaction du Jeu ####
def print_position(joueur1):
    position = joueur1.get_position()
    text = f'** {position["NOMZONE"]} : {position["DESCRIPTION"]} **'
    print("\n", "=" * (8 + len(text)))
    print("\n",text)
    print("\n", "=" * (8 + len(text)))
    
def interactions(zones_carte,joueur1):
    print_position(joueur1)
    position_joueur = joueur1.get_position()
    time.sleep(0.5)
    print("Que voulez vous faire?")
    action = input("> ")
    actions_possibles = ["se deplacer","bouger","aller a","examiner","inspecter","fouiller","quitter"]
    while action.lower() not in actions_possibles:
        print("Pas d'action connue")
        action = input("> ")
    if action.lower() == "quitter":
        sys.exit()
    elif action.lower() in ["se deplacer","bouger","aller a"]:
        mouvement_joueur(zones_carte,position_joueur, joueur1)
        time.sleep(1)
    elif action.lower() in ["examiner","inspecter","fouiller"]:
        examiner(action.lower(),action,position_joueur)
        time.sleep(1)
        
def mouvement_joueur(zones_carte, position_joueur, joueur1):
    direction_correcte = False
    while not direction_correcte:
        direction = input("Où voulez-vous aller?\n> ")
        if direction.lower() == "haut":
            if position_joueur["HAUT"] != "":
                destination = position_joueur["HAUT"]
                direction_correcte = True
        elif direction.lower() == "bas":
            if position_joueur["BAS"] != "":
                destination = position_joueur["BAS"]
                direction_correcte = True
        elif direction.lower() == "gauche":
            if position_joueur["GAUCHE"] != "":
                destination = position_joueur["GAUCHE"]
                direction_correcte = True
        elif direction.lower() == "droite":
            if position_joueur["DROITE"] != "":
                destination = position_joueur["DROITE"]
                direction_correcte = True
        else:
            print("Mouvement non disponible")
    deplacer_joueur(destination, zones_carte, joueur1)
        
def deplacer_joueur(destination, zones_carte, joueur1):
    nouvelle_position = zones_carte[destination]
    print("\n",f'Vous êtes maintenant à {nouvelle_position["NOMZONE"]}')
    joueur1.set_position(nouvelle_position)
    
def examiner(zones_map,action,position):
    if action in ["examiner","inspecter"]:
        #print("")
        print(position["EXAMINATION"])
        position["RESOLUE"] = True
    if action == "fouiller" and position == "d3":
        print("bravo vous avez trouvé le mot de passe pour la porte au sous sol")
        zones_map["e3"]["MOTDEPASSE"] = True
    
        
    
os.system('clear')
menu_principal()





"""
for element in zones_carte:
    print(zones_carte[element]["NOMZONE"],":",  zones_carte[element]["DESCRIPTION"])
"""

