class Node:
    def __init__(self, val):
        self.value = val 
        self.left = None 
        self.right = None 

class BinarySearchTree:
    """
    insert, lookup, remove are all O(n) if there are no left childs but ideally we would have some children, so for the above operations its O(logn)
    """
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node 
            return True
        
        curr = self.root 
        prev = None
        while curr is not None:
            prev = curr
            if curr.value == val:
                return False
            elif curr.value > val:
                curr = curr.left
            else:
                curr = curr.right
        
        if prev.value > val:
            prev.left = node 
        else:
            prev.right = node
        return True 

    def contains(self, val):
        curr = self.root 
        while curr is not None:
            if curr.value == val:
                return True 
            elif curr.value > val:
                curr = curr.left 
            else:
                curr = curr.right 
        
        return False
