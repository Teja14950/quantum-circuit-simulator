import numpy as np

def tensor_product(vector1, vector2):
  
  result = []

  for element1 in vector1:
    for element2 in vector2:
      result.append(element1 * element2)

  return np.array(result, dtype = complex)