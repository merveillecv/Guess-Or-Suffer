# code compler GUESS OR SUFFER


import sys
from random import*
from pygame import* 

init()
mixer.pre_init(44100, -16, 2, 512)
mixer.init()
mixer.music.load("fonds/musiquefond.ogg")
mixer.music.set_volume(0.4)
mixer.music.play(-1)

# les variables  jeu
niveau = 0
chances = 7
l = 1408
h = 768
continuer = True 
menu_parametre = False
quitter = False 
nombre_secret = randint(1, 100)
saisie =""
proposition = 0
partie_perdue = False
partie_gagnée = False
liste = [x for x in range(1,101)]
replique_actuelle = ""
index_replique = 0

fenetre = display.set_mode((l, h))
display.set_caption("Guess or Suffer")
clock = time.Clock()

#police
texte = font.SysFont("Impact", 48)
texte_start = texte.render("CLICK TO START", True, (217, 1, 21))
texte_parametre = texte.render("PARAMETRES", True, (217, 1, 21))
texte_parametre_w, texte_parametre_h = texte_parametre.get_size()
texte_w, texte_h = texte_start.get_size()
texte1 = font.SysFont("Arial", 30)
texte_quit1 = texte1.render("Vous etes sur(e) de vouloir quitter ?", True, ((217, 1, 21)))
texte_quit2  = texte1.render("Si oui appuyez sur la touche Q ", True, (217, 1, 21))
texte_noquit = texte1.render("Si non, cliquez sur le bouton parametres", True, (217, 1, 21))
police_saisie = font.SysFont("Impact", 60)
texte_enter = police_saisie.render("ENTREZ VOTRE PROPOSITION", True, (217, 1, 21))
texteraté = police_saisie.render("RATÉ !", True, (217, 1, 21))
texteniveausup = police_saisie.render("On passe à un niveau supérieur !", True, (217, 1, 21))
textebigger = texte1.render("T'es nul ! Le nombre est plus grand !", True, (217, 1, 21))
textesmaller= texte1.render("T'es nul ! Le nombre est plus petit !", True, (217, 1, 21))
texteliste = texte1.render("Le nombre à deviner se trouve dans cette liste:", True, (217, 1, 21))

# les répliques 

# réplique du prof
repliques_prof = ["Oh non pas lui...",
    "Ton père se demande pourquoi on t'a mis à l'école...",
    "Une erreur pareille à ton age ? C'est inadmissible.",
    "Pas les cours avec toi... Pitié, trouve ce nombre !",
    "Si tu rates encore, c'est une heure de colle direct.",
    "Je prépare déjà la fiche de suivi pour tes parents...",
    "Bravo... place auxcours de rattrapage tout l'été."]

# réplique de la soeur
repliques_soeur = repliques_soeur = ["Je suis sûre que tu ne vas pas y arriver.",
    "Je l'ai fait du premier coup moi !",
    "Dépêche j'ai pas que ça à faire !",
    "c'est le jeu ou c'est ton cerveau qui est lent?",
    "Regarde-toi galérer, c'est trop la honte.",
    "Abandonne et encaisse ton zéro tu fais pitié.",
    "Loser ! Allez pousse-toi de là maintenant."]

# réplique du père
repliques_pere = ["Concentration. Tu manques cruellement de rigueur.",
    "Tu réfléchis avant de taper ou tu laisses faire le hasard ?",
    "Ce n'est pourtant pas sorcier, applique-toi.",
    "À ton âge, je savais faire ça de tête.",
    "L'erreur est humaine, mais là ça devient une habitude.",
    "Dernière chance. Ne me déçois pas plus que ça.",
    "C'est un échec. Tu iras expliquer ça à ton professeur."]

# réplique du grand père
repliques_grandpere = ["Miskine. Meme ton grand-père s'y met !",
    "Perdu ! Allez, viens m'aider au jardin, ça te fera les pieds.",
    "Tu t'es trompé ? Recommence et redresse-toi.",
    "Sacredie, tes yeux fatiguent ou quoi ?",
    "Si tu rates ce coup-là, pas de dessert ce soir.",
    "Je pense que je peux régler ça à coup de bâton !",
    "Une fessée et tu trouveras le bon chiffre tout de suite.",]

