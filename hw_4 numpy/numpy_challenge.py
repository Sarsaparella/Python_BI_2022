import numpy as np


if __name__ == '__main__':
    first = np.full((14, 14), 0)
    second = np.mgrid[1:7, 1:7]
    third = np.zeros((14, 14), int)
    np.fill_diagonal(third, 4)



def matrix_multiplication(mat1, mat2):
    return np.matmul(mat1, mat2)

def multiplication_check(list_of_matrices):
    rows, cols = [], []
    for mat in list_of_matrices:
        row, col = mat.shape
        rows.append(row)
        cols.append(col)
    if rows[1:] == cols[:-1]:
        return True
    else:
        return False

def multiply_matrices(list_of_matrices):
    if multiplication_check(list_of_matrices):
        return np.linalg.multi_dot(list_of_matrices)
    else:
        return None

def compute_2d_distance(arr1, arr2):
    return np.linalg.norm(arr1 - arr2)

def compute_multidimensional_distance(arr1, arr2):
    return np.linalg.norm(arr1 - arr2)

def compute_pair_distances(array):
    return np.linalg.norm(array[:, None, :] - array[None, :, :], axis=-1)