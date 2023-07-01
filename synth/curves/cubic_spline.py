import scipy

import numpy as np

class CubicSpline:
    def __init__(self, points):
        self.x = np.array(points)[:,0]
        self.y = np.array(points)[:,1]

        self.spline = scipy.interpolate.CubicSpline(self.x, self.y)

    def interpolate(self, length):
        xs = np.linspace(0, self.x[-1], length)

        return self.spline(xs)