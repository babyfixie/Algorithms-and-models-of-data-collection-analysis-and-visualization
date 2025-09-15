import numpy as np
import matplotlib.pyplot as plt

# y(x)
def y_func(x):
    return 5 * np.sin(x) * np.cos(3 * x + 1)

# z(x)
def z_func(x):
    z = np.zeros_like(x)
    # Case 1: x <= -1
    mask1 = x <= -1
    z[mask1] = (1 + np.abs(x[mask1])) / np.cbrt(1 + x[mask1] + x[mask1]**2)
    # Case 2: -1 < x < 0
    mask2 = (x > -1) & (x < 0)
    z[mask2] = 2 * np.log(1 + x[mask2]**2) + (1 + np.cos(x[mask2])**4) / (2 + x[mask2])
    # Case 3: x >= 0
    mask3 = x >= 0
    z[mask3] = (1 + x[mask3])**(3/5)
    return z

def plot_functions():
    x = np.linspace(-5, 5, 1000)  # Generate x values

    plt.figure(figsize=(10, 6)) 
    plt.plot(x, y_func(x), label=r'$y = 5 \sin(x)\cos(3x+1)$', color='blue') 
    plt.plot(x, z_func(x), label=r'$z(x)$', color='red')

    # Labels, grid, legend
    plt.xlabel("x")
    plt.ylabel("y, z")
    plt.title("Function plots")
    plt.grid(True)
    plt.legend()

    # Add equation text
    plt.text(0.5, -4, r"$y=5\sin(x)\cos(3x+1)$", fontsize=10, color="blue")
    plt.text(-4.5, 2, r"$z(x)$", fontsize=10, color="red")

    plt.show()

if __name__ == "__main__":
    plot_functions()
