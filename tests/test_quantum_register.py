from src.core.quantum_register import QuantumRegister

def test_register_stores_number_of_qubits():
  register = QuantumRegister(3)
  assert register.num_qubits==3

def test_state_vector_has_correct_size():
  register = QuantumRegister(3)
  assert len(register.state_vector) == 8

def test_register_initializes_to_ground_state():
  register = QuantumRegister(3)

  assert register.state_vector[0] == 1 + 0j
  assert all(amplitude == 0 for amplitude in register.state_vector[1:])