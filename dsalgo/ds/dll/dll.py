class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    '''
    Worst Time Complexities:
        Append: O(1)
        Prepend: O(1)
        Insert at index: O(N)
        Pop from first: O(1)
        Pop: O(1)
        Remove from index: O(N)
        Search: O(N) 
    '''
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        node = Node(value)
        self.length += 1
        if self.length == 1:
            self.head = node 
            self.tail = node
        else:
            node.prev = self.tail 
            self.tail.next = node 
            self.tail = node

    def pop(self):
        if self.length == 0:
            return None 
        self.length -= 1
        rm_node = self.tail

        if self.length == 0:
            self.tail = None 
            self.head = None 
        else:
            self.tail = self.tail.prev
            self.tail.next = None 
            rm_node.prev = None 
        return rm_node
    
    def prepend(self, value):
        node = Node(value)
        self.length += 1
        if self.length == 1:
            self.head = node 
            self.tail = node 
        else:
            node.next = self.head
            self.head.prev = node 
            self.head = node
    
    def pop_first(self):
        if self.length == 0:
            return None 
        
        self.length -= 1
        rm_node = self.head
        if self.length == 0:
            self.head = None 
            self.tail = None 
        else:
            self.head = self.head.next 
            self.head.prev = None 
            rm_node.next = None 
        return rm_node

    def get(self, index):
        if self.length == 0:
            return None 
        
        if index < 0 or index > self.length:
            return None 
        curr = self.head
        while index != 0:
            curr = curr.next 
            index -= 1

        return curr

    def set_value(self, index, val):
        node = self.get(index)
        if node is None:
            return False 
        node.value = val 
        return True

    def insert(self, ind, val):
        if ind == 0:
            self.prepend(val)
        elif ind == self.length :
            self.append(val)
        else:
            node = self.get(ind)
            if node is None:
                return False
            new_node = Node(val)
            new_node.prev = node.prev 
            node.prev.next = new_node
            new_node.next = node 
            node.prev = new_node
        return True

    def remove(self, ind):
        if ind == 0:
            return self.pop_first()
        elif ind == self.length - 1:
            return self.pop()
        else:
            node = self.get(ind)
            if node is not None:
                node.prev.next = node.next 
                node.next.prev = node.prev 
                node.prev = None 
                node.next = None 
            return node
    
    def reverse(self):
        if self.length == 0:
            return 
        
        curr = self.head 
        prev = None
        while curr is not None:
            prev = curr 
            curr = curr.next 
            tmp = prev.next 
            prev.next = prev.prev 
            prev.prev = tmp

        tmp = self.head
        self.head = self.tail 
        self.tail = tmp
    
    def is_palindrome(self):
        if self.length == 0:
            return True 

        curr = self.head 
        curr2 = self.tail 
        for _ in range(self.length // 2):
            if curr.value != curr2.value:
                return False 
            curr = curr.next
            curr2 = curr2.prev

        return True

    def swap_pairs(self):
        new_head = Node(0)
        new_head.next = self.head
        prev = new_head
        fn = self.head
        
        while fn is not None and fn.next is not None:
            sn = fn.next
            fn.next = sn.next
            sn.prev = fn.prev
            fn.prev = sn
            sn.next = fn
            prev.next = sn
            prev = fn
            fn = fn.next
        
        self.head = new_head.next

my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
#my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 
print('my_dll after swap_pairs:')
my_dll.print_list()
        



                

            
            
        

