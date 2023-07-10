#Auteur : Paul MARESCHI
#Date : 10/07/2023
#Version : 1

#Description : Programme qui permet de jouer à la roulette avec une mise precise 

#But : Tester et voir le gain sur cette mise



#Importation des modules
import random
from time import sleep

def roulette():
    #Initialisation des variables
    gain = 0
    numero = 0
    perte = 0
    perte_gain = 0

    #Demande de l'argent de départ
    argent = int(input("Combien d'argent voulez vous mettre ? : "))

    #Demande du nombre de tour
    nombre_de_tour = int(input("Combien de tour voulez vous faire ? : "))

    #Demande de la mise
    mise = int(input("Combien voulez vous miser sur chaque colonne ? : "))

    #Demande du temps de sleep (DEV)
    temps_sleep = float(input("Combien de temps de sleep ? : "))
    #Création des colonnes
    colonne1 = [1,4,7,10,13,16,19,22,25,28,31,34]
    colonne2 = [2,5,8,11,14,17,20,23,26,29,32,35]
    colonne3 = [3,6,9,12,15,18,21,24,27,30,33,36]

    #Choix des colonnes
    choix_colonne = [1,2]

    #Boucle de jeu
    for i in range(nombre_de_tour):

        #Perte de la mise
        argent -= mise*2

        #Tirage du numéro
        numero = random.randint(0,36)

        #Verificattion si la colonne correspond au choix
        if numero in colonne1 and 1 in choix_colonne:
            gain += mise
            argent += mise*3
            perte_gain += mise*3

            #Affichage du tour
            affichage_resultat(i,numero,gain,perte,argent,perte_gain,choix_colonne)

            #Changement du choix de colonne
            choix_colonne = [2,3]

        elif numero in colonne2 and 2 in choix_colonne:
            gain += mise
            argent += mise*3
            perte_gain += mise*3

            #Affichage du tour
            affichage_resultat(i,numero,gain,perte,argent,perte_gain,choix_colonne)

            #Changement du choix de colonne
            choix_colonne = [1,3]

        elif numero in colonne3 and 3 in choix_colonne:
            gain += mise
            argent += mise*3
            perte_gain += mise*3

            #Affichage du tour
            affichage_resultat(i,numero,gain,perte,argent,perte_gain,choix_colonne)

            #Changement du choix de colonne
            choix_colonne = [1,2]

        else:
            perte += mise*2
            perte_gain -= mise

            #Affichage du tour
            affichage_resultat(i,numero,gain,perte,argent,perte_gain,choix_colonne)


        if argent <= 0:
            print("Vous n'avez plus d'argent")
            break

        sleep(temps_sleep)


def affichage_resultat(i,numero,gain,perte,argent,perte_gain,choix_colonne):
    #Affichage des résultats
        affichage(numero,choix_colonne)
        print("")
        print("")
        print("Tour : ",i+1)
        print("Tirage : ",numero)
        print("Gain : ",gain)
        print("Perte : ",perte)
        print("Argent : ",argent)
        print("Perte/gain : ",perte_gain)
        print("")
        print("")
        
        

        
def affichage(numero,choix_colonne):
    colonne1 = [1,4,7,10,13,16,19,22,25,28,31,34]
    colonne2 = [2,5,8,11,14,17,20,23,26,29,32,35]
    colonne3 = [3,6,9,12,15,18,21,24,27,30,33,36]
    
    for i in range(len(colonne1)):
            if 1 in choix_colonne and 2 in choix_colonne:
                if numero == colonne1[i]:
                    print("\033[1;34m",colonne1[i],"\033[1;32m",colonne2[i],"\033[0m",colonne3[i])
                elif numero == colonne2[i]:
                    print("\033[1;32m",colonne1[i],"\033[1;34m",colonne2[i],"\033[0m",colonne3[i])
                else :
                    if numero == colonne3[i] :
                        print("\033[1;32m",colonne1[i],colonne2[i],"\033[1;34m",colonne3[i],"\033[0m")
                    else :
                        print("\033[1;32m",colonne1[i],colonne2[i],"\033[0m",colonne3[i])


            elif 2 in choix_colonne and 3 in choix_colonne:
                if numero == colonne2[i]:
                    print(colonne1[i],"\033[1;34m",colonne2[i],"\033[1;32m",colonne3[i],"\033[0m")
                elif numero == colonne3[i] :
                    print(colonne1[i],"\033[1;32m",colonne2[i],"\033[1;34m",colonne3[i],"\033[0m")
                else :
                    if numero == colonne1[i] :
                        print("\033[1;34m",colonne1[i],"\033[1;32m",colonne2[i],colonne3[i],"\033[0m")
                    else :
                        print(colonne1[i],"\033[1;32m",colonne2[i],"\033[1;32m",colonne3[i],"\033[0m")

            else :
                if numero == colonne1[i]:
                    print("\033[1;34m",colonne1[i],"\033[0m",colonne2[i],"\033[1;32m",colonne3[i],"\033[0m")
                elif numero == colonne3[i] :
                    print("\033[1;32m",colonne1[i],"\033[0m",colonne2[i],"\033[1;34m",colonne3[i],"\033[0m")
                else :
                    if numero == colonne2[i]:
                        print("\033[1;32m",colonne1[i],"\033[1;34m",colonne2[i],"\033[1;32m",colonne3[i],"\033[0m")
                    else :
                        print("\033[1;32m",colonne1[i],"\033[0m",colonne2[i],"\033[1;32m",colonne3[i],"\033[0m")


roulette()


#Mettre plus de fonction dans le code (pour changer les colonnes par exemple)



        
