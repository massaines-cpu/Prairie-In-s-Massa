from arbre import generate
from numpy import mean
from solver import solve, solveDf
from sklearn import tree
import matplotlib.pyplot as plt

df = generate(1)
result = solve(df.loc[0])

df = generate(10)

solved = solveDf(df)

df_train = generate(30)  # 500 pour l'entrainement
df_test = generate(1000)   # 50 pour tester
df_test = df_test[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']] # pas besoin de v on le calculera au fur et a mesure

# resoudre (remplir v) pour les data d'entrainement
df_train = solveDf(df_train)

# séparer in et out
inputs = df_train[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']]
output = df_train[['v']]

# créer l'arbre
arbre = tree.DecisionTreeClassifier()

# entrainer l'arbre
arbre = arbre.fit(inputs, output)

dfTest = generate(1)
print(dfTest)

repArbre = arbre.predict(dfTest[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']])
repSolver = solve(dfTest.loc[0])

print(repArbre, repSolver)

#calcul pourcentage bonne réponse
#définir ce qu'est une bonne réponse
#comparer repArbre et repSolver
#calculer uniquement pourcentage de bonne reponse de reArbre car repSolver 100% vrai
stat = []
# pour chaque ligne du df de test
for i in range(len(df_test)):
    # récupérer la ligne
    row = df_test.iloc[[i]]
    # faire la prédiction à partir de la ligne (sans v)
    prediction = arbre.predict(row)
    # faire la prédiction avec le solver
    solution = solve(row.loc[0])
    # stocker 0 (erreur de l'arbre) ou 1 (réussite de l'arbre)
    stat.append(int(prediction[0] == solution))

# affichage des résultats
print("moyenne: ", mean(stat))

dfTest = generate(300)
repArbre = arbre.predict(dfTest[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']])
dfTest['vArbre'] = repArbre
dfTestSolved = solveDf(dfTest)
bonnesReponses = dfTestSolved[dfTestSolved['v'] == dfTestSolved['vArbre']]
print(len(bonnesReponses) / len(dfTestSolved) * 100)