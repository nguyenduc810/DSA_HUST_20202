
def dSort(key):
    n = len(key)
    max = key[0]
    for i in range(1,n):
        if max < key[i] :
            max = key[i]
    count = max*[0]
    ##for i in range(max+1):
      ##  count.append(0)
    for i in range(n):
        count[key[i]] += 1
    for i in range(1,max+1):
        count[i] = count[i] + count[i-1]
    newkey = n*[0]
    #for i in range(n):
     #   newkey.append(0)
    for i in range(n):              # sửa
        count[key[i]] -= 1
        newkey[count[key[i]]] = key[i]
    key[0:n] = newkey
def radixSort(key):
    n = len(key)
    max = key[0]
    for i in range(1,n):
        if max < key[i]:
            max = key[i]
    bucket = 10*[0]
    esp = 1
    temp = n*[0]
    while max / esp > 0 :
        for i in range(n):
            bucket[(int(key[i]/esp)) % 10] += 1
        for i in range(1,10):
            bucket[i] = bucket[i]+ bucket[i-1]
        for i in range(n):
            bucket[(int(key[i] / esp)) % 10] -= 1
            temp[bucket[(int(key[i]/esp)) % 10]] = key[i]
        key[0: n] = temp
        esp *= 10


"""
Test
"""
sample = [100,23,1000,555,345,23456]
radixSort(sample)
print(sample)


