class MinHeap:
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
        index = lenh - 1
        while index > 0:
            p_ind = self._parent(index)
            if self.heap[p_ind] > value:
                self._swap(p_ind, index)
                index = p_ind 
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
            self.heap.pop()
            self._sink_down(0)
            return rr
        except IndexError:
            return None


 
 
myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)

print(myheap.heap)  # [6, 8, 10, 12]

myheap.insert(4)

print(myheap.heap)  # [4, 6, 10, 12, 8]

myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]


"""
    EXPECTED OUTPUT:
    ----------------
    [6, 8, 10, 12]
    [4, 6, 10, 12, 8]
    [2, 6, 4, 12, 8, 10]

"""
