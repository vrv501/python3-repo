class Node:
    def __init__(self, value) -> None:
        self.value = value 
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
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self) -> None:
        print("LinkedList Length:", self.length)
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value) -> None:
        new_node = Node(value)
        self.length += 1

        # Appending to empty ll
        if self.length == 1:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def pop(self) -> Node:
        if self.length == 0:
            return None

        prev = None
        curr = self.head
        # Get node prev to tail
        while curr.next is not None:
            prev = curr 
            curr = curr.next
        
        # Removing the only node in ll
        if prev is None:
            self.head = None 
            self.tail = None 
            self.length = 0
            return curr 

        self.tail = prev
        prev.next = None 
        self.length -= 1
        return curr

    def prepend(self, value) -> None:
        new_node = Node(value)
        self.length += 1

        # Prepending to empty ll
        if self.length == 1:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop_first(self) -> Node:
        if self.length == 0:
            return None
        
        curr = self.head
        self.length -= 1
        self.head = curr.next
        if self.length == 0:
            self.tail = None 
        return curr
    
    def get(self, index) -> Node:
        if index < 0 or index > self.length:
            return None
        
        curr = self.head 
        while index != 0:
            curr = curr.next
            index -= 1
        return curr

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
    
    def reverse(self) -> None:
        if self.length == 0:
            return
        
        # swap tail & head
        curr = self.head 
        self.head = self.tail 
        self.tail = curr 

        prev = None 
        next = curr.next

        while curr is not None:
            curr.next = prev 
            prev = curr 
            curr = next 
            if next is not None:
                next = next.next

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
