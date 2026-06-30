"""
quantum_gate.py

Represents a generic quantum gate.

Responsibilities:
- Define the interface for all quantum gates.
- Transform a QuantumRegister.
"""

class QuantumGate:

  def apply(self, register):
    new_state = self.matrix @ register.state_vector
    register.state_vector = new_state
    

