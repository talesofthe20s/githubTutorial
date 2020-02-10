import numpy as numpy
def my_func(matrix_1, matrix_2):
	return matrix_1 * matrix_2

my_matrix = np.identity(4)
my_2nd_matrix = np.random.random(size=(4,5))


print(my_func(my_matrix, my_2nd_matrix))