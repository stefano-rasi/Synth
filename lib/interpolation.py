class Interpolation:
    def __init__(self, values):
        self.values = sorted(values)

    def interpolate(self, value):
        start = None
        stop = None

        for point in self.values:
            if point[0] <= value:
                start = point
            else:
                stop = point

                break

        if start is None:
            return self.values[0][1]

        if stop is None:
            return start[1]

        amount = (value - start[0]) / (stop[0] - start[0])

        return start[1] * (1 - amount) + stop[1] * amount
