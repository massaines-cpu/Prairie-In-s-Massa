# Exercice Asch Theory

Objectif : Créer un arbre de décision pour l’expérience de Asch

## Ce qu'on a fait

- Introduction des bibliothèques Pandas, Numpy, Sklearn, Matplotlib
- Définir des fonctions qui vont être liées à notre code final, DP strategy ?

## Les définitions des fonctions
### Fonction 1 : Création du tableau
```
import random
import pandas as pd

def generate(n):
    ash_keys = ['a', 'b', 'c', 'd', 'v', '1', '2', '3', 'ref'] 
    df = pd.DataFrame(columns=ash_keys)                        
    for i in range(n):                                         
        bars = set()                                         
        while len(bars) < 3:                                   
            bars.add(random.randrange(1, 11))
        bars = list(bars)                                      
        bonne_reponse = random.randrange(1, 3)                 
        ref = bars[bonne_reponse -1]                                   
        choix_des_complices = random.randrange(1, 3)           
        while bars[choix_des_complices -1] == ref:            
            choix_des_complices = random.randrange(1, 3)
        df = pd.concat([df, pd.DataFrame([[                    
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

```


## LIEN DEPÔT
[Lien vers exercice]()
