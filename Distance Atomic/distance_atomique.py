# Extraction des coordonnees atomiques
with open("1bta.pdb", "r") as file_pdb, open("1bta_CA.txt", "w") as file_out :
    for line in file_pdb :
        if line.startswith("ATOM") and line[12:16].strip() == "CA" :
            x = line[30:38]
            y = line[38:46]
            z = line[46:54]
            file_out.write(f"{x} {y} {z} ")
            
# Lecture des coordonnees
coordinates = []
with open("1bta_CA.txt", "r") as file_read :
    for line in file_read :
        coords = [float(coord) for coord in line.split()]
        coordinates.extend(coords)
print(f"Le nombre total de coordonnees est de {len(coordinates)}")

# Construction de la matrice de coordonees
import numpy as np
number_of_carbones_alpha = len(coordinates) // 3 # 3 coordonnees par atome (x, y, z)
coordinates = np.array(coordinates)
matrix = coordinates.reshape(number_of_carbones_alpha, 3)
print(f"La dimension de la matrice de coordonnes est de {matrix.shape}")

# Calcul de la distance
firsts_ca_matrix = matrix[:-1]
lasts_ca_matrix = matrix[1:]
# distances = np.sqrt(np.sum((firsts_ca_matrix - lasts_ca_matrix) ** 2, axis = 1))
distances = np.linalg.norm(firsts_ca_matrix - lasts_ca_matrix, axis = 1)
for i in range(len(distances)) :
    print(f"La distance entre l'atome {i + 1} et l'atome {i + 2} est de {distances[i]: .1f}")
unexpected_value = np.argmax(distances)
print(f"La valeur suprenante est de {distances[unexpected_value]: .1f} et elle se trouve entre l'atome {unexpected_value + 1} et l'atome {unexpected_value + 2}")