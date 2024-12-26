## Stack & Queue Patterns
1. Sort stack implemented using list:   
   ```pseudocode
   # O(N^2)
   buffer = Stack()
   while inp_stack is not empty:
      top = inp_stack.pop()
      while buffer is not empty:
         buf_top = buffer.peek()
         if buf_top is not None and buf_top > top:
            inp_stack.push(buffer.pop())
        else:
            break
      buffer.push(top)

    while buffer is not empty:
       inp_stack.push(buffer.pop())

   ```
