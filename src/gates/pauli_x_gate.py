import numpy as np

from .quantum_gate import QuantumGate

class PauliXGate(QuantumGate):

  def __init__(self):
    self.matrix = np.array([
      [0, 1],
      [1, 0]
    ], dtype=complex)

    