
def set_axes_equal(ax):
    """Fixe le rapport d’échelle de l'axe 3D pour qu'une sphère ait l'air ronde"""
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    plot_radius = 0.5 * max([x_range, y_range, z_range])
    
    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])






import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Charger les données
df = pd.read_csv("output_JAX_068_df1_md.txt", delim_whitespace=True)

# Conversion en radians
az = np.radians(df["Az"].values)
el = np.radians(df["El"].values)

# Rayon de la sphère (scène)
r = 1.0

# Conversion sphérique → cartésienne
x = r * np.cos(el) * np.cos(az)
y = r * np.cos(el) * np.sin(az)
z = r * np.sin(el)

# Création de la figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Tracer la sphère
u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
xs = np.cos(u) * np.sin(v)
ys = np.sin(u) * np.sin(v)
zs = np.cos(v)
ax.plot_surface(xs, ys, zs, color='lightblue', alpha=0.3)

# Tracer les satellites
ax.scatter(x, y, z, color='red', s=50)

# Options d'affichage
ax.set_title("Visualisation des satellites autour d'une scène sphérique")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
