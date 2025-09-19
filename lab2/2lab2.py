import numpy as np
import matplotlib.pyplot as plt

# define ranges
x = np.linspace(-4, 4, 20)
y = np.linspace(-4, 4, 20)
X, Y = np.meshgrid(x, y)

# vector field
U = X**2 + 2*Y
V = Y**2 + 2*X

# visualize quiver
plt.figure(figsize=(6, 5))
plt.quiver(X, Y, U, V, color="blue")
plt.title("Vector field F(x,y)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig("2_1.png", dpi=150)
plt.show()

# visualize stream
x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)
U = X**2 + 2*Y
V = Y**2 + 2*X

plt.figure(figsize=(6, 5))
plt.streamplot(X, Y, U, V, color=np.sqrt(U**2 + V**2), cmap="plasma")
plt.title("Streamlines of vector field F(x,y)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig("2_2.png", dpi=150)
plt.show()
