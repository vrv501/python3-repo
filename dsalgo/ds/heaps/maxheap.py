class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        lenh = len(self.heap)
        curr_index = lenh - 1
        while curr_index > 0:
            parent_ind = self._parent(curr_index)
            if self.heap[parent_ind] < value:
                self._swap(parent_ind, curr_index)
                curr_index = parent_ind
                continue
            break
    
    def _sink_down(self, index):
        lenh = len(self.heap)

        while index < lenh:
            lc_ind = self._left_child(index)
            if lc_ind >= lenh:
                break
            rc_ind = self._right_child(index)
            max_ind = lc_ind
            if rc_ind < lenh and self.heap[rc_ind] > self.heap[lc_ind]:           
                max_ind = rc_ind

            if self.heap[max_ind] > self.heap[index]:
                self._swap(max_ind, index)
                index = max_ind
                continue 
            break
    
    def remove(self):
        try:
            rr = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self._sink_down(0)
            return rr
        except IndexError:
            return None
        


    
    
    
myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)


myheap.remove()

print(myheap.heap)


myheap.remove()

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]

"""
    