some_list = ['a', 'b', 'c', 'b', 'f', 'b', 'n', 'd', 'a' ,'d']
duplicate = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in duplicate:
          duplicate.append(i)

print(duplicate)
