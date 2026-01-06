from asch import generate
from arbre import solve, solveDf

df = generate(1)
result = solve(df.loc[0])

df = generate(10)

solved = solveDf(df)


from sklearn import tree
import matplotlib.pyplot as plt

inputs = df[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']]
output = df[['v']]
arbre = tree.DecisionTreeClassifier()

arbre = arbre.fit(inputs, output)
tree.plot_tree(arbre)


dfTest = generate(1)
print(dfTest)

repArbre = arbre.predict(dfTest[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']])
repSolver = solve(dfTest.loc[0])

print(repArbre, repSolver)
