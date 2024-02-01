## Basic Data-Types
int - Numbers  
float - floating numbers  
str - strings, characters. Strings are immutable(but concatenated), indexable and slicable  
bool - True, False  
list - ordered mutable collection of non-homogenous data-types. Indexed and slicable `[]`  
tuple - ordered immutable collection of non-homogenous data-types.  Indexed and slicable`()`  
dict - also called hashmap. `{key:value}`. Sets, list, dict **CANNOT** be used as keys  
set - unordered collection of unique non-homogenous data-types. It is mutable. Not indexable and slicable `{1,2}`  
Sets, list, dict **CANNOT** be members of a set as they are not hashable  


Use `type(variable_name)` to get the data-type of var  
Slicing - [start:stop:step]  
Can be positive and negative numbers  

## Rules
Use ALL_CAPS for global vars
Use `_` while connecting words for var names

## Assignment
Assigning a var to a list will point to the same list, which means any modifications to original var will also modify the subsequent var  
So use `deepcopy()` from `copy` pkg when copying and assigning a dup
