import yaml

import numpy as np

from curves.linear import LinearInterpolation

class LinearInterpolationNode:
    def __init__(self, tag):
        if tag.has_attr('y-max'):
            y_max = float(tag['y-max'])
        else:
            y_max = 1

        points = yaml.safe_load(tag.text)

        for x in points:
            points[x] = points[x] / y_max

        points_array = np.array(list(points.items()))

        self.curve = LinearInterpolation(points_array)