"""
Thuật toán bubble sort
"""
import random as rd
import time
def swap(a , b ):
    return (b,a)

def bubble (key):
    n = len(key)
    for i in range(n -1 ):
        for j in range(0,n-i- 1):
            if key[j] > key[j+1]:
                key[j] , key[j+1] = key[j+1], key[j]

"""
Test
"""
sample = rd.sample(range(10000),10000)
print('Before: ',sample)
start = time.time()
bubble(sample)
end = time.time()
print('After: ', sample)
print("Thời gian chạy là : ", end - start)
