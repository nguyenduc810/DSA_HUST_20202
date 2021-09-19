"""
Thuật toán heap sort (xắp xếp đống)
author:Nguyen Duc
"""
import random as rd
import time


# hàm vun đống tại gốc i
def heapify(key, n, i):
    largest = i
    # gán giá trị chỉ mục node con trái, phải
    left = 2 * i
    right = 2 * i + 1
    # So sánh và tìm giá trị lớn nhất trong 2 node con
    if left < n and key[left] > key[largest]:
        largest = left
    if right < n and key[right] > key[largest]:
        largest = right
    # Nếu giá trị large khác với gốc i thì đổi chỗ và đệ quy để vun đống giá trị gốc là large tiếp theo
    if largest is not i:
        key[i], key[largest] = key[largest], key[i]
        heapify(key, n, largest)


# hàm xắp xếp bằng vun đống
def heapSort(key, n):
    i = int(n / 2 - 1)
    # vun đống mảng đã cho
    while i >= 0:
        heapify(key, n, i)
        i = i - 1
    # thực hiện đổi chỗ key[0] với key[j](phần tử đầu tiên với phần tử cuối cùng) sau đó lại vun đống dãy j-1 phần tử còn lại
    j = n - 1
    while j > 0:
        key[j], key[0] = key[0], key[j]
        heapify(key, j, 0)
        j = j - 1


"""
Test
"""
# tạo ngẫu nhiên 1 mảng
sample = rd.sample(range(10000), 10000)
print('Before: ', sample)
# thời gian bắt đầu thuật toán
start = time.time()
heapSort(sample, 10000)
# thời gian kết thúc thuật toán
end = time.time()
print('After: ', sample)
print('Running time: ', end - start, ' (s)')
