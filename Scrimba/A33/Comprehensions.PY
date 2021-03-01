numbers = [1,2,3,4,5,6,7,8,9]
# give me a list with num squared for each num in numbers
new_list = []
for i in numbers:
    new_list.append(i*i)
print(new_list)


new_list = [num for num in numbers if num % 2 == 0]

print(new_list)

new_list = filter(lambda num : num % 2 == 0, numbers)


