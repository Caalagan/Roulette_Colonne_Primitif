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
    #argent = int(input("Combien d'argent voulez vous mettre ? : "))
    #Test a 30€
    #argent = 30

    #Recupération de l'argent de départ dans la derniere ligne du fichier memoire_total.txt
    memoire_total = open("memoire_total.txt","r")
    argent = int(memoire_total.readlines()[-1])
    memoire_total.close()


    #Demande du nombre de tour
    #nombre_de_tour = int(input("Combien de tour voulez vous faire ? : "))
    #Test a 100 tours
    nombre_de_tour = 30

    #Demande de la mise
    #mise = int(input("Combien voulez vous miser sur chaque colonne ? : "))
    #Test a 2€
    mise = 1
    mise_initiale = mise

    #Création du min / max
    min = [argent,0]
    max = [argent,0]

    #Demande du temps de sleep (DEV)
    #temps_sleep = float(input("Combien de temps de sleep ? : "))
    #Test a 0
    temps_sleep = 0

    #Création des colonnes
    colonne1 = [1,4,7,10,13,16,19,22,25,28,31,34]
    colonne2 = [2,5,8,11,14,17,20,23,26,29,32,35]
    colonne3 = [3,6,9,12,15,18,21,24,27,30,33,36]

    #Choix des colonnes
    choix_colonne = [1,2]

    #Perte précédente
    perte_precedente = False

    #######################TEMP
    gain_double = 0
    perte_double = 0
    #######################TEMP

    #Boucle de jeu
    for i in range(nombre_de_tour):
        

        fin = False
        #Vérification si l'argent est suffisant
        while True:
            if argent >= mise and mise >= mise_initiale:
                break
            else:
                mise = mise/2
                #Transformer mise en int
                mise = int(mise)
            if mise < 0.01:
                print("Vous n'avez plus assez d'argent pour miser")
                fin = True
                break            
        if fin == True :
            break

        #Perte de la mise
        argent -= mise*2

        #Tirage du numéro
        numero = random.randint(0,36)

        #Verificattion si la colonne correspond au choix
        if numero in colonne1 and 1 in choix_colonne:
            gain += mise
            argent += mise*3
            perte_gain += mise

            #Affichage du tour
            affichage_resultat(i,mise,numero,gain,perte,argent,perte_gain,choix_colonne)

            #Changement du choix de colonne
            choix_colonne = [2,3]

            if perte_precedente == True:
                mise = mise_initiale
                perte_precedente = False
                gain_double += 1

        elif numero in colonne2 and 2 in choix_colonne:
            gain += mise
            argent += mise*3
            perte_gain += mise

            #Affichage du tour
            affichage_resultat(i,mise,numero,gain,perte,argent,perte_gain,choix_colonne)

            #Changement du choix de colonne
            choix_colonne = [1,3]

            if perte_precedente == True:
                mise = mise_initiale
                perte_precedente = False
                gain_double += 1

        elif numero in colonne3 and 3 in choix_colonne:
            gain += mise
            argent += mise*3
            perte_gain += mise

            #Affichage du tour
            affichage_resultat(i,mise,numero,gain,perte,argent,perte_gain,choix_colonne)

            #Changement du choix de colonne
            choix_colonne = [1,2]
            
            if perte_precedente == True:
                mise = mise_initiale
                perte_precedente = False
                gain_double += 1

        else:
            perte += mise*2
            perte_gain -= mise*2

            #Affichage du tour
            affichage_resultat(i,mise,numero,gain,perte,argent,perte_gain,choix_colonne)

            #Augmentation de la mise si perte

            if perte_precedente == False:
                mise *=2
                perte_precedente = True
            else:
                mise *=2
                perte_double += 1

        if argent < min[0]:
            min[0] = argent
            min[1] = i+1
        elif argent > max[0]:
            max[0] = argent
            max[1] = i+1 

        #Vérification si l'argent est suffisant
        if argent <= mise_initiale:
            print("Vous n'avez plus d'argent")
            break
        
        sleep(temps_sleep)

    stockage_resultat(i,gain,perte,argent,perte_gain,min,max)
    stockage_argent(argent)
    print("Gain double : ",gain_double)
    print("Perte double : ",perte_double)


def affichage_resultat(i,mise,numero,gain,perte,argent,perte_gain,choix_colonne):
    #Affichage des résultats
        affichage(numero,choix_colonne)
        print("")
        print("")
        print("Tours : ",i+1)
        print("Mise : ",mise)
        print("Tirage : ",numero)
        print("Gain : ",gain)
        print("Perte : ",perte)
        print("Argent : ",argent)
        print("Perte/gain : ",perte_gain)
        print("")
        print("")
        
def stockage_resultat(tours,gain,perte,argent,perte_gain,min,max):
    #Ecriture des résultats dans un fichier
    fichier = open("resultat.txt","a")
    fichier.write("Tour : "+str(tours+1)+"\n")
    fichier.write("Argent de départ : "+str(argent+perte-gain)+"\n")
    fichier.write("Argent final : "+str(argent)+"\n")
    if perte_gain > 0:
        fichier.write("Gain : +"+str(perte_gain)+"\n")
    else:
        fichier.write("Perte : "+str(perte_gain)+"\n")
    fichier.write("Minimum atteint : "+str(min[0])+" au tour "+str(min[1])+"\n")
    fichier.write("Maximum atteint : "+str(max[0])+" au tour "+str(max[1])+"\n")
    fichier.write("\n")
    fichier.write("\n")
    fichier.close()

def stockage_argent(argent):
    #Ecriture des résultats dans un fichier
    fichier = open("memoire_total.txt","a")
    fichier.write("\n"+str(argent))
    fichier.close()

        
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


fin = False
while fin == False:
    memoire_total = open("memoire_total.txt","r")
    argent = int(memoire_total.readlines()[-1])
    memoire_total.close()
    if argent >2 and argent<10000:
        roulette()
    else : 
        fin = True


#Mettre plus de fonction dans le code (pour changer les colonnes par exemple)



        
