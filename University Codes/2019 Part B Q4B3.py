inList = input("Enter the elements in L: ")
L = [int(x) for x in inList.split()]
K = int(input("Enter K: "))
M = 100
for i in L:
    if i > K:
        if i < M:
            M = i
print (M)
