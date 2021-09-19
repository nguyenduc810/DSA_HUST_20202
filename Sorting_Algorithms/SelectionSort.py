"""
Thuật toán selection sort
"""
import  random as rd
import time
def SelectionSort(key):
    n = len(key)
    for i in range(n-1):
        k = i
        for j in range(i+1 ,n):
            if(key[k] > key[j]):
                k = j
        if (k!= i):
            key[i], key[k] = key[k] , key[i]

"""
Test
"""
sample = rd.sample(range(10000),10000)
print("Before: ", sample)
start = time.time()
SelectionSort(sample)
end = time.time()
print("After: ", sample)
print('Thời gian chạy là : ' , end - start)