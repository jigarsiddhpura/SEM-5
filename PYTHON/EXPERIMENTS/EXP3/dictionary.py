dict1 = {'1': 'One','2':'Two','3':'Three'}
print("Original dictionary:", dict1)
# copy()- copies the dictionary
dict2 = dict1.copy()
print("Copied Dictionary :",dict2)
# fromkeys() – gives details from dictionary
seq = ('4', '5', '6')
print("fromkeys() method")
print(dict1.fromkeys(seq, None))
# clear()- clears the dictionary
dict1.clear()
print("clear() function")
print("The dictionary after clearing it:", dict1)