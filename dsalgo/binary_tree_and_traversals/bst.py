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
    
    def __r_contains(self, node, value):
        if node is None:
            return False 
        elif node.value == value:
            return True 
        elif node.value > value:
            return self.__r_contains(node.left, value)
        else:
            return self.__r_contains(node.right, value)


    def r_contains(self, val):
        return self.__r_contains(self.root, val)

    def __r_insert(self, node, val):
        if node.value == val:
            return False 
        elif node.value > val:
            if node.left is not None:
                return self.__r_insert(node.left, val)
            node.left = Node(val)
        else:
            if node.right is not None:
                return self.__r_insert(node.right, val)
            node.right = Node(val)
        return True
    
    def r_insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return True

        return self.__r_insert(self.root, val)

    def __delete_node(self, node, val):
        if node is None:
            return None
        elif node.value == val:
            if node.left is not None and node.right is not None:
                prev = None
                curr = node.right
                while curr.left is not None:
                    prev = curr
                    curr = curr.left
                if prev is not None:
                    prev.left = curr.right
                curr.left = node.left
                curr.right = node.right
                return curr
            elif node.left is None and node.right is None:
                return None 
            elif node.left is None:
                return node.right
            else:
                return node.left 
        elif node.value > val:
            node.left = self.__delete_node(node.left, val)
            return node
        else:
            node.right = self.__delete_node(node.right, val)
            return node
    
    def delete_node(self, val):
        if self.root is None:
            return
        self.root = self.__delete_node(self.root, val)
    
    def BFS(self):
        q = [self.root]
        r = []
        while q != []:
            rm = q.pop(0)
            r.append(rm.value)
            if rm.left is not None:
                q.append(rm.left)
            if rm.right is not None:
                q.append(rm.right)
        return r
    
    def dfs_pre_order(self):
        r = []
        def traverse(node):
            r.append(node.value)
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
        traverse(self.root)
        return r 
    
    def dfs_post_order(self):
        r = []
        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            r.append(node.value)
        traverse(self.root)    
        return r 

    def dfs_in_order(self):
        r = []
        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            r.append(node.value)
            if node.right is not None:
                traverse(node.right)
            
        traverse(self.root)
        return r 

    def __kth_smallest(self, node, index):
        if node is None:
            return None 
        
        l_child = self.__kth_smallest(node.left, index)
        if l_child is not None:
            return l_child
        
        self.count += 1
        if self.count == index:
            return node.value

        r_child = self.__kth_smallest(node.right, index)
        if r_child is not None:
            return r_child 
        
        return None
    
    def kth_smallest(self, index):
        if self.root is None or index < 0:
            return None
    
        self.count = 0
        return self.__kth_smallest(self.root, index)

