import numpy as np
import pandas as pd
def my_func(matrix_1, matrix_2):
	try:
		return matrix_1 * matrix_2
	except ValueError:
		print("Matrices are not aligned")
		return None 

my_matrix = np.identity(5)
my_2nd_matrix = np.random.random(size=(4,4))
print(my_func(my_matrix, my_2nd_matrix))
