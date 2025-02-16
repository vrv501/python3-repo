def bubble_sort(inp_list):
	"""
	Space: O(1)
	Time: O(N^2)
	"""
	list_len = len(inp_list)
	for i in range(list_len-1, -1, -1):
		sorted = True
		for j in range(0, i):
			if inp_list[j] > inp_list[j+1]:
				inp_list[j], inp_list[j+1] = inp_list[j+1],inp_list[j]
				sorted = False 
		if sorted:
			break
	return inp_list

def selection_sort(inp_list):
	"""
	Space: O(1)
	Time: O(N^2)
	"""
	list_len = len(inp_list)
	for i in range(0, list_len):
		min_ind = i
		for j in range(i+1, list_len):
			if inp_list[j] < inp_list[min_ind]:
				min_ind = j 
		inp_list[i],inp_list[min_ind] = inp_list[min_ind],inp_list[i]
	return inp_list

def insertion_sort(inp_list):
	"""
	Space: O(1)
	Time: O(N^2)
	"""
	list_len = len(inp_list)
	for i in range(1, list_len):
		j = i-1
		while inp_list[j] > inp_list[j+1] and j > 0:
			inp_list[j+1], inp_list[j] = inp_list[j], inp_list[j+1]
			j-=1
	return inp_list

def merge_sort(inp_list):
	"""
	Space: O(N)
	Time: O(NlogN)
	"""
	def merge(left, right):
		i, j = 0, 0
		c = []
		left_len = len(left)
		right_len = len(right)
		while i < left_len and j < right_len:
			if left[i] < right[j]:
				c.append(left[i])
				i+=1 
			else: 
				c.append(right[j])
				j+=1
		while i < left_len:
			c.append(left[i])
			i+=1 
		while j < right_len:
			c.append(right[j])
			j+=1 
		return c
	
	def _merge_sort(inp_list):
		list_len = len(inp_list)
		if list_len == 1:
			return inp_list
		mid = (list_len)//2
		left = _merge_sort(inp_list[0:mid])
		right = _merge_sort(inp_list[mid:])
		return merge(left, right)

	return _merge_sort(inp_list)

def quick_sort(inp_list):
	"""
	Space: O(N)
	Time: O(N^2)
	"""

	def pivot(inp_list, pivot, end):
		swap = pivot 
		for i in range(pivot+1, end+1):
			if inp_list[i] < inp_list[pivot]:
				swap += 1
				inp_list[i], inp_list[swap] = inp_list[swap], inp_list[i]
		
		inp_list[pivot], inp_list[swap] = inp_list[swap], inp_list[pivot]
		return swap

	def _quick_sort(inp_list, left, right):
		if left < right:
			pi_ind = pivot(inp_list, left, right)
			_quick_sort(inp_list, left, pi_ind-1)
			_quick_sort(inp_list, pi_ind+1, right)
		return inp_list

	return _quick_sort(inp_list, 0, len(inp_list)-1)
		


print(bubble_sort([5,3,4,2,1]))
print(insertion_sort([5,3,4,2,1]))
print(merge_sort([5,3,4,2,1]))
print(quick_sort([5,3,4,2,1]))

