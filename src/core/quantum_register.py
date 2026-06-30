"""
quantum_register.py

Represents a quantum register.

Responsibilities:
- Store the number of qubits.
- Initialize the quantum system to the ground state.
- Maintain the current state vector.
"""

import numpy as np

class QuantumRegister:

  def __init__(self, num_qubits):
    self.num_qubits = num_qubits
    size = 2 ** num_qubits
    self.state_vector(size,dtype=complex)
    self.state_vector[0] = 1.0