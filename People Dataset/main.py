import pandas as pd

# Chargement du jeu de données
dataframe = pd.read_csv('people.tsv', sep = '\t', index_col = 'name')
print(f"Les 6 premiers lignes du jeu de données sont : \n{dataframe.head(6)}")
print(f"Le jeu de donnees comporte {dataframe.shape[0]} lignes")

# Selections
print(f"La taille de Claire est de {dataframe.loc['claire', 'size']} cm")
print(f"L'age de Baptiste est de {dataframe.loc['baptiste', 'age']}")
print(f"L'age de Paul et de Bob sont respectivement {dataframe.loc[['paul', 'bob'], 'age'].values} ans")

# Statistiques descriptives et table de comptage
print(f"La taille moyenne des personnes est de {dataframe['size'].mean()} cm et la taille minimale est de {dataframe['size'].min()} cm")
print(f"L'age  moyenne des personnes est de {int(dataframe['age'].mean())} ans et l'age minimale est de {dataframe['age'].min()} ans")
print(f"Le nombre de personne de sexe masculin est de {len(dataframe[dataframe['sex'] == 'male'])}")
print(f"Le nombre de personne de sexe feminin est de {len(dataframe[dataframe['sex'] == 'female'])}")

# Statistiques par groupe
print(f"La taille et l'age moyenne chez les hommes sont respectivement {dataframe.groupby('sex').mean().loc['male', ['size', 'age']].values}")
print(f"La taille et l'age moyenne chez les femmes sont respectivement {dataframe.groupby('sex').mean().loc['female', ['size', 'age']].astype(int).values}")

# Selection par filtre
print(f"Le nombre d'individus mesurant plus de 180 cm est de {len(dataframe[dataframe['size'] > 180])}")
print(f"La femme qui a moins de 35 ans est {dataframe[(dataframe['sex'] == 'female') & (dataframe['age'] < 35)].index.values[0].capitalize()}")

# Selection et Statistique
print(f"L'age moyen des individus qui mesurent plus de 180 cm est de {int(dataframe[dataframe['size'] > 180]['age'].mean())} ans")
print(f"La taille maximale des femmes qui ont plus de 35 ans est de {dataframe[(dataframe['sex'] == 'female') & (dataframe['age'] > 35)]['size'].max()} cm")