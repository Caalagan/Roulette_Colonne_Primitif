### Conclusion temporaire

PAS WORTH DU TOUT, que des descente en partant de 1000€ avec 1€ de mise


## A faire :

    - Recalculer si la mise double est good ou pas
    - Voir si la mise double a l'infini est bien ou pas
    - Empecher de miser si la mise est superieur au solde



    - Diversifier ? avec du noir rouge pair impair manque passe

## A faire apres le projet :

    - Faire un fichier de config pour les variables


# Roulette_Colonne_Primitif

Ce projet est une version pprimitive du projet final, il s'agit d'un jeu de roulette avec une mise precise :

    - La mise porte sur les deux colonne non gagnante de la manche précédente (normalement 60% de chance de gagner [à verifier])

    - La mise est de 2€ (comme dansmon casino)

    - Il y a minimum une colonne de perdante

    - Le gain est de 6€ si la mise est gagnante sur une colonne 

    - Le total sur une manche gagnante est donc : mise de 2€ + 2€ / perte d'une colonne - 2€ / gain d'une colonne + 6€ / Total : +2€

    - Le total sur une manche perdante est donc : mise de 2€ + 2€ / perte de deux colonne - 4€ / Total : -4€