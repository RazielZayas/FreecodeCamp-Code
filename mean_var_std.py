import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Matrix array de 3x3
    matrix = np.array(input_list).reshape((3, 3))

    # Diccionario de Calculos
    calculations = {}
    
    calculations['mean'] = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), np.mean(matrix).tolist()]
    calculations['variance'] = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), np.var(matrix).tolist()]
    calculations['standard deviation'] = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), np.std(matrix).tolist()]
    calculations['max'] = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), np.max(matrix).tolist()]
    calculations['min'] = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), np.min(matrix).tolist()]
    calculations['sum'] = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), np.sum(matrix).tolist()]

    return calculations

# Funcion Calculate
print(calculate([0,1,2,3,4,5,6,7,8]))