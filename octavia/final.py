from arbre import generate
from numpy import mean
from solver import solve, solveDf
from sklearn import tree
import matplotlib.pyplot as plt

df_train = generate(30)  # 500 pour l'entrainement
df_test = generate(10)   # 50 pour tester
df_test = df_test[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']] # pas besoin de v on le calculera au fur et a mesure

# résoudre (remplir v) pour les data d'entrainement
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
print("moyenne: ", mean(stat)*100)
pickle.dump(arbre, open("model.pkl", 'wb'))