import time
from BTrees.IIBTree import IIBTree

t = IIBTree()
insertion_start_time = time.time()

for i in range(1000):
    t.update({i: 2*i})

insertion_end_time = time.time()

print(f"Insertion time: {round((insertion_end_time-insertion_start_time)*1000,3)} milliseconds")
key = int(input("enter key: "))

search_start_time = time.time()

if t.has_key(key):
    print(t[key])

search_end_time = time.time()
print(f"Search time: {round((insertion_end_time-insertion_start_time)*1000,3)} milliseconds")