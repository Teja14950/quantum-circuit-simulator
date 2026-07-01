import numpy as np

from .quantum_gate import QuantumGate


class PauliYGate(QuantumGate):
    def __init__(self):
        self.matrix = np.array([[0, -1j], [1j, 0]], dtype=complex)
