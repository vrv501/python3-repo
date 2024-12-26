class Node:
    def __init__(self, val):
        self.value = val 
        self.next = None
        
class Stack:
    '''
    LIFO
    Worst Time Complexities:
        Prepend: O(1)
        Pop: O(1)
        Search: O(N) 
    '''
    def __init__(self, val):
        node = Node(val)
        self.top = node 
        self.height = 1
    
    def push(self, val):
        node = Node(val)
        self.height += 1
        if self.height == 1:
            self.top = node 
        else:
            node.next = self.top
            self.top = node
    
    def pop(self):
        if self.height == 0:
            return None 
        
        rm_node = self.top 
        self.top = self.top.next 
        self.height -= 1
        return rm_node








my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)



"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""