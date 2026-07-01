import numpy as np

from src.core.quantum_register import QuantumRegister
from src.measurement.measurement import measure
from src.gates.pauli_x_gate import PauliXGate


def test_measure_zero_state():
    register = QuantumRegister(1)
    result = measure(register)
    assert result == 0
    np.testing.assert_array_equal(
        register.state_vector, np.array([1, 0], dtype=complex)
    )


def test_measure_one_state():
    register = QuantumRegister(1)
    PauliXGate().apply(register)
    result = measure(register)
    assert result == 1
    np.testing.assert_array_equal(
        register.state_vector, np.array([0, 1], dtype=complex)
    )
