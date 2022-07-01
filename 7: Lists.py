my_list = ['string', 100, 23.2]  # lists are very flexible; they can hold multiple data types
print(len(my_list))  # returns how many objects are in a list
my_list = ['one', 'two', 'three']
print(my_list[0])  # you can use slicing and indexing with lists
print(my_list[1:])
another_list = ['four', 'five']
print(my_list + another_list)  # you can concatenate lists
new_list = my_list + another_list
new_list[0] = 'ONE ALL CAPS'  # you can mutate lists
print(new_list)
new_list.append('six')  # adds an element to the end of a list
print(new_list)
new_list.append('seven')
print(new_list)
new_list.pop()  # removes an element from the end of a list
print(new_list)
popped_item = new_list.pop()
print(popped_item)
new_list.pop(0)  # pass in an index position to remove an item at that index
print(new_list)
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
print(new_list)
new_list.sort()  # sorts a list
print(new_list)
print(num_list)
num_list.sort()
print(num_list)
num_list.reverse()  # reverses a list
print(num_list)
