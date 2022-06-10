even = []
def highest_even(li):
    for item in li:
        if item % 2 == 0:
            even.append(item)
    return max(even)
print(highest_even([10, 3, 5, 7, 9, 11, 4, 80]))
