class Node:
    def __init__(self, data, parent = None , left = None, right = None ):
        self.data = data
        self.parent = parent
        self.leftChild = left
        self.rightChild = right
        self.isLeft = None
        self.isRight = None
class Height:
    def __init__(self):
        self.height = 0
class BinaryTree:
    def __init__(self, data = None):
        if data is not None:
            self.root = Node(data)
        else:
            self.root = None
    def insert(self,_root, data):
        if self.root is None:
            newNode = Node(data)
            self.root = newNode
            return
        if _root.data == data:
            print('Giá trị đã tồn tại!')
            return
        if _root.data > data:
            if _root.leftChild is None:
                newNode = Node(data,_root)
                newNode.isLeft = 1
                _root.leftChild = newNode
            else:
                self.insert(_root.leftChild, data)
        else:
            if _root.rightChild is None:
                newNode = Node(data,_root)
                newNode.isRight = 1
                _root.rightChild = newNode
            else:
                self.insert(_root.rightChild, data)
    def isLeaf(self,_root):
        return _root.leftChild is None and _root.rightChild is None

    #tìm nút trái nhất
    def findLeftMost(self, _root):
        if _root.leftChild is None:
            return _root
        if _root.leftChild is not None:
            return self.findLeftMost(_root.leftChild)
    def deleteNode(self,_root , data):
        if _root.data == data:
            if self.isLeaf(_root):   # Nếu nút là lá
                _root = None
                return
            if _root.leftChild is not None and _root.rightChild is None:  # Nếu nút có 1 con
                if _root.isRight is not None:
                    _root.parent.rightChild = _root.leftChild
                elif _root.isLeft is not None:
                    _root.parent.leftChild = _root.leftChild
                return
            if _root.leftChild is None and _root.rightChild is not None:
                if _root.isRight is not None:
                    _root.parent.rightChild = _root.rightChild
                elif _root.isLeft is not None:
                    _root.parent.leftChild = _root.rightChild
                return
            # trường hợp có 2 con
            node = self.findLeftMost(_root.rightChild)
            _root.data = node.data
            self.deleteNode(_root.rightChild , data)
        elif _root.data > data:
            self.deleteNode(_root.leftChild , data)
        else:
            self.deleteNode(_root.rightChild , data)

    def inOrderTraversal(self,root):
        if root is not None:
            self.inOrderTraversal(root.leftChild)
            print(root.data, end=', ')
            self.inOrderTraversal(root.rightChild)

    # Hàm tính chiều cao cây
    def hight(self, _root):
        if _root is None:
            return 0
        return 1+ max(self.hight(_root.leftChild), self.hight(_root.rightChild))
    '''
    Viết hàm kiểm tra cây cân bằng
    Kiểm tra hiệu của 2 cây con tại mỗi thời điểm 
    nếu ổn thì đệ quy tiếp cho từng nhánh con
    '''
    def checkAVL(self,_root):
        if _root is None:
            return True
        '''if abs(self.hight(_root.leftChild) - self.hight(_root.rightChild)) > 1:
            return False
        elif self.checkAVL(_root.leftChild) and self.checkAVL(_root.rightChild):
            return True
        return False '''
        return self.checkAVL(_root.leftChild) and self.checkAVL(_root.rightChild) and abs(self.hight(_root.leftChild) - self.hight(_root.rightChild)) <= 1

    def isBalanced(self,root):

        # lh and rh to store height of
        # left and right subtree
        lh = Height()
        rh = Height()

        # Base condition when tree is
        # empty return true
        if root is None:
            return True

        # l and r are used to check if left
        # and right subtree are balanced
        l = self.isBalanced(root.leftChild)
        r = self.isBalanced(root.rightChild)

        # height of tree is maximum of
        # left subtree height and
        # right subtree height plus 1

        if abs(lh.height - rh.height) <= 1:
            return l and r

        # if we reach here then the tree
        # is not balanced
        return False
#lt = rd.sample(range(5),5)
bTree = BinaryTree()
#size = len(lt)
#for i in range(size):
#    bTree.insert(bTree.root, lt[i])
bTree.insert(bTree.root,1)
bTree.insert(bTree.root,2)
bTree.insert(bTree.root,3)
bTree.insert(bTree.root,4)
bTree.insert(bTree.root,5)
bTree.insert(bTree.root,6)
bTree.insert(bTree.root,7)
bTree.inOrderTraversal(bTree.root)
print('\nHight of binary tree: ', bTree.hight(bTree.root))
if bTree.checkAVL(bTree.root):
    print('Là cây AVL')
else:
    print('Không là cây AVL')