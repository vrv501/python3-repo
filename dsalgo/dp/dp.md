- A problem can be of type dp if it has following porperties: repearting sub-problems. (A problem can be broken down into sub-problems. but those sub-problems can be repeating)
- To avoid computation, we use memoization to store computed values of already calculcated problem
- They also have optimised sub-structure. To achieve a big problem, we go through calculation of smaller subproblems which in turn at the end added together will compute final result
- Ex: 
  ```python3
  # Fibonacci
  def fib(n, m):
    if n in m:
      return m[n]
    if n==0 or n==1:
      return 1 
    m[n] = fib(n-1)+fib(n-2)
    return m[n]

  fib(7, {})

  # Iterative
  def fib(n):
    m = [0,1]
    for i in range(2, n+1):
      m.append(m[i-1]+m[i-2])
  ```