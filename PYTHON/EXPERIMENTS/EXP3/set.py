set1 = {'a','b', 'c', 'd', 'e'}
print("Original set is:", set1)
# add()- adds element to set
set1.add('f')
print("add() function")
print("Set after adding 'f'", set1)
# discard() – discards element from set
set1.discard('e')
print("discard() function")
print("Set after discarding/Updating 'e': ",set1)
# remove() – removes element from set
set1.remove('a')
print("remove() function")
print("Set after removing 'a':", set1)
# pop()- pops element from the set
set1.pop()
print("pop() function")
print("Set after poping elements:", set1)
# clear()-clears the set
set1.clear()
print("clear() function")
print("Set after clearing:",set1)