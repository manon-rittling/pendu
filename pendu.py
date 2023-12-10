#importation des bibliotheques
import pygame
from pygame.locals import *
import random

# initaialisation de pygame
pygame.init() 

#initialisation de la police
police = pygame.font.SysFont('comic', 35)

#definition de la taille de l'ecran souhaité
largeur_ecran = 800
hauteur_ecran = 600

#creation de la fenetre du jeu
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Jeu du pendu")

#chargement image du pendu 
images = [
    pygame.image.load('images\\pendu00.png'),
    pygame.image.load('images\\pendu11.png'),
    pygame.image.load('images\\pendu22.png'),
    pygame.image.load('images\\pendu33.png'),
    pygame.image.load('images\\pendu44.png'),
    pygame.image.load('images\\pendu55.png'),
    pygame.image.load('images\\pendu66.png'),
    pygame.image.load('images\\pendu77.png'),
    pygame.image.load('images\\pendu88.png'),
]

# Charger les mots depuis le fichier mots.txt
with open('mots.txt', 'r', encoding='utf-8') as fichier:
    mots = fichier.readlines()

# Initialiser les variables pour les options du menu
menu_options = ["Jouer", "Insérer un mot", "Tableau des scores", "Quitter"] # Les options du menu principal sous forme de liste
current_option = 0 # L'option actuellement sélectionnée
bg = pygame.image.load('bg-menu\\tableaubg2.jpeg') # Charger l'image de fond du menu

def afficher_menu():
    ecran.blit(bg, (0, 0)) #permet d'afficher l'ecran avec background
    
    # Afficher le titre du jeu
    titre_font = pygame.font.Font(None, 50) #police du titre
    titre_text = titre_font.render("Jeu du Pendu !", True, (249, 244, 244)) #couleur du titre et son emplacement sur l'ecran 
    ecran.blit(titre_text, (230, 20)) #affichage du titre sur l'ecran   

    # Afficher les options du menu principal 
    option_font = pygame.font.Font(None, 30) #police des options du menu 
    for i, option in enumerate(menu_options): # boucle qui parcourt chaque élément de la liste menu_options en attribuant à i l'indice de l'élément et à option la valeur de l'élément lui-même.
        texte = option_font.render(option, True, (249, 244, 244))  # Rendu du texte de l'option du menu avec la police et la taille spécifiées, avec une couleur de texte blanc cassé (249, 244, 244), prêt à être affiché à l'écran.
        text_rect = texte.get_rect(center=(300, 285 + i * 70)) # Récupérer le rectangle qui entoure le texte et le centrer horizontalement sur l'écran et verticalement en fonction de l'indice de l'option.
        position_y = 250 + i * 70 # Définir la position verticale du rectangle de l'option en fonction de l'indice de l'option.
        pygame.draw.ellipse(ecran, (150, 150, 150), pygame.Rect(180, position_y, 240, 60), 4) # Dessiner un rectangle autour de l'option avec une couleur de remplissage gris clair (150, 150, 150) et une épaisseur de ligne de 4 pixels. 
        ecran.blit(texte, text_rect, ) # Afficher le texte de l'option à l'écran en utilisant le rectangle de texte récupéré précédemment.

    current_option_rect = pygame.Rect(180, 250 + current_option * 70, 240, 60) # Récupérer le rectangle de l'option actuellement sélectionnée.
    pygame.draw.ellipse(ecran, (249, 244, 244), current_option_rect, 4) # Dessiner un rectangle autour de l'option actuellement sélectionnée avec une couleur de remplissage blanc cassé (249, 244, 244) et une épaisseur de ligne de 4 pixels.

