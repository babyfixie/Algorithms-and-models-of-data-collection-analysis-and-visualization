import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# bar charts
def bar_charts():
    # years
    years = [1900, 1913, 1929, 1938, 1950, 1960, 1970, 1980, 1990, 2000]

    # number of employed
    employed = {
        "Germany": [18.5, 23.5, 25, 26.5, 29, 31, 34, 35, 37, 38.5],
        "France": [20, 20, 20, 19.5, 19, 21, 23, 25, 26.5, 27.5],
        "Great Britain": [16.5, 18.5, 20, 20.5, 22.5, 24, 25, 25.5, 26, 26.5],
        "Italy": [15, 16.5, 17, 18, 18.5, 20, 22, 24, 24.5, 25]
    }

    # data
    countries = list(employed.keys())
    data = np.array(list(employed.values()))

    # 2d bar chart
    x = np.arange(len(years))  # X positions
    bar_width = 0.18

    fig, ax = plt.subplots(figsize=(12, 6))

    # Cycle for bar chart
    for i, country in enumerate(countries):
        ax.bar(x + i*bar_width, employed[country], bar_width, label=country)

    # Labels
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Employed (mln people)")
    ax.set_title("Employment by Country (1900–2000)")
    ax.set_xticks(x + bar_width * (len(countries)-1)/2)
    ax.set_xticklabels(years, rotation=45)
    ax.legend()
    ax.grid(True)

    # Plot
    plt.tight_layout()
    plt.show()

    # 3d bar chart
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Data
    xpos, ypos = np.meshgrid(np.arange(len(years)), np.arange(len(countries)))
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros_like(xpos)

    dx = dy = 0.5 * np.ones_like(zpos)
    dz = data.flatten()

    # Plot
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, shade=True)

    # Labels
    ax.set_xticks(np.arange(len(years)))
    ax.set_xticklabels(years, rotation=45)
    ax.set_yticks(np.arange(len(countries)))
    ax.set_yticklabels(countries)
    ax.set_zlabel("Number of Employed (mln)")

    ax.set_title("3D Bar Chart of Employment (1900–2000)")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    bar_charts()
