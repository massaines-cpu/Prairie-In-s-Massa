import random
import pandas as pd

def generate(n):
    ash_keys = ['a', 'b', 'c', 'd', 'v', '1', '2', '3', 'ref'] # les colonnes de mon df
    df = pd.DataFrame(columns=ash_keys)                        # créer le df

    for i in range(n):                                         # n fois
        bars = set()                                           # un set c'est (presque) comme un tableau mais sans doublon
        while len(bars) < 3:                                   # je crée les 3 barres.
            bars.add(random.randrange(1, 11))                  # Comme c'est un set il ne peut pas y avoir deux barres de la même taille
                                                               # je mets un while car je dois créer des arbres jusqu'à ce que j'en ai 3

        bars = list(bars)                                      # je transforme en list c'est plus pratique qu'un set
        bonne_reponse = random.randrange(1, 3)                 # choisir au hasard une barre 
        ref = bars[bonne_reponse -1]                           # mettre la même taille à la ref
        
        choix_des_complices = random.randrange(1, 3)           # pour les complices il ne faut pas qu'ils choisissent la bonne réponse !
        while bars[choix_des_complices -1] == ref:             # donc je choisi au hasard jusqu'a ce que ce soit faux
            choix_des_complices = random.randrange(1, 3)

        df = pd.concat([df, pd.DataFrame([[                    # j'ajoute ma "ligne" à mon df.
            choix_des_complices, # a
            choix_des_complices, # b
            choix_des_complices, # c
            choix_des_complices, # d,
            None,                # v
            bars[0],             # 1
            bars[1],             # 2
            bars[2],             # 3
            ref                  # ref
        ]], columns=ash_keys)])

    return df


if __name__ == "__main__":
    df = generate(10)
    print(df)