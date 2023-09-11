import numpy as np

def Transpose(M):
    arrays = np.array(M)
    num_list = arrays.transpose().tolist()
    return num_list