# design

fondpendant = image.load("fonds/fond.png").convert()
fondpendant = transform.scale(fondpendant, (l, h))

fonddebut = image.load("fonds/presentation.png").convert()
fonddebut = transform.scale(fonddebut, (l, h))
fenetregameover = image.load("fonds/gameover.jpg").convert()
fenetregameover = transform.scale(fenetregameover, (l, h))
fenetrewin = image.load("fonds/win.jpg").convert()
fenetrewin = transform.scale(fenetrewin, (l, h))

fenetrefinale = image.load("fonds/finalwin.jpg").convert()
fenetrefinale = transform.scale(fenetrefinale, (l, h))
buttonparametre = image.load("fonds/parametre.png").convert_alpha()
buttonparametre_w, buttonparametre_h = buttonparametre.get_size()
bulle = image.load("fonds/bulle.png").convert_alpha()
bulle = transform.scale(bulle, (650, 110))





# les pnj

prof = [image.load("pnj/prof/prof1.png").convert_alpha(), image.load("pnj/prof/prof2.png").convert_alpha(), image.load("pnj/prof/prof3.png").convert_alpha(), image.load("pnj/prof/prof4.png").convert_alpha()]  
pere = [image.load("pnj/pere/pere1.png").convert_alpha(), image.load("pnj/pere/pere2.png").convert_alpha(), image.load("pnj/pere/pere3.png").convert_alpha(), image.load("pnj/pere/pere4.png").convert_alpha()]  
soeur = [image.load("pnj/soeur/soeur1.png").convert_alpha(), image.load("pnj/soeur/soeur2.png").convert_alpha(), image.load("pnj/soeur/soeur3.png").convert_alpha(), image.load("pnj/soeur/soeur4.png").convert_alpha()] 
grandpere = [image.load("pnj/grandpere/grandpere1.png").convert_alpha(), image.load("pnj/grandpere/grandpere2.png").convert_alpha(), image.load("pnj/grandpere/grandpere3.png").convert_alpha(), image.load("pnj/grandpere/grandpere4.png").convert_alpha()] 
prof = [transform.scale_by(img, 2.5) for img in prof]
pere = [transform.scale_by(img, 2.5) for img in pere]
soeur = [transform.scale_by(img, 2.5) for img in soeur]
grandpere = [transform.scale_by(img, 2.5) for img in grandpere]



