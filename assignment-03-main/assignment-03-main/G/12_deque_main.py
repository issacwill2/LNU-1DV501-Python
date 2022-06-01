import Deque as deq

# Program starts
empty = deq.Deque()     # An empty deque
deque = deq.Deque()     # To be filled

# Add 10 integers using add_last and print list content
for i in range(1, 11):
    deque.add_last(i)
print(deque.to_string())
print("Size:", deque.size)

# Add 10 integers using add_first and print list content
for i in range(11, 21):
    deque.add_first(i)
print(deque.to_string())
print("Size:", deque.size)

# Test get_last
print("\nget_last():", deque.get_last())
print("get_last() on empty deque:", empty.get_last())

# Test get_first
print("\nget_first():", deque.get_first())
print("get_first() on empty deque:", empty.get_first())

# Test remove_first
print("\nremove_first():", deque.remove_first())
print("remove_first() on empty deque:", empty.remove_first())

# Test remove_last
print("\nremove_last():", deque.remove_last())
print("remove_last() on empty deque:", empty.remove_last())

print(deque.to_string())
print("Size:", deque.size)

# Test add and remove all
print("\nTest to remove all elements")
temp = deq.Deque()
for i in range(100, 106):
    temp.add_first(i)
print("After adding elements:", temp.to_string())
while temp.size > 0:
    temp.remove_last()
print("After removing all elements:", temp.to_string())
print("Size:", temp.size)

# OUTPUT
'''
{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
Size: 10
{ 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
Size: 20

get_last(): 10
You can't access an empty queue
get_last() on empty deque: None

get_first(): 20
You can't access an empty queue
get_first() on empty deque: None

remove_first(): 20
You can't access an empty queue
remove_first() on empty deque: None

remove_last(): 10
You can't access an empty queue
remove_last() on empty deque: None
{ 19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
Size: 18

Test to remove all elements
After adding elements: { 105, 104, 103, 102, 101, 100 }
After removing all elements: {  }
Size: 0
'''
