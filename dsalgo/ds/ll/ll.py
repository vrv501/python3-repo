class Node:
    def __init__(self, val):
        self.value = val 
        self.next = None

    def __str__(self) -> str:
       return f"Value: {self.value}"

class LinkedList:
    '''
    Worst Time Complexities:
        Append: O(1)
        Prepend: O(1)
        Insert at index: O(N)
        Pop from first: O(1)
        Pop: O(N)
        Remove from index: O(N)
        Search: O(N) 
    '''
    def __init__(self, val):
        self.head = Node(val)
        self.tail = self.head 
        self.length = 1
    
    def print_list(self):
        tmp = self.head 
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next
    
    def append(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = self.head 
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None 
            
        node = self.tail 
        self.length -= 1
        
        if self.length == 0:
            self.head = None 
            self.tail = self.head
        else: 
            prev = None 
            curr = self.head 
            while curr.next is not None:
                prev = curr 
                curr = curr.next 
            prev.next = None 
            self.tail = prev
        return node 

    def prepend(self, val):
        new_node = Node(val)
        self.length += 1 
        if self.length == 1:
            self.head = new_node 
            self.tail = self.head 
        else:
            new_node.next = self.head 
            self.head = new_node

    def pop_first(self):
        if self.length == 0:
            return None 
        
        node = self.head 
        self.length -= 1 
        if self.length == 0:
            self.head = None 
            self.tail = self.head 
        else:
            self.head = self.head.next 
        
        node.next = None
        return node 
    
    def get(self, ind):
        if ind < 0 or ind > self.length:
            return None 
        
        tmp = self.head 
        while ind != 0:
            tmp = tmp.next 
            ind -= 1 
        
        return tmp

    def set_value(self, index, value) -> bool:
        node = self.get(index)
        if node is None:
            return False
        
        node.value = value
        return True

    def insert(self, index, value) -> bool:
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            prev_node = self.get(index-1)
            if prev_node is None:
                return False
            curr_node = prev_node.next
            if curr_node is None:
                return False
            new_node = Node(value)
            prev_node.next = new_node
            new_node.next = curr_node
            self.length += 1
        return True

    def remove(self, index) -> Node:
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev_node = self.get(index-1)
            if prev_node is None:
                return None 
            curr_node = prev_node.next
            if curr_node is None:
                return None 
            prev_node.next = curr_node.next
            curr_node.next = None 
            self.length -= 1
            return curr_node
    
    def reverse(self):
        if self.head is None or self.head.next is None:
            return 
        
        tmp = self.head 
        self.head = self.tail 
        self.tail = tmp 
        
        prev = None 
        curr = self.tail 
        while curr.next is not None:
            f = curr.next 
            curr.next = prev 
            prev = curr 
            curr = f 
            f = f.next
        
        curr.next = prev

new_ll = LinkedList(1)
new_ll.append(2)
new_ll.append(4)
new_ll.append(6)
new_ll.append(8)
new_ll.append(9)
new_ll.print_list()
print("popping from last", new_ll.pop())
new_ll.print_list()
print("popping from first", new_ll.pop_first())
new_ll.print_list()
print("get at index: 1", new_ll.get(1))
print("get at index: 3", new_ll.get(3))
print("get at index: -1", new_ll.get(-1))
print("get at index: 200", new_ll.get(200))
print("set at index: 1", new_ll.set_value(1, 40))
print("set at index: 3", new_ll.set_value(3, 90))
new_ll.print_list()
print("set at index: -1", new_ll.set_value(-1, 40))
print("set at index: 400", new_ll.set_value(100, 40))
print("insert at index: 1", new_ll.insert(1, 56))
print("insert at index: 3", new_ll.insert(3, 64))
new_ll.print_list()
print("insert at index: -1", new_ll.insert(-1, 56))
print("insert at index: 100", new_ll.insert(100, 56))
print("remove at index: 1", new_ll.remove(1))
new_ll.print_list()
print("remove at index: 3", new_ll.remove(3))
new_ll.print_list()
print("remove at index: -1", new_ll.remove(-1))
print("remove at index: 100", new_ll.remove(100))
new_ll.reverse()
new_ll.print_list()
