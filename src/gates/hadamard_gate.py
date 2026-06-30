import numpy as np

from .quantum_gate import QuantumGate

class HadamardGate(QuantumGate):
  
  def __init__(self):
    self.matrix = (1/np.sqrt(2))*np.array([
      [1, 1],
      [1, -1]
    ], dtype=complex)

