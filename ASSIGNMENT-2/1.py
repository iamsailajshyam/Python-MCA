list = ['Audi','BMW','SUZUKI']
print(list)

print (list[1:2])
#LIST VALUE RE ASSIGN
# Define the list
car_list = ['Audi', 'BMW', 'SUZUKI']
print("Original List:", car_list)

# Slicing the list
sliced_list = car_list[1:2]  # This gets the element at index 1 (i.e., 'BMW')
print("Sliced List (Index 1:2):", sliced_list)

# Reassigning list values
car_list[1] = 'Mercedes'  # Change the element at index 1 from 'BMW' to 'Mercedes'
print("Modified List:", car_list)

# Reassigning multiple values using slicing
car_list[1:3] = ['Tesla', 'Ford']  # Change the elements from index 1 to 2
print("List After Slicing Reassignment:", car_list)


tupple = ("HERO","YAHAMA","BAJAJ")
print(tupple)
print (tupple[1:2])
