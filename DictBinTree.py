class BinNode:
    def __init__(self, k):
        self.key = k  
        self.left = None  
        self.right = None  

class DictBinTree:
    def __init__(self):
        self.root = None

    def insert(self, k):
        z = BinNode(k)
        x = self.root  
        y = None 
        while x != None: 
            y = x  
            if z.key < x.key:
                x = x.left  
            else:
                x = x.right  
        z.p = y  
        if y == None:
            self.root = z  
        elif z.key < y.key:
            y.left = z  
        else:
            y.right = z  

    def search(self, k):
        return self._search(self.root, k) is not None

    def _search(self, x, k):
        while x != None and k != x.key:
            if k < x.key:
                x = x.left  
            else:
                x = x.right  
        return x  

    def orderedTraversal(self):
        result = []  
        self._inorder(self.root, result)  
        return result  

    def _inorder(self, x, result):
        if x != None: 
            self._inorder(x.left, result) 
            result.append(x.key) 
            self._inorder(x.right, result)  
