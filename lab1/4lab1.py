import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def second_order_surface():
    # Constants
    a, b, c = 2, 1, 2  

    # Ranges
    u = np.linspace(0, 2*np.pi, 100)  # angle
    v = np.linspace(-2, 2, 100)       # vertical coordinate

    U, V = np.meshgrid(u, v) # grid

    # Parametric equations of hyperboloid
    X = a * np.cosh(V) * np.cos(U)
    Y = b * np.cosh(V) * np.sin(U)
    Z = c * np.sinh(V)

    # Plot
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8, edgecolor="none")

    # Labels
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title(r"$\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$")

    plt.show()

if __name__ == "__main__":
    second_order_surface()
