# Lattice Boltzmann
from configparser import Interpolation
import numpy as np
import matplotlib.pyplot as plt
import cv2

# plot_every = 50

# TESLA VALVE
image = cv2.imread("tesla_2.png", 0)
image = cv2.resize(image, (300, 50))
image = image.astype(np.float32)

image[image != 255] = 0
image = image/255

# CHANNEL
# image = cv2.imread("rect.png", 0)
# image = cv2.resize(image, (200, 50))
# plt.imshow(image, cmap='gray')
# image = image.astype(np.float32)

# image[image == 0] = 255
# image[image != 255] = 0
# image = image/255

# image = np.invert(image.astype(np.uint8)).astype(np.float32)
# imagePoints = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# y, x = np.where(imagePoints == 1)
# puntos = list(zip(y, x))

# image = cv2.imread("pw.png", 0)
# image = cv2.resize(image, (300, 50))
# plt.imshow(image, cmap='gray')


# image[image != 255] = 0
# image = image/255

# image = cv2.imread("p.png", 0)
# image = cv2.resize(image, (300, 50))
# # plt.imshow(image, cmap='gray')
# image[image != 0] = 1


# image = cv2.imread("base2.png", 0)
# image = cv2.resize(image, (300, 50))
# image = np.invert(image.astype(np.uint8)).astype(np.float32)

# image[image != 0] = 1


def distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def main(cyl):
    Nx = 300
    Ny = 50
    tau = 0.53
    Nt = 10000

    # Initialize the lattice
    # lattice speeds and weights (D2Q9)
    Nl = 9
    cxs = np.array([0, 0, 1, 1, 1, 0, -1, -1, -1], dtype=np.int64)
    cys = np.array([0, 1, 1, 0, -1, -1, -1, 0, 1], dtype=np.int64)
    weights = np.array([4/9, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36], dtype=np.longdouble)

    # Initialize the fluid
    F = np.ones((Ny, Nx, Nl), dtype=np.longdouble) + 0.01 * np.random.randn(Ny, Nx, Nl)
    F[:, :, 3] = 2.3

    cylinder = np.full((Ny, Nx), False)

    # if cyl:
    #     for y in range(Ny):
    #         for x in range(Nx):

    #             if distance(Nx//8, Ny//2, x, y) < 8:
    #                 cylinder[y][x] = True

    #             if distance(Nx//8, Ny//1, x, y) < 8:
    #                 cylinder[y][x] = True

    #             if distance(Nx//8, 1, x, y) < 8:
    #                 cylinder[y][x] = True

    #             if distance(Nx//4, Ny//1.3, x, y) < 8:
    #                 cylinder[y][x] = True

    #             if distance(Nx//4, Ny//4, x, y) < 8:
    #                 cylinder[y][x] = True

    #             if distance(Nx//2.6, Ny//2, x, y) < 8:
    #                 cylinder[y][x] = True

    #             if distance(Nx//2.6, Ny//1, x, y) < 8:
    #                 cylinder[y][x] = True

    #             if distance(Nx//2.6, 1, x, y) < 8:
    #                 cylinder[y][x] = True

    #             if distance(Nx//2, Ny//1.3, x, y) < 8:
    #                 cylinder[y][x] = True

    #             if distance(Nx//2, Ny//4, x, y) < 8:
    #                 cylinder[y][x] = True

    #             if distance(Nx//1.6, Ny//2, x, y) < 8:
    #                 cylinder[y][x] = True

    #             if distance(Nx//1.6, Ny//1, x, y) < 8:
    #                 cylinder[y][x] = True

    #             if distance(Nx//1.6, 1, x, y) < 8:
    #                 cylinder[y][x] = True

    # if (x, y) in puntos:
    #     cylinder[y][x] = True

    # To optimize performance, we only sum the cylinder image
    # with the binary image of the valve.
    cylinder = cylinder + image.astype(np.bool_)

    for it in range(Nt):
        # print(it)
        F[:, -1, [6, 7, 8]] = F[:, -2, [6, 7, 8]]
        F[:, 0, [2, 3, 4]] = F[:, 1, [2, 3, 4]]

        for i, cx, cy in zip(range(Nl), cxs, cys):
            F[:, :, i] = np.roll(F[:, :, i], cx, axis=1)
            F[:, :, i] = np.roll(F[:, :, i], cy, axis=0)

        bndryF = F[cylinder, :]
        bndryF = bndryF[:, [0, 5, 6, 7, 8, 1, 2, 3, 4]]

        # Fluid variables
        rho = np.sum(F, 2, dtype=np.double)
        ux = np.sum(F * cxs, 2, dtype=np.double) / rho
        uy = np.sum(F * cys, 2, dtype=np.double) / rho

        F[cylinder, :] = bndryF
        ux[cylinder] = 0
        uy[cylinder] = 0

        # Collision step
        Feq = np.zeros(F.shape, dtype=np.longdouble)
        for i, cx, cy, w in zip(range(Nl), cxs, cys, weights):
            Feq[:, :, i] = rho*w*(1 + 3*(cx*ux + cy*uy) + 9*(cx*ux + cy*uy)**2 / 2 - 3*(ux**2 + uy**2)/2)

        F = F + -(1/tau)*(F-Feq)

        if it % 50 == 0:

            plt.ion()
            plt.subplot(1, 1, 1)
            graph = np.clip(np.sqrt(ux**2 + uy**2), 0, 1)
            graph[cylinder] = np.NaN
            plt.imshow(graph, cmap="hot", interpolation="bilinear")

            # plt.subplot(5, 1, 2)
            # plt.imshow(np.clip(ux, 0, 1), cmap='hot', interpolation='bilinear')

            # plt.subplot(5, 1, 3)
            # plt.imshow(np.clip(uy, 0, 1), cmap='hot', interpolation='bilinear')

            # vorticity = (np.roll(ux, -1, axis=0) - np.roll(ux, 1, axis=0)) - (np.roll(uy, -1, axis=1) - np.roll(uy, 1, axis=1))
            # vorticity[cylinder] = np.nan

            # plt.subplot(5, 1, 4)
            # plt.imshow(vorticity, cmap='RdBu', interpolation='bilinear')

            # plt.subplot(5, 1, 5)
            # plt.imshow(rho, cmap='RdBu', interpolation='bilinear')
            # plt.colorbar()
            plt.pause(0.000000000001)
            plt.cla()


if __name__ == "__main__":
    main(True)
