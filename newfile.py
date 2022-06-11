def findpos(arr,num):
    pos = False
    for i in range(len(arr)):
        row = arr[i]
        for j in range(len(row)):
            if num(row[j]):
                pos = (i,j)
                break
    return pos

print(findpos(['-1','0','1'],0))