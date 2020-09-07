l = []
number = int(input("Enter no. of Elements : "))
for i in range(number):
    value = int(input("Enter Elements :  "))
    l.append(value)

still_swapping = True

while still_swapping:
    still_swapping = False
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
            still_swapping = True

print("Array",l)                      