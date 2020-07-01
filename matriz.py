#librería numpy#
import numpy as np
def split(arr, size): #division de lista por semana#
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs