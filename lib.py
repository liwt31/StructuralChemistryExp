import numpy as np
from matplotlib import pyplot as plt

def cart_contour(rho, theta, a):
    m = np.max(np.abs(a))
    plt.contourf(theta, rho, a, 100, cmap="RdBu", vmin=-m, vmax=m)
    plt.colorbar()
    plt.show()

def polar_contour(r, theta, values):
    m = np.max(np.abs(values))
    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    ax.grid(False)
    ax.set_theta_offset(np.pi/2)
    ax.contourf(theta, r, values, 100, cmap="RdBu", vmin=-m, vmax=m)
    plt.axis('off')
    plt.show()