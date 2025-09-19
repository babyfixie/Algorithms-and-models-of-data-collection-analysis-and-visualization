import numpy as np
import matplotlib.pyplot as plt

# define ranges
n = 100
x = np.linspace(0, 5, n)
y = np.linspace(0, 5, n)
X, Y = np.meshgrid(x, y)

# scalar field
U = X * np.sqrt(Y) + Y * np.sqrt(X)

# visualize
plt.figure(figsize=(6, 5))
plt.pcolormesh(X, Y, U, shading='auto', cmap='viridis')
plt.colorbar(label="u(x,y)")
plt.title("Scalar field u(x,y)")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("1_1.png", dpi=150)
plt.show()

# gradient
Ux, Uy = np.gradient(U, x, y)

plt.figure(figsize=(6, 5))
plt.pcolormesh(X, Y, U, shading='auto', cmap='viridis', alpha=0.6)
plt.colorbar(label="u(x,y)")
plt.quiver(X, Y, Ux, Uy, color="red")
plt.title("Gradient of scalar field (vector field)")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("1_2.png", dpi=150)
plt.show()
