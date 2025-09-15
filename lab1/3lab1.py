import numpy as np
import matplotlib.pyplot as plt

# Polar plot
def polar_plot():
    a = -1 # constant (-1, 0, 1)
    phi = np.linspace(-np.pi/2 + 0.01, np.pi/2 - 0.01, 100)  # angle

    rho = 2 * a * (np.sin(phi)**2) / np.cos(phi)

    fig = plt.figure(figsize=(8, 8)) 
    ax = fig.add_subplot(111, projection='polar')

    # Plot
    ax.plot(phi, rho, label=r"$\rho = 2a \frac{\sin^2 \varphi}{\cos \varphi}$", color="purple")

    # Grid, labels, legend
    ax.set_title("Polar plot", va='bottom')
    ax.legend(loc="upper right")
    ax.grid(True)

    plt.show()

if __name__ == "__main__":
    polar_plot()
