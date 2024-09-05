# Recuperation des coordonnees et construction de matrice 2D (n, 3) avec n le nombre de phosphores
phosphore_coordinates = []
with open("coors_P.dat", "r") as file_read :
    for line in file_read :
        coords = [float(coord) for coord in line.split()]
        phosphore_coordinates.extend(coords)
import numpy as np
phosphore_coordinates = np.array(phosphore_coordinates).reshape(len(phosphore_coordinates) // 3, 3)

# Calcul de z moyen de tous les phosphores
mean_z = np.mean(phosphore_coordinates[:, 2])

# Creeation du mask de boolean pour recupere la monocouche du haut et du bas
upper_mask = phosphore_coordinates[:, 2] > mean_z
lower_mask = phosphore_coordinates[:, 2] < mean_z
upper_cordinates = phosphore_coordinates[upper_mask]
lower_cordinates = phosphore_coordinates[lower_mask]

# Calcul de la centre de masse de la membrane ainsi que la monocouche haut et la monocouche bas
# Le centre de masse est calculer par la formule somme(mixi) / somme(mi) dans notre cas les atomes on la meme masse (masse phosphore) donc somme(mi) = n * m avec n le nombre d'atomes, donc il revient a calculer la moyen
menbrane_com = np.mean(phosphore_coordinates, axis = 0)
upper_com = np.mean(upper_cordinates, axis = 0)
lower_com = np.mean(lower_cordinates, axis = 0)

# Creeation du graphique 3D
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
X_upper = upper_cordinates[:, 0] # Recuperation des positions x, y, z
Y_upper = upper_cordinates[:, 1]
Z_upper = upper_cordinates[:, 2]

X_lower = lower_cordinates[:, 0]
Y_lower = lower_cordinates[:, 1]
Z_lower = lower_cordinates[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.scatter(X_upper, Y_upper, Z_upper, color = "Salmon", marker = "o", label = "Monocouche du haut") # Ajout des points pour la monocouche du haut
ax.scatter(X_lower, Y_lower, Z_lower, color = "cyan", marker = "o", label = "Monocouche du bas") # Ajout des points pour la monocouche du bas

ax.scatter(menbrane_com[0], menbrane_com[1], menbrane_com[2], color = "green", marker = "x", label = "Centre de masse de la membrane") # Ajout du centre de masse de la membrane
ax.scatter(upper_com[0], upper_com[1], upper_com[2], color = "red", marker = "x", label = "Centre de masse de la monocouche du haut") # Ajout du centre de masse de la monocouche du haut
ax.scatter(lower_com[0], lower_com[1], lower_com[2], color = "blue", marker = "x", label = "Centre de masse de la monocouche du bas") # Ajout du centre de masse de la monocouche du bas

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Representation 3D des centres de masse')
# ax.legend(loc = 'upper right', frameon = False)
plt.show()
plt.savefig('COM_3D.jpg')