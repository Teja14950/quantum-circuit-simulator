import numpy as np


def measure(register):
    probabilities = np.abs(register.state_vector) ** 2
    outcome = np.random.choice(len(probabilities), p=probabilities)
    collapsed_state = np.zeros(len(probabilities), dtype=complex)
    collapsed_state[outcome] = 1
    register.state_vector = collapsed_state
    return outcome
