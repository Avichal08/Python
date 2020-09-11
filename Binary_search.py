lst = []
size = int(input("Enter size of array "))
for n in range(size):
    number = int(input("Enter Elements "))
    lst.append(number)


x = int(input("Enter number to be searched "))

still_swapping = True

while still_swapping:
    still_swapping = False
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            temp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp
            still_swapping = True

start = 0
end = len(lst) - 1

found = False

while start <= end and not found:
    location = (start + end) // 2
    if lst[location] == x:
        found = True
    else:
        if x < lst[location]:
            end = location - 1

        else :
            start = location + 1


print(found)
print(location)               