class Dog():
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age
        self.mydict = {
            'name': 'baggu',
            'color': 'black'
        }

# modified some pre built dunder methods
    def __str__(self):
        return self.breed

    def __len__(self):
        return 5

    def __getitem__(self, i):
        return self.mydict[i]

baggu = Dog('mix',1)

print(baggu.__str__())
print(baggu.__len__())
print(baggu['color'])