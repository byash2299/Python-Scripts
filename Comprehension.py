# list, set, dictionary

my_list = [num for num in range(1,11)]
print(my_list)

new_list = [x**2 for x in range(1,12) if x % 2 != 0]
print(new_list)

# Set comprehension is same as list comprehension
# only difference is it scores unique values

some_dict = {
    'a': 11,
    'b': 22
}

new_dict = {key:value**4 for key,value in some_dict.items()}
print(new_dict)

more_dict = {key:key**2 for key in [1,2,3]}
print(more_dict)