import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# define grid
x = np.linspace(-3, 4, 5)
y = np.linspace(-3, 4, 5)
z = np.linspace(-3, 4, 5)
X, Y, Z = np.meshgrid(x, y, z)

# vector field F
den = X**2 + Y**2 + Z**2 + 1e-6  # to avoid division by zero
U = (Y*Z) / den
V = (X*Z) / den
W = (X*Y) / den

# visualize
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W, length=0.5, normalize=True, color="blue")
ax.set_title("3D Vector Field F(x,y,z)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("vector_field_3d.png", dpi=150)
plt.show()