import pandas as pd
import numpy as np
from itertools import combinations

# === Charger les données ===
# Remplace ce chemin par le tien si nécessaire
df = pd.read_csv("output_JAX_260_df1_md.txt", delim_whitespace=True)

# === Fonction : coordonnées sphériques (az, el) -> cartésiennes (x, y, z) ===
def sph_to_cart(az_deg, el_deg, r=1.0):
    az = np.radians(az_deg)
    el = np.radians(el_deg)
    x = r * np.cos(el) * np.cos(az)
    y = r * np.cos(el) * np.sin(az)
    z = r * np.sin(el)
    return np.array([x, y, z])

# === Calcul de toutes les distances entre paires ===
distances = []
for (idx1, row1), (idx2, row2) in combinations(df.iterrows(), 2):
    p1 = sph_to_cart(row1["Az"], row1["El"])
    p2 = sph_to_cart(row2["Az"], row2["El"])
    dist = np.linalg.norm(p1 - p2)
    distances.append((row1["ID"], row2["ID"], dist))

# === Tri des distances décroissantes ===
distances_sorted = sorted(distances, key=lambda x: x[2], reverse=True)

# === Conversion en DataFrame ===
df_dist = pd.DataFrame(distances_sorted, columns=["ID_1", "ID_2", "Distance"])

# === Affichage du top 10 ===
print(df_dist.head(10))
