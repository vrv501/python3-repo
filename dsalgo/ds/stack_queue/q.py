class Node:
    def __init__(self, val):
        self.value = val 
        self.next = None 
        
class Queue:
    '''
    FIFO
    Worst Time Complexities:
        Append: O(1)
        Pop: O(1)
        Search: O(N) 
    '''
        
    def __init__(self, val) -> None:
        node = Node(val)
        self.first = node 
        self.last = node
        self.length = 1
    
    def enqueue(self, val):
        node = Node(val)
        self.length += 1
        if self.length == 1:
            self.first = node 
            self.last = node 
        else:
            self.last.next = node
            self.last = node
    
    def dequeue(self):
        if self.length == 0:
            return None 
        
        rm_node = self.first 
        self.first = self.first.next 
        self.length -= 1
        if self.length == 0:
            self.last = self.first
        return rm_node
