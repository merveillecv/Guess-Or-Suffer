# voici l'algorithme de base du jeu

from random import*

def guess():
    liste = [x for x in range(1,101)]
    chances = 5
    number = randint(1,100)
    while chances>0:
        choix = int(input("Devine le nombre!"))
        if choix == number:
            print("You won !")
            break 
        if choix != number:
            print("Wrong!")
            chances -=1
            print("Il te reste",chances,'chances. Loser')
            if number > choix :
                print("T'es nul ! le nombre est supérieur ! ")
                toremove =[x for x in range(1,101) if choix >= x ]
            else : 
                print('Trop bete ! Le nombre est plus petit! Comme tu es inférieur par rapport à moi!')
                toremove =[x for x in range(1,101) if choix <= x ]          
            liste = [x for x in liste if x not in toremove]
            print("Le nombre à deviner se trouve dans cette liste:", liste)
            
    if chances == 0:
            print(" Tu as perdu ! Le nombre était", number)
       
            
