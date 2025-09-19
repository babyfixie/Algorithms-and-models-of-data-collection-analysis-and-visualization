import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_von_Mises_stress(stress_tensor):
    """
    stress_tensor: shape (3,3,...)
    """
    # diagonal
    s11, s22, s33 = stress_tensor[0,0], stress_tensor[1,1], stress_tensor[2,2]
    # off-diagonal
    s12, s13, s23 = stress_tensor[0,1], stress_tensor[0,2], stress_tensor[1,2]

    vm = np.sqrt(
        0.5 * ((s11 - s22)**2 + (s22 - s33)**2 + (s11 - s33)**2)
        + 3*(s12**2 + s13**2 + s23**2)
    )
    return vm

def get_colormap_ratio_on_stress(value, limits):
    vmin, vmax = limits
    return (value - vmin) / (vmax - vmin + 1e-12)  # normalize

def plot_ellipsoid(center, data, limits, radius=0.3, n_points=20, cmap=plt.cm.rainbow):
    # Base sphere
    u = np.linspace(0, 2 * np.pi, n_points)
    v = np.linspace(0, np.pi, n_points)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones_like(u), np.cos(v))

    # Scale according to tensor (based on eigenvalues/eigenvectors)
    eigvals, eigvecs = np.linalg.eigh(data)
    ellipsoid = np.array([x.flatten(), y.flatten(), z.flatten()])
    ellipsoid = eigvecs @ np.diag(np.abs(eigvals) * radius) @ ellipsoid

    x_e = ellipsoid[0].reshape(n_points, n_points) + center[0]
    y_e = ellipsoid[1].reshape(n_points, n_points) + center[1]
    z_e = ellipsoid[2].reshape(n_points, n_points) + center[2]

    # Color based on stress
    vm = get_von_Mises_stress(data)
    color_ratio = get_colormap_ratio_on_stress(vm, limits)
    color = cmap(color_ratio)

    return x_e, y_e, z_e, color

def main():
    x = np.linspace(-2*np.pi, 2*np.pi, 4)  # fewer points for faster computation
    y = np.linspace(-2*np.pi, 2*np.pi, 4)
    z = np.linspace(-2*np.pi, 2*np.pi, 4)

    X, Y, Z = np.meshgrid(x, y, z, indexing="ij")

    stress_tensor = np.array([
        [np.sin(X), X + Y, X + Z],
        [np.zeros_like(X), np.cos(Y), Y + Z],
        [np.zeros_like(X), np.zeros_like(Y), np.cos(Z)]
    ])

    vm_stress = get_von_Mises_stress(stress_tensor)
    limits = [np.min(vm_stress), np.max(vm_stress)]

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    for i in range(x.size):
        for j in range(y.size):
            for k in range(z.size):
                center = [x[i], y[j], z[k]]
                data = stress_tensor[:, :, i, j, k]
                x_e, y_e, z_e, color = plot_ellipsoid(center, data, limits, radius=0.3)
                ax.plot_surface(x_e, y_e, z_e, color=color, linewidth=0, alpha=0.8)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()

if __name__ == "__main__":
    main()
