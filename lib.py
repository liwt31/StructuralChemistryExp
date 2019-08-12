import numpy as np
from matplotlib import pyplot as plt

def cart_contour(theta, rho, a):
    plt.contourf(theta, rho, a, 100, cmap="RdBu")
    plt.colorbar()
    plt.show()

def polar_contour(theta, r, values):
    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    ax.grid(False)
    ax.set_theta_offset(np.pi/2)
    ax.contourf(theta, r, values, 100, cmap="RdBu")
    plt.axis('off')
    plt.show()