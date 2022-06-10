from operator import truediv


is_magician = False
is_expert = True

if is_magician and is_expert:
    print('You are a master magician')
elif is_magician and not is_expert:
    print('at least you are getting there')
elif not is_magician:
    print('You need magic powers')
