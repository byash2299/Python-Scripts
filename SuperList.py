class SuperList(list):
    def __init__(self):
       pass
    def __len__(self):
        return 100

superlist1 = SuperList()
superlist1.append(10)

print(superlist1[0])
