import scipy

import numpy as np

class LinearInterpolation:
    def __init__(self, points):
        self.x = np.array(points)[:,0]
        self.y = np.array(points)[:,1]

        self.curve = scipy.interpolate.interp1d(self.x, self.y)

    def interpolate(self, length):
        xs = np.linspace(0, self.x[-1], length)

        return self.curve(xs)