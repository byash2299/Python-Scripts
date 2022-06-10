from datetime import date

birth_year = input('What year you were born?')
current_year = date.today().year
age = current_year - int(birth_year) # convert birth_year type from string to int
print(f'You are {age} years old')