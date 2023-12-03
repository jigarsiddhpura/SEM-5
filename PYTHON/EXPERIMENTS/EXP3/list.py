# append()-appends element to list
print("append() function")
list1 = [10, 20, 30]
print("Original list:", list1)
list1.append(50)
print("List After Appending 50:", list1)
# extend()- extends by adding on with new list
print("extend() function")
list1 = [10, 20, 30]
print("Original list:", list1)
list2 = [222, 333]
list1.extend(list2)
print("After extending to list2, the original list is : ", list1)
# insert() – inserts element at particular location
print("insert() function")
list1 = [10, 20, 30]
print("Original list:", list1)
list1.insert(2, 15)
print("List After Appending 15:", list1)
# pop()- pops element from list
print("pop() function")
list1 = [10, 20, 30]
print("Original list:", list1)
list1.pop(2)
print("List after poping from index 2:", list1)
# copy()-copies a list
print("copy() function")
list1 = [10, 20, 30]
print("Original list:", list1)
list2 = list1.copy()
print("Copied list is:", list2)
# clear()-clears the list
print("Clear() function")
list1 = [10, 20, 30]
print("Original list:", list1)
list2 = list1.clear()
print("List after clearing:", list2)