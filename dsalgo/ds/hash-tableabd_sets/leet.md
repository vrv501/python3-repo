- Compuite hash of immutable type and store both kv in that address
- hashing is one way
- There are chances where one or more keys can have same hash. Themn its called collision. To address this we either use 
  - seperate-chaining: Chain the keys in same address either by using lists or chaining using ll(preferred)
  - linear probing: If address is already occupied by key, just keep incrementng address until you find one that's not occupied
- lookup, insert, delete is O(1)

- Grouping Anagarms: parse list of words. sort each word and use it as key in dict. Its value will be list of unaltered words.
Finally parsing through values should give you all anagrams
- Finding indexes of contingous sub_array whose sum of elements matches with target:   
  ```pseudocode
  basically idea is if 
    target=9
    1,2,7,6

    1+2=3
    1+2+7=10

    now if we remove 1 from 10 we get target or in other words
    from totalsun if we remove index at which sum was curr-target, we get target, but index should +1 of where we had curr-target as we dont want to include them
  d = {0:-1} # n
  for k, i in enumerate(list1):
    add elemnt to 
    now see if sum_so_far - target is already present in dict
       if so return dict[sum_so_far-dict]+1, k
    add sum_so_far to dict where sum is key and value is curr_index
  ```
- Finding longest subsequence(not continguous) where each value is 1 greater than prev: 
  ```pseudocode
  First remove all duplicates in list by taking set()
  then iterate thru each element and see if there is 1 less element in set, if not continue.
  if found, then add + 1 to curr element and see if its in set loop until no longer found. The count so far will be length of subsequence
  ```