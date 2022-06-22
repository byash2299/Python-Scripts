from collections import Counter, defaultdict

new_dict = defaultdict(lambda : 'not present')
new_dict['a'] = 1
new_dict['b'] = 2

print(new_dict['c'])

sentence = '''Heyy there, 
let me tell you something about my dog,
His name is Baggu and he is black in color'''

c = Counter(sentence)
print(c)