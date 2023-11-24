a = [90, 10, 56, 43,3, 76, 90, 50]
for i in range(len(a)-1):

    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)

