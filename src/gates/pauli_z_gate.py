import numpy as np

from .quantum_gate import QuantumGate


class PauliZGate(QuantumGate):
    def __init__(self):
        self.matrix = np.array([[1, 0], [0, -1]], dtype=complex)
