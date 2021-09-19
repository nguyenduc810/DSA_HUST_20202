import random as rd

class BTnode:
    def __init__(self,data):
        self.data = data
        self.leftChild  = None
        self.rightChild = None

def construcBT(myList):
    root = BTnode(myList[0]) # tao goc cua cay
    for i in range(1 , len(myList)):
        newNode = BTnode(myList[i]) #tao nut moi
        curNode = root
        while curNode.leftChild is not None and curNode.rightChild is not None :
            direction = rd.randint(0,1)
            if direction == 0 :
                curNode = curNode.leftChild
            else :
                curNode = curNode.rightChild
        if curNode.leftChild is None:
            curNode.leftChild = newNode
        else :
            curNode.rightChild = newNode
    return root

def inOrderTraversal(root):
    if root is not None:
        inOrderTraversal(root.leftChild)
        print(root.data , end = ', ')
        inOrderTraversal(root.rightChild)

#def breadFirstTraversal(root):


sample = [1,2,3]
root = construcBT(sample)
inOrderTraversal(root)

