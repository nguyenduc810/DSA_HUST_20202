# author: Nguyen Duc
from TheStack import Stack
"""
Mô tả cây biểu thức
"""

# Mô tả cây nhị phân
class ExpTree :
    def __init__(self, data, left = None , right = None):
        self.data = data
        self.leftChild = left
        self.rightChild = right
    # Hàm xem node đang xét có phải là lá hay không
    def isLeaf(self,node):
        return node.leftChild is None and node.rightChild is None

# Hàm đưa biểu thức vào trong cây nhị phân
def construct(exp):
    s = Stack()
    for i in exp: # Duyệt từng kí tự trong xâu
        if i in '+-*/' :
            s.push(i)
        elif i not in '()':    # Nếu là toán hạng thì tạo cây con và đưa vào Stack
            tmpTree = ExpTree(i)
            s.push(tmpTree)
        elif i == ')':         # Nếu gặp dấu ")" thì lấy ra khỏi stack 3 giá trị tạo thành 1 cây con
            right = s.pop()
            operator = s.pop()
            left = s.pop()
            tmpTree = ExpTree(operator, left , right)
            s.push(tmpTree)
    right = s.pop()
    operator = s.pop()
    left = s.pop()
    root = ExpTree(operator, left , right)
    return root

# Duyệt cây theo thứ tự giữa
def inOrderTraversal(root):
    if root is not None:
        if not root.isLeaf(root):
            print('(' , end = ' ')
        inOrderTraversal(root.leftChild)
        print(root.data , end = ' ')
        inOrderTraversal(root.rightChild)
        if not root.isLeaf(root) :
            print(')' ,end = ' ')
def compute(operator, leftOperand , rightOperand):
    if operator == '+' :
        return float(leftOperand + rightOperand)
    elif operator == '-':
        return float(leftOperand - rightOperand)
    elif operator == '/' :
        return float(leftOperand/rightOperand)
    else:
        return float(leftOperand* rightOperand)
def calculateExpression(expTree):
    if expTree.isLeaf(expTree):
        return float(expTree.data)
    operator = expTree.data
    if expTree.leftChild.isLeaf(expTree.leftChild):
        leftOperand = float(expTree.leftChild.data)
    else:
        leftOperand = calculateExpression(expTree.leftChild)
    if expTree.rightChild.isLeaf(expTree.rightChild):
        rightOperand = float(expTree.rightChild.data)
    else:
        rightOperand = calculateExpression(expTree.rightChild)
    return compute(operator, leftOperand,rightOperand)

# xâu đầu vào phải có đử dấu ngoặc, kể cả các phép nhân, chia
t = construct('(((2+3)*2)*2)+2')
print(calculateExpression(t))
inOrderTraversal(t)