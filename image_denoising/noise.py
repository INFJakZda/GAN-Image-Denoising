import numpy as np
import random
from PIL import Image
import cv2


def add_noise(image: np.ndarray, mode: str):
    """
    Parameters
    ----------
    image : ndarray
        Input image resources. Will be converted to float.
    mode : str
        One of the following strings, selecting the type of noise to add:

        'gauss'     Gaussian-distributed additive noise.
        'sp'       Replaces random pixels with 0 or 1.
        'speckle'   Multiplicative noise using out = image + n*image,where
                    n is uniform noise with specified mean & variance.
    """
    if mode == 'gauss':
        mean = 0
        var = 10
        gauss = np.random.normal(mean, var ** 0.5, image.shape)
        noisy = image + gauss
        noisy[noisy < 0] = 0
        noisy[noisy > 255] = 255
        return noisy

    elif mode == 'sp':
        prob = 0.05
        noisy = np.zeros(image.shape, np.uint8)
        thres = 1 - prob
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                rdn = random.random()
                if rdn < prob:
                    noisy[i][j] = 0
                elif rdn > thres:
                    noisy[i][j] = 255
                else:
                    noisy[i][j] = image[i][j]
        return noisy

    elif mode == 'speckle':
        row, col, ch = image.shape
        speckle = np.random.randn(row, col, ch) * 0.15
        speckle = speckle.reshape(row, col, ch)
        noisy = image + image * speckle
        return noisy
