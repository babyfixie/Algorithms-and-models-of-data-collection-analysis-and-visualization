import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def surface_plot():
    # Define ranges
    x = np.linspace(0, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)

    # Function z(x,y)
    Z = (3*X - 1) * np.sqrt(X) + 2 * np.sin(Y)**2

    # Plot
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

    # Labels
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title(r"$z=(3x-1)\sqrt{x} + 2\sin^2(y)$")

    # Color bar
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

if __name__ == "__main__":
    surface_plot()
