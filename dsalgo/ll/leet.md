## Linked List patterns
### Two-pointer approach
- One slow ptr which moves one step at a time. One fast pointer which initially or after moves k steps at a time
- slow_ptr and fast_ptr init at head

1. [Find mid value](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=problem-list-v2&envId=linked-list): slow_ptr moves one step. fast_ptr moves 2 steps. By the time, fast_ptr is at the end(odd length) or after-end(even length), slow_ptr is at mid
2. [Check loop](https://leetcode.com/problems/linked-list-cycle/?envType=problem-list-v2&envId=linked-list): slow_ptr moves one step. fast_ptr moves 2 steps. If fast_ptr is None, no loop. If after some steps fast_ptr == slow_ptr, loop detected
3. [Kth value from end](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=linked-list): slow_ptr and fast_ptr init at head. move fast_ptr by k values. Then from now on move slow & fast_ptr by one step until fast_ptr is at the end(not after end). slow_ptr should be at the result. IDEA is to have k places gap b/w slow & fast ptr
3. [Rotate right by k steps](https://leetcode.com/problems/rotate-list/?envType=problem-list-v2&envId=linked-list): First find ll length and ll tail. Then normalise k by % with n. This is bcoz rotations are circular. `k = k % n`. Then new head is at (n-k)thpos and tail is (n-k-1). head will updated to n-k, tail's next will be old-head. new_tail's next pos will be None
4. [Reverse](https://leetcode.com/problems/reverse-linked-list/description/?envType=problem-list-v2&envId=linked-list): use 3 ptr's. as you are doing single pass keep swapping next pte's. Finally update head & tail
5. [Binary to decimal]: simple steps. as we are passing from left to right in binary, init empty var to 0, then empty var = empty_var*2 + curr.value. Reason why we use 2 is in binary base is 2 and addition is done in decimal because we want decimal to be returned