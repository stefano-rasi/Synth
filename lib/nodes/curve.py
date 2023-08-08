from nodes.curves.linear import LinearInterpolationNode

class CurveNode:
    def __init__(self, tag):
        child = tag.find()

        if child.name == 'linear-curve':
            curve_node = LinearInterpolationNode(child)

        self.curve = curve_node.curve