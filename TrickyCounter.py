my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
    counter = counter + item

print(counter)

for i,char in enumerate(list(range(1,100))):
    if char == 50:
        print(i)