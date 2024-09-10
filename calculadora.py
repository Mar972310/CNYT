import numpy as np

def dimension_vectors(v1,v2):
    if v1.shape == v2.shape:
        return True
    return False

def dimension_matrices(M1,M2):
    dimension1 = M1.shape
    dimension2 = M2.shape
    if dimension1 == dimension2:
        return True
    return False

def add_complex_vectors(v1,v2):
    if dimension_vectors(v1,v2) == True:
        return np.add(v1,v2)
    else:
        raise Exception ("Error: Los vectores no tienen las mismas dimensiones")

def iverso_vector(v1):
    inverso = np.negative(v1)
    return inverso

def multiplication_scalar_vector(scalar,vec1):
    multiplication = np.multiply(scalar,vec1)
    return multiplication

def add_complex_matrix(M1, M2):
    if dimension_matrices(M1,M2) == True:
        sum = np.add(M1,M2)
        return sum
    else: 
        raise Exception ("Error: Las matrices no tienen las mismas dimensiones")

def inversa_complex_matrix(M):
    return np.negative(M)

def multiplication_scalar_matrix(scalar,M):
    multiplication = np.multiply(scalar,M)
    return multiplication

def transpose_complex_matrix_vecto(a):
    transpose = a.T
    return transpose

def conjugate_complex_matrix_or_vector(a):
    conjugate = np.conjugate(a)
    return conjugate

def adjunct_matrix_or_vector(a):
    adjunct = np.conjugate(a.T)
    return adjunct


       

