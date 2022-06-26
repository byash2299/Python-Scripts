import re

# myfile = open('test.txt')
# print(myfile.read())
# print("****")
# myfile.seek(0)
# print(myfile.readline())
# myfile.close()


# with open('test.txt',mode='w') as myfile:
#     print(myfile.writelines('hey, just wrote a new line is test file'))

# Regex

pattern = re.compile(r"(^[a-zA-Z0-9$@%#]+)")

password = 'Swift@$%#'

a = pattern.search(password)
print(a)


