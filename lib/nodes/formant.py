from formant import Formant

from nodes.curve import CurveNode

from utils.audio import power_to_amplitude

class FormantNode:
    LENGTH = 1000

    def __init__(self, tag):
        curve_tag = tag.find('curve')

        curve_node = CurveNode(curve_tag)

        curve = curve_node.curve

        if tag.has_attr('scale'):
            if tag['scale'] == 'log':
                log = True
            else:
                log = False
        else:
            log = False

        curve = power_to_amplitude(curve.interpolate(self.LENGTH))

        self.formant = Formant(curve, log=log)