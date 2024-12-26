- In a **binary tree**, each node has one parent and each parent node can point to atmost one node
- A binary tree is said to be **full** if each points to zero or two nodes
- A binary tree is said to be **perfect** if all nodes except last **level** have two child nodes
- For perfect binary tree if theare are N levels, then there are 2^N - 1 nodes
- A **binary search tree**(divide & conquer) is special binary tree where each node's left child is less than  or equal its current value and right child is greater than curr value
- When **deleting a node from bst**, remember 3 things:   
  ```
  - If curr_node is None, return None
  - if curr_node.value > val: traverse left sub tree, similarly for else case, traverse right sub tree
  - if curr_node.value == val, there are 4 sub-cases:
       - if both children are None, return None
       - if one of them is None return the other one which is not None
       - if both are not None, then set curr to right child, then traverse left sub tree of right child until
         you find its left leaf node. Now set this node's right tree to curr_node's right child and left child to curr_node left child
       - finally delete the left subtree leaf node of curr_node's right child 
  ```
- in breadth first search(**BFS**) we print curr node value, left child & right child and then move down. Essentially we print level wise from left to right
  - useful for finding shortest path in unweighted graphs
- In depth first search(**DFS**) there are 3 types:
  - preOredr: print curr value, then keep printing all left childs until we encounter None, then for each left child start prinintg right children. Finally traverse right subtree in similar fashion. Useful for prefix notation (curr, all left, right)
  - postOrder: Useful for postfix notation(left, right and then root)
  - inorder: increasing order of tree values. useful to check validity of bst (left, root, right)
  