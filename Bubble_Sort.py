l = [5,8,3,1,4]
still_swapping = True

while still_swapping:
    still_swapping = False
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
            still_swapping = True

print(l)                      