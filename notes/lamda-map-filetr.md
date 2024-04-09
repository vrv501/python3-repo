map expects a function name and an iterable as arguments
map fucntion returns the tranformation done on element
Ex: 
```python
def isFunc(element):
    return elemnt*2
list_num = [1,2,3,45]
list(map(isFunc, list_num))
```

filter expects a function name which returns bool and an iterable as arguments
filter returns elemnts present in list which satisfy fun and return True. It doesnt tranform any lements in the ietrable
Ex: 
```python
def isFunc(element):
    return elemnt*2 == 0
list_num = [1,2,3,45]
list(filter(isFunc, list_num))
```

lamda arg: tranformation-on-arg