# la boucle du jeu
while continuer:
    

    

    for event_item in event.get():

        # pour quitter le jeu
        if event_item.type == QUIT or quitter == True:
            continuer = False
        
        # pour que les clics commencent le jeu et ouvrent le menu parametre
        if event_item.type == MOUSEBUTTONDOWN:
            if event_item.button == 1:
                mouse_x, mouse_y = event_item.pos
                if (l - buttonparametre_w - 50 <= mouse_x <= l - 50 and h - buttonparametre_h - 50 <= mouse_y <= h - 50):
                    menu_parametre = not menu_parametre 
                
               
                elif niveau == 0 and menu_parametre == False:
                     niveau = 1
                     nombre_secret = randint(1,100)
                     replique_actuelle = repliques_prof[0] 
                     nombre_secret = randint(1, 100)
                    
        # pour toutes les interactions avec clavier       
        elif event_item.type == KEYDOWN:


            # pour quitter le jeu depuis le menu parametre ou après avoir gagné
            if event_item.key == K_q and menu_parametre == True:
                quitter = True
            elif niveau == 4 and partie_gagnée and event_item.key == K_q:
                    quitter = True


            # la gestion des interactions clavier pendant le jeu    
            elif menu_parametre == False:

                # si on perd
                if partie_perdue and event_item.key == K_SPACE:
                    proposition = 0
                    chances = 7
                    saisie = ""
                    nombre_secret = randint(1, 100)
                    partie_perdue = False
                    liste = [x for x in range(1,101)]
                    if niveau == 1: 
                         replique_actuelle = repliques_prof[0]
                    elif niveau == 2: 
                         replique_actuelle = repliques_soeur[0]
                    elif niveau == 3: 
                         replique_actuelle = repliques_pere[0]
                    elif niveau == 4: 
                         replique_actuelle = repliques_grandpere[0]
                    


                # si on gagne
                elif partie_gagnée and event_item.key == K_RETURN:
                        if niveau < 4:
                            niveau += 1  # passe au niveau suivant
                            
                        else :
                             niveau = 0  # on revient au niveau 0 après avoir gagné le niveau 4

                        chances = 7  # remet les chances à 7
                        partie_gagnée = False  # réinitialise la variable de victoire
                        saisie = ""
                        proposition = 0
                        liste = [x for x in range(1, 101)]  
                        nombre_secret = randint(1, 100) 
                        if niveau == 1: 
                            replique_actuelle = repliques_prof[0]
                        elif niveau == 2:
                            replique_actuelle = repliques_soeur[0]
                        elif niveau == 3: 
                            replique_actuelle = repliques_pere[0]
                        elif niveau == 4: 
                            replique_actuelle = repliques_grandpere[0]
         
         

                # pour entrer les nombres et valider la proposition
                elif event_item.key == K_RETURN and not partie_perdue and not partie_gagnée:

                    if saisie != "":
                        proposition = int(saisie)
                        
                        if proposition == nombre_secret:
                            partie_gagnée = True
                            saisie = ""
                        else:
                            chances -= 1       
                            saisie = "" 
                            if chances > 0:
                                index_replique = 7 - chances
                            else:
                                index_replique = 6
                            
                            
                            # pour faire défiler les répliques à chaque erreur
                            if niveau == 1:
                                replique_actuelle = repliques_prof[index_replique]
                            elif niveau == 2:
                                replique_actuelle = repliques_soeur[index_replique]
                            elif niveau == 3:
                                replique_actuelle = repliques_pere[index_replique]
                            elif niveau == 4:
                                replique_actuelle = repliques_grandpere[index_replique]
                            
                            if nombre_secret > proposition :
                                toremove =[x for x in range(1,101) if proposition >= x ]
                            else :
                                toremove =[x for x in range(1,101) if proposition    <= x ]        
                            liste = [x for x in liste if x not in toremove]  # pour nettoyer la liste pour aider le joueur
                            if chances == 0:
                                 partie_perdue = True 
            

                  
                
                elif event_item.key == K_BACKSPACE:  # pour effacer un chiffre
                        saisie = saisie[:-1]

                
                    
                elif not partie_perdue and not partie_gagnée:           
                    if event_item.unicode.isdigit():
                        if len(saisie) < 3:
                            #  chiffre dépasse pas 100
                            test_saisie = saisie + event_item.unicode
                            if int(test_saisie) <= 100:
                                saisie += event_item.unicode
                
                
    
    if niveau == 0:
        fenetre.blit(fonddebut, (0, 0)) 
        fenetre.blit(texte_start, (l // 2 - texte_w // 2, h // 3.5 - texte_h // 2))
        fenetre.blit(buttonparametre, (l - buttonparametre_w - 50, h - buttonparametre_h - 50))
             
    elif niveau == 1:
        if not partie_perdue and not partie_gagnée:
            fenetre.blit(fondpendant, (0, 0))
            fenetre.blit(buttonparametre, (l - buttonparametre_w - 50, h - buttonparametre_h - 50))
            if chances >= 6:      
                 fenetre.blit(prof[0], (prof[0].get_width() // 4 -20, h - prof[0].get_height()))
            elif chances == 4 or chances ==5:
                   fenetre.blit(prof[0], (prof[0].get_width() // 4 -20, h - prof[0].get_height()))
            elif chances == 3:
                 fenetre.blit(prof[1], (prof[1].get_width() // 4 -20, h - prof[1].get_height()))
            elif chances == 2:
                fenetre.blit(prof[2], (prof[2].get_width() // 4 -20, h - prof[2].get_height()))
            elif chances == 1:
                 fenetre.blit(prof[3], (prof[3].get_width() // 4 -20, h - prof[3].get_height()))
        
            fenetre.blit(texte_enter, (l // 2 - texte_enter.get_width() // 2, h // 4))
            image_chiffres = police_saisie.render(saisie, True, (255, 255, 255)) 
            fenetre.blit(image_chiffres, (l // 2 - image_chiffres.get_width() // 2, h // 4 + 70))
            texte_chances = texte.render("Chances: " + str(chances), True, (217, 1, 21))
            fenetre.blit(texte_chances, (texte_chances.get_width()//2, 30))

            if proposition != 0:
                fenetre.blit(texteraté,(l // 2 - texteraté.get_width() // 2, h // 4 + 160))
                if nombre_secret > proposition :
                    fenetre.blit(textebigger, (l // 2 - textebigger.get_width() // 2, h // 4 + 230))
                else :
                    fenetre.blit(textesmaller, (l // 2 - textesmaller.get_width() // 2, h // 4 + 230))
            fenetre.blit(texteliste, (l // 2 - texteliste.get_width() // 2, h // 4 + 290))
            if len(liste) > 7:
                    texte_resume_liste = f"[{liste[0]}, {liste[1]}, {liste[2]} ... {liste[-3]}, {liste[-2]}, {liste[-1]}]"
            else:
                texte_resume_liste = str(liste)
            listechiffres = texte1.render(texte_resume_liste, True, (217, 1, 21))
            fenetre.blit(listechiffres, (l // 2 - listechiffres.get_width() // 2, h // 4 + 340))


        elif partie_perdue:
            fenetre.blit(fenetregameover, (0, 0))
            fenetre.blit(buttonparametre, (l - buttonparametre_w - 50, h - buttonparametre_h - 50))
            partie_perdue = True
            texte_revelation = texte1.render("Le nombre secret était "+str(nombre_secret), True, (0, 0, 0))
            fenetre.blit(texte_revelation, (l // 2 - texte_revelation.get_width() // 2, h // 2 + 170))

        elif partie_gagnée:
            fenetre.blit(fenetrewin, (0, 0))
            fenetre.blit(buttonparametre, (l - buttonparametre_w - 50, h - buttonparametre_h - 50))
    elif niveau == 2:
            fenetre.blit(fondpendant, (0, 0))
            fenetre.blit(buttonparametre, (l - buttonparametre_w - 50, h - buttonparametre_h - 50))

            if chances >= 6:      
                 fenetre.blit(soeur[0], (soeur[0].get_width() // 4 -20, h - soeur[0].get_height()))
            elif chances == 4 or chances ==5:
                   fenetre.blit(soeur[0], (soeur[0].get_width() // 4 -20, h - soeur[0].get_height()))
            elif chances == 3:
                 fenetre.blit(soeur[1], (soeur[1].get_width() // 4 -20, h - soeur[1].get_height()))
            elif chances == 2:
                fenetre.blit(soeur[2], (soeur[2].get_width() // 4 -20, h - soeur[2].get_height()))
            elif chances == 1:
                 fenetre.blit(soeur[3], (soeur[3].get_width() // 4 -20, h - soeur[3].get_height()))
        
            fenetre.blit(texte_enter, (l // 2 - texte_enter.get_width() // 2, h // 4))
            image_chiffres = police_saisie.render(saisie, True, (255, 255, 255)) 
            fenetre.blit(image_chiffres, (l // 2 - image_chiffres.get_width() // 2, h // 4 + 70))
            texte_chances = texte.render("Chances: " + str(chances), True, (217, 1, 21))
            fenetre.blit(texte_chances, (texte_chances.get_width()//2, 30))

            if proposition != 0:
                fenetre.blit(texteraté,(l // 2 - texteraté.get_width() // 2, h // 4 + 160))
                if nombre_secret > proposition :
                    fenetre.blit(textebigger, (l // 2 - textebigger.get_width() // 2, h // 4 + 230))
                else :
                    fenetre.blit(textesmaller, (l // 2 - textesmaller.get_width() // 2, h // 4 + 230))
            fenetre.blit(texteliste, (l // 2 - texteliste.get_width() // 2, h // 4 + 290))
            if len(liste) > 7:
                    texte_resume_liste = f"[{liste[0]}, {liste[1]}, {liste[2]} ... {liste[-3]}, {liste[-2]}, {liste[-1]}]"
            else:
                texte_resume_liste = str(liste)
            listechiffres = texte1.render(texte_resume_liste, True, (217, 1, 21))
            fenetre.blit(listechiffres, (l // 2 - listechiffres.get_width() // 2, h // 4 + 340))


            if partie_perdue:
                fenetre.blit(fenetregameover, (0, 0))
                fenetre.blit(buttonparametre, (l - buttonparametre_w - 50, h - buttonparametre_h - 50))
                partie_perdue = True
                texte_revelation = texte1.render("Le nombre secret était "+str(nombre_secret), True, (0, 0, 0))
                fenetre.blit(texte_revelation, (l // 2 - texte_revelation.get_width() // 2, h // 2 + 170))

            elif partie_gagnée:
                fenetre.blit(fenetrewin, (0, 0))
                fenetre.blit(buttonparametre, (l - buttonparametre_w - 50, h - buttonparametre_h - 50))
    elif niveau == 3:
            fenetre.blit(fondpendant, (0, 0))
            fenetre.blit(buttonparametre, (l - buttonparametre_w - 50, h - buttonparametre_h - 50))

            if chances >= 6:      
                 fenetre.blit(pere[0], (pere[0].get_width() // 4 -20, h - pere[0].get_height()))
            elif chances == 4 or chances ==5:
                   fenetre.blit(pere[0], (pere[0].get_width() // 4 -20, h - pere[0].get_height()))
            elif chances == 3:
                 fenetre.blit(pere[1], (pere[1].get_width() // 4 -20, h - pere[1].get_height()))
            elif chances == 2:
                fenetre.blit(pere[2], (pere[2].get_width() // 4 -20, h - pere[2].get_height()))
            elif chances == 1:
                 fenetre.blit(pere[3], (pere[3].get_width() // 4 -20, h - pere[3].get_height()))
        
            fenetre.blit(texte_enter, (l // 2 - texte_enter.get_width() // 2, h // 4))
            image_chiffres = police_saisie.render(saisie, True, (255, 255, 255)) 
            fenetre.blit(image_chiffres, (l // 2 - image_chiffres.get_width() // 2, h // 4 + 70))
            texte_chances = texte.render("Chances: " + str(chances), True, (217, 1, 21))
            fenetre.blit(texte_chances, (texte_chances.get_width()//2, 30))

            if proposition != 0:
                fenetre.blit(texteraté,(l // 2 - texteraté.get_width() // 2, h // 4 + 160))
                if nombre_secret > proposition :
                    fenetre.blit(textebigger, (l // 2 - textebigger.get_width() // 2, h // 4 + 230))
                else :
                    fenetre.blit(textesmaller, (l // 2 - textesmaller.get_width() // 2, h // 4 + 230))
            fenetre.blit(texteliste, (l // 2 - texteliste.get_width() // 2, h // 4 + 290))
            if len(liste) > 7:
                    texte_resume_liste = f"[{liste[0]}, {liste[1]}, {liste[2]} ... {liste[-3]}, {liste[-2]}, {liste[-1]}]"
            else:
                texte_resume_liste = str(liste)
            listechiffres = texte1.render(texte_resume_liste, True, (217, 1, 21))
            fenetre.blit(listechiffres, (l // 2 - listechiffres.get_width() // 2, h // 4 + 340))
            if partie_perdue:
                fenetre.blit(fenetregameover, (0, 0))
                fenetre.blit(buttonparametre, (l - buttonparametre_w - 50, h - buttonparametre_h - 50))
                partie_perdue = True
                texte_revelation = texte1.render("Le nombre secret était "+str(nombre_secret), True, (0, 0, 0))
                fenetre.blit(texte_revelation, (l // 2 - texte_revelation.get_width() // 2, h // 2 + 170))

            elif partie_gagnée:
                fenetre.blit(fenetrewin, (0, 0))
                fenetre.blit(buttonparametre, (l - buttonparametre_w - 50, h - buttonparametre_h - 50))
    elif niveau == 4:
            fenetre.blit(fondpendant, (0, 0))
            fenetre.blit(buttonparametre, (l - buttonparametre_w - 50, h - buttonparametre_h - 50))

            if chances >= 6:      
                 fenetre.blit(grandpere[0], (grandpere[0].get_width() // 4 -20, h - grandpere[0].get_height()))
            elif chances == 4 or chances ==5:
                   fenetre.blit(grandpere[0], (grandpere[0].get_width() // 4 -20, h - grandpere[0].get_height()))
            elif chances == 3:
                 fenetre.blit(grandpere[1], (grandpere[1].get_width() // 4 -20, h - grandpere[1].get_height()))
            elif chances == 2:
                fenetre.blit(grandpere[2], (grandpere[2].get_width() // 4 -20, h - grandpere[2].get_height()))
            elif chances == 1:
                 fenetre.blit(grandpere[3], (grandpere[3].get_width() // 4 -20, h - grandpere[3].get_height()))
        
            fenetre.blit(texte_enter, (l // 2 - texte_enter.get_width() // 2, h // 4))
            image_chiffres = police_saisie.render(saisie, True, (255, 255, 255)) 
            fenetre.blit(image_chiffres, (l // 2 - image_chiffres.get_width() // 2, h // 4 + 70))
            texte_chances = texte.render("Chances: " + str(chances), True, (217, 1, 21))
            fenetre.blit(texte_chances, (texte_chances.get_width()//2, 30))

            if proposition != 0:
                fenetre.blit(texteraté,(l // 2 - texteraté.get_width() // 2, h // 4 + 160))
                if nombre_secret > proposition :
                    fenetre.blit(textebigger, (l // 2 - textebigger.get_width() // 2, h // 4 + 230))
                else :
                    fenetre.blit(textesmaller, (l // 2 - textesmaller.get_width() // 2, h // 4 + 230))
            fenetre.blit(texteliste, (l // 2 - texteliste.get_width() // 2, h // 4 + 290))
            if len(liste) > 7:
                    texte_resume_liste = f"[{liste[0]}, {liste[1]}, {liste[2]} ... {liste[-3]}, {liste[-2]}, {liste[-1]}]"
            else:
                texte_resume_liste = str(liste)
            listechiffres = texte1.render(texte_resume_liste, True, (217, 1, 21))
            fenetre.blit(listechiffres, (l // 2 - listechiffres.get_width() // 2, h // 4 + 340))


            if partie_perdue:
                fenetre.blit(fenetregameover, (0, 0))
                fenetre.blit(buttonparametre, (l - buttonparametre_w - 50, h - buttonparametre_h - 50))
                partie_perdue = True
                texte_revelation = texte1.render("Le nombre secret était "+str(nombre_secret), True, (0, 0, 0))
                fenetre.blit(texte_revelation, (l // 2 - texte_revelation.get_width() // 2, h // 2 + 170))

            elif partie_gagnée:
                fenetre.blit(fondpendant, (0, 0))
                fenetre.blit(fenetrefinale, (0, 0))
                fenetre.blit(buttonparametre, (l - buttonparametre_w - 50, h - buttonparametre_h - 50))

    if niveau != 0 and not partie_perdue and not partie_gagnée:
        fenetre.blit(bulle, (l // 2 - 650 // 2, h - 150))
        texte_pnj_rendu = texte1.render(replique_actuelle, True, (0, 0, 0))
        fenetre.blit(texte_pnj_rendu, (l // 2 - texte_pnj_rendu.get_width() // 2 - 10, h - 150 + 20))

    if menu_parametre:
        draw.rect(fenetre, (61, 61, 61), (l // 4, h // 3, l // 2, h // 2.5))
        fenetre.blit(texte_parametre, (l // 4 + 20, h // 3 + 20))
        fenetre.blit(texte_quit1, (l // 4 + 20, h // 3 + 120))
        fenetre.blit(texte_quit2, (l // 4 + 20, h // 3 + 170))
        fenetre.blit(texte_noquit, (l // 4 + 20, h // 3 + 220))

    display.flip()
    clock.tick(60)

quit()
sys.exit()