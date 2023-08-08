from nodes.curve import CurveNode

from envelope import EnvelopeFactory

class EnvelopeNode:
    def __init__(self, tag, sample_rate):
        if tag.find('attack'):
            attack_tag = tag.find('attack')

            curve_tag = attack_tag.find('curve')

            curve_node = CurveNode(curve_tag)

            attack_curve = curve_node.curve

            attack_length = round(float(attack_tag['duration']) * sample_rate)

            attack = attack_curve.interpolate(attack_length)
        else:
            attack = []

        if tag.find('decay'):
            decay_tag = tag.find('decay')

            curve_tag = decay_tag.find('curve')

            curve_node = CurveNode(curve_tag)

            decay_curve = curve_node.curve

            decay_length = round(float(decay_tag['duration']) * sample_rate)

            decay = decay_curve.interpolate(decay_length)
        else:
            decay = []

        if tag.find('release'):
            release_tag = tag.find('release')

            curve_tag = release_tag.find('curve')

            curve_node = CurveNode(curve_tag)

            release_curve = curve_node.curve

            release_length = round(float(release_tag['duration']) * sample_rate)

            release = release_curve.interpolate(release_length)
        else:
            release = []

        self.envelope = EnvelopeFactory(attack, decay, release)