# fonction qui permet de saisir un mot et de l'ajouter au fichier mots.txt 
def input_box(ecran, prompt): # prompt est le message qui s'affiche pour demander à l'utilisateur de saisir un mot
    pygame.font.init() # initialisation de la police 
    font = pygame.font.Font(None, 36) # police et taille de la police 
    bgJeu = pygame.image.load('bg-game\\fond-tableau.jpg') # chargement de l'image de fond du jeu
    input_box = pygame.Rect(300, 250, 180, 40) # rectangle qui entoure la zone de saisie du mot
    color_inactive = pygame.Color('grey') # couleur du rectangle quand il n'est pas sélectionné 
    color_active = pygame.Color('white') # couleur du rectangle quand il est sélectionné
    color = color_inactive # couleur du rectangle par défaut
    active = False # variable qui permet de savoir si le rectangle est sélectionné ou non
    text = '' # variable qui contient le mot saisi par l'utilisateur
    titre = prompt  # titre qui s'affiche au dessus de la zone de saisie du mot
    clock = pygame.time.Clock() # variable qui permet de gérer le temps

# boucle qui permet de gérer les événements (clavier, souris, ...)
    while True: # boucle infinie
        for event in pygame.event.get(): # boucle qui parcourt tous les événements qui se sont produits depuis le dernier appel de la fonction pygame.event.get()
            if event.type == pygame.QUIT: # si l'utilisateur clique sur la croix de la fenêtre
                pygame.quit() # fermeture de la fenêtre
            if event.type == pygame.MOUSEBUTTONDOWN: # si l'utilisateur clique sur la souris  
                if input_box.collidepoint(event.pos): # si la position de la souris est dans le rectangle input_box
                    active = not active # active prend la valeur inverse de active
                else: 
                    active = False # active prend la valeur False
                color = color_active if active else color_inactive # si active est True, color prend la valeur color_active sinon elle prend la valeur color_inactive
            if event.type == pygame.KEYDOWN: # si l'utilisateur appuie sur une touche du clavier 
                if active: # si active est True
                    if event.key == pygame.K_RETURN: # si l'utilisateur appuie sur la touche entrée
                        return text # la fonction retourne le mot saisi par l'utilisateur
                    elif event.key == pygame.K_BACKSPACE:   # si l'utilisateur appuie sur la touche backspace
                        text = text[:-1] # on supprime le dernier caractère du mot saisi
                    else:
                        text += event.unicode # on ajoute le caractère saisi au mot saisi par l'utilisateur    

        ecran.blit(bgJeu, (0, 0))  # affichage de l'image de fond du jeu
        txt_surface = font.render(text, True, color) # rendu du texte saisi par l'utilisateur avec la police, la taille et la couleur spécifiées
        width = max(200, txt_surface.get_width() + 10) # largeur du rectangle qui entoure le texte saisi par l'utilisateur
        input_box.w = width # largeur du rectangle qui entoure le texte saisi par l'utilisateur
        txt_titre = font.render(titre, True, color) # rendu du titre avec la police, la taille et la couleur spécifiées
        ecran.blit(txt_titre, (300, 200)) # affichage du titre au dessus de la zone de saisie du mot   
        ecran.blit(txt_surface, (input_box.x + 5, input_box.y + 5)) # affichage du texte saisi par l'utilisateur dans la zone de saisie du mot 
        pygame.draw.rect(ecran, color, input_box, 3) # affichage du rectangle qui entoure la zone de saisie du mot avec une épaisseur de ligne de 3 pixels
        pygame.display.flip() # mise à jour de l'affichage de la fenêtre 
        clock.tick(30) # limite le nombre de frames par seconde à 30    

# fonction qui permet de choisir la difficulté du jeu 
def menu_niveau_difficulte():
    global current_option # permet de modifier la variable current_option qui est définie en dehors de la fonction
    difficultes = ["Facile", "Difficile"] # difficultés du jeu 
    while True: 
        for event in pygame.event.get(): # boucle qui parcourt tous les événements qui se sont produits depuis le dernier appel de la fonction pygame.event.get()
            if event.type == pygame.QUIT: # si l'utilisateur clique sur la croix de la fenêtre
                pygame.quit() # fermeture de la fenêtre
                
            elif event.type == KEYDOWN: # si l'utilisateur appuie sur une touche du clavier
                if event.key == K_DOWN: # si l'utilisateur appuie sur la touche flèche du bas
                    current_option = (current_option + 1) % len(difficultes) # current_option prend la valeur de l'indice de l'élément suivant dans la liste difficultes
                elif event.key == K_UP: # si l'utilisateur appuie sur la touche flèche du haut
                    current_option = (current_option - 1) % len(difficultes) # current_option prend la valeur de l'indice de l'élément précédent dans la liste difficultes
                elif event.key == K_RETURN: # si l'utilisateur appuie sur la touche entrée 
                    return difficultes[current_option]  # la fonction retourne la difficulté choisie par l'utilisateur 

        ecran.blit(bg, (0, 0)) 
        titre_font = pygame.font.Font(None, 40)
        titre_text = titre_font.render("Choisissez la difficulté :", True, (249, 244, 244)) 
        ecran.blit(titre_text, (190, 20))

        option_font = pygame.font.Font(None, 36)
        for i, difficulte in enumerate(difficultes): # boucle qui parcourt chaque élément de la liste difficultes en attribuant à i l'indice de l'élément et à difficulte la valeur de l'élément lui-même. 
            texte = option_font.render(difficulte, True, (249, 244, 244)) # Rendu du texte de la difficulté avec la police et la taille spécifiées, avec une couleur de texte blanc cassé (249, 244, 244), prêt à être affiché à l'écran.
            text_rect = texte.get_rect(center=(400, 285 + i * 73)) # Récupérer le rectangle qui entoure le texte et le centrer horizontalement sur l'écran et verticalement en fonction de l'indice de la difficulté.
            position_y = 250 + i * 80
            pygame.draw.ellipse(ecran, (150, 150, 150), pygame.Rect(280, position_y, 240, 60), 4) # Dessiner un rectangle autour de la difficulté avec une couleur de remplissage gris clair (150, 150, 150) et une épaisseur de ligne de 4 pixels.
            ecran.blit(texte, text_rect, ) # Afficher le texte de la difficulté à l'écran en utilisant le rectangle de texte récupéré précédemment.

        current_option_rect = pygame.Rect(280, 250 + current_option * 80, 240, 60) # Récupérer le rectangle de la difficulté actuellement sélectionnée.
        pygame.draw.ellipse(ecran, (249, 244, 244), current_option_rect, 4) # Dessiner un rectangle autour de la difficulté actuellement sélectionnée avec une couleur de remplissage blanc cassé (249, 244, 244) et une épaisseur de ligne de 4 pixels.

        pygame.display.update() # mise à jour de l'affichage de la fenêtre

# fonction qui permet de jouer au jeu du pendu
def jouer(difficulte): 
    if difficulte == "Facile": # si la difficulté choisie est facile
        tentatives = 8 # le nombre de tentatives est égal à 9 si diffuculté est facile
    elif difficulte == "Difficile": 
        tentatives = 6
        

    solution = random.choice(mots).strip().lower() # choix aléatoire d'un mot dans la liste mots et suppression des espaces et des retours à la ligne
    lettres_trouvees = set() # initialisation de la variable lettres_trouvees qui contient les lettres trouvées par l'utilisateur 
    current_image_index = 0 # initialisation de la variable current_image_index qui contient l'indice de l'image du pendu à afficher
    current_image = images[current_image_index] # initialisation de la variable current_image qui contient l'image du pendu à afficher
    
    # Déterminer l'indice de début des images en fonction du niveau de difficulté
    if difficulte == "Facile":
        debut_images = 0
    elif difficulte == "Difficile":
        debut_images =  2 # indice de début des images du pendu en fonction du niveau de difficulté 


    running = True # variable qui permet de savoir si le jeu est en cours ou non
    clock = pygame.time.Clock() # variable qui permet de gérer le temps
    bgJeu = pygame.image.load('bg-game/fond-tableau.jpg')   # chargement de l'image de fond du jeu
    resultat_text = "" # initialisation de la variable resultat_text qui contient le résultat de la partie (gagné ou perdu)
    score = 0 # initialisation du score à 0
    debut_images = 2 # indice de début des images du pendu en fonction du niveau de difficulté
    pygame.time.delay(1000) # pause de 1 seconde avant de commencer le jeu

    nom_joueur = input_box(ecran,'entrez votre nom :') # saisie du nom du joueur

    # boucle qui permet de gérer les événements 
    while running and tentatives > 0: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN: # si l'utilisateur appuie sur une touche du clavier 
                if event.unicode.isalpha(): # si le caractère saisi est une lettre de l'alphabet 
                    proposition = event.unicode.lower() # la proposition prend la valeur de la lettre saisie par l'utilisateur en minuscule

                    if proposition in solution: # si la lettre saisie par l'utilisateur est dans le mot à deviner
                        lettres_trouvees.add(proposition) # on ajoute la lettre saisie par l'utilisateur à la liste lettres_trouvees
                    else:
                        tentatives -= 1 # on décrémente le nombre de tentatives restantes
                        current_image_index = (current_image_index + 1) % len(images) # on incrémente l'indice de l'image du pendu à afficher
                        current_image = images[current_image_index] # on change l'image du pendu à afficher
                        
                        if difficulte == "Difficile": 
                            current_image = images[current_image_index + debut_images]
                    
        ecran.blit(bgJeu, (0, 0))
        ecran.blit(current_image, (100, 100))

        # Afficher les lettres trouvées
        affichage = "" # initialisation de la variable affichage qui contient les lettres trouvées par l'utilisateur
        for lettre in solution: # boucle qui parcourt chaque lettre du mot à deviner
            if lettre in lettres_trouvees: # si la lettre est dans la liste lettres_trouvees
                affichage += lettre # on ajoute la lettre à la variable affichage
            else:
                affichage += " _ " # sinon on ajoute un espace à la variable affichage

        text1 = police.render(affichage, True, (249, 244, 244))
        text2 = police.render("Mot à deviner :", True, (249, 244, 244))
        text3 = police.render("Il vous reste {} tentatives".format(tentatives), True, (249, 244, 244)) # affichage du nombre de tentatives restantes

        ecran.blit(text1, (100, 400))
        ecran.blit(text2, (300, 10))
        ecran.blit(text3, (25, 500))

        pygame.display.update()
        clock.tick(30)

        if "_" not in affichage: # si l'utilisateur a trouvé toutes les lettres du mot à deviner 
            resultat_text = "Gagné!"
            break

    if tentatives == 0: # si le nombre de tentatives est égal à 0
        resultat_text = "Perdu!"

    resultat_couleur = (255, 0, 0) if tentatives == 0 else (0, 255, 0)
    resultat_surface = police.render(resultat_text, True, resultat_couleur)
    ecran.blit(resultat_surface, (350, 250))

    quitter = False # variable qui permet de savoir si l'utilisateur veut quitter le jeu ou non
    while not quitter: 
        for event in pygame.event.get(): # boucle qui parcourt tous les événements qui se sont produits depuis le dernier appel de la fonction pygame.event.get()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: # si l'utilisateur appuie sur la touche entrée
                quitter = True # quitter prend la valeur True

        pygame.display.update()
    

    mettre_a_jour_score(nom_joueur, tentatives) 
    
    
# fonction qui permet de mettre à jour le score du joueur dans le fichier scores.txt
def mettre_a_jour_score(nom_joueur, score):
    with open('scores.txt', 'a', encoding='utf-8') as fichier: # ouverture du fichier scores.txt en mode ajout
        fichier.write(f"{nom_joueur}: {score}\n") # ajout du nom du joueur et de son score à la fin du fichier scores.txt suivi d'un retour à la ligne

# fonction qui permet d'afficher le tableau des scores 
def afficher_scores():
    ecran.blit(bg, (0, 0))
    titre_font = pygame.font.Font(None, 50)
    titre_text = titre_font.render("Tableau des scores", True, (249, 244, 244))
    ecran.blit(titre_text, (200, 20))

    score_font = pygame.font.Font(None, 36)
    scores = []
    # Charger les scores depuis le fichier scores.txt 
    try:
        with open('scores.txt', 'r', encoding='utf-8') as fichier:
            scores = fichier.readlines()  # lire toutes les lignes du fichier scores.txt et les stocker dans la liste scores
    except FileNotFoundError: # si le fichier scores.txt n'existe pas
        pass # on ne fait rien

    for i, score in enumerate(scores): # boucle qui parcourt chaque élément de la liste scores en attribuant à i l'indice de l'élément et à score la valeur de l'élément lui-même.
        texte = score_font.render(score.strip(), True, (249, 244, 244)) # Rendu du texte du score avec la police et la taille spécifiées, avec une couleur de texte blanc cassé (249, 244, 244), prêt à être affiché à l'écran.
        position_y = 100 + i * 30 # Définir la position verticale du texte du score en fonction de l'indice du score. 
        ecran.blit(texte, (300, position_y)) # Afficher le texte du score à l'écran en utilisant le rectangle de texte récupéré précédemment.

    
    pygame.display.update()

    quitter = False # variable qui permet de savoir si l'utilisateur veut quitter le jeu ou non   
    while not quitter: 
        for event in pygame.event.get(): # boucle qui parcourt tous les événements qui se sont produits depuis le dernier appel de la fonction pygame.event.get()
            if event.type == pygame.KEYDOWN: # si l'utilisateur appuie sur une touche du clavier
                if event.key == pygame.K_RETURN: # si l'utilisateur appuie sur la touche entrée
                    quitter = True # quitter prend la valeur True

    afficher_menu()
    
# fonction qui permet de réinitialiser les variables du jeu 
def reinitialiser_jeu():
    global solution, lettres_trouvees, tentatives, current_image_index, current_image # permet de modifier les variables qui sont définies en dehors de la fonction
    solution = "" # initialisation de la variable solution qui contient le mot à deviner
    lettres_trouvees = set() # initialisation de la variable lettres_trouvees qui contient les lettres trouvées par l'utilisateur
    tentatives = 9 # initialisation de la variable tentatives qui contient le nombre de tentatives restantes
    current_image_index = 0 # initialisation de la variable current_image_index qui contient l'indice de l'image du pendu à afficher
    current_image = images[current_image_index] # initialisation de la variable current_image qui contient l'image du pendu à afficher

# boucle qui permet de gérer les événements 
menu_actif = True
while menu_actif: #
    for event in pygame.event.get(): # boucle qui parcourt tous les événements qui se sont produits depuis le dernier appel de la fonction pygame.event.get()
        if event.type == pygame.QUIT: # si l'utilisateur clique sur la croix de la fenêtre
            menu_actif = False # menu_actif prend la valeur False
        elif event.type == KEYDOWN: # si l'utilisateur appuie sur une touche du clavier
            if event.key == K_DOWN: # si l'utilisateur appuie sur la touche flèche du bas
                current_option = (current_option + 1) % len(menu_options) # current_option prend la valeur de l'indice de l'élément suivant dans la liste menu_options
            elif event.key == K_UP: # si l'utilisateur appuie sur la touche flèche du haut
                current_option = (current_option - 1) % len(menu_options) # current_option prend la valeur de l'indice de l'élément précédent dans la liste menu_options
            elif event.key == K_RETURN: # si l'utilisateur appuie sur la touche entrée
                if menu_options[current_option] == "Jouer":     # si l'utilisateur choisit l'option "Jouer"
                        difficulte = menu_niveau_difficulte() # choix de la difficulté du jeu
                        jouer(difficulte) # lancement du jeu
                        reinitialiser_jeu() # réinitialisation des variables du jeu
                        afficher_menu() # affichage du menu
                elif menu_options[current_option] == "Insérer un mot": # si l'utilisateur choisit l'option "Insérer un mot"
                    nouveauMot = input_box(ecran, 'Entrez un nouveau mot : ') # saisie du nouveau mot à ajouter au fichier mots.txt
                    with open('mots.txt', 'a', encoding='utf8') as fichier: # ouverture du fichier mots.txt en mode ajout
                        fichier.write(nouveauMot + '\n') # ajout du nouveau mot à la fin du fichier mots.txt suivi d'un retour à la ligne
                    afficher_menu()
                elif menu_options[current_option] == "Tableau des scores":
                    afficher_scores()
                elif menu_options[current_option] == "Quitter":
                    menu_actif = False

    afficher_menu()
    pygame.display.update()
pygame.quit()