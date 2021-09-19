
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# mo ta cau truc stack
class Stack:
    """
    Mô tả cấu trúc Stack
    """
    def __init__(self):
        self.top = None
        self.size = 0

     # ham kiem tra stack co trong hay khong
    def isEmpty(self):
        return self.size == 0

    # ham them phan tu vao stack
    def push(self,data):
        newNode = Node(data)
        if self.isEmpty() :
            self.top = newNode
            self.size += 1
            return
        newNode.next = self.top
        self.top = newNode
        self.size +=1

    #ham xoa phan tu khoi stack va tra ve gia tri
    def pop(self):
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    # in ra stack
    def printS(self):
        curNode = self.top
        while curNode is not None:
            print(curNode.data, end = ', ')
            curNode = curNode.next



