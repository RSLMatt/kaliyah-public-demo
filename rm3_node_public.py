class RM3Node:
    def __init__(self, identity, kc=1.0, phase=0.0, amplitude=1.0):
        self.identity = identity
        self.kc = kc
        self.phase = phase
        self.amplitude = amplitude

    def resonate(self, other_identity):
        return self.identity in other_identity or other_identity in self.identity
