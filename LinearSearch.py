lst = []
size = int(input("Enter size of array "))
for n in range(size):
    number = int(input("Enter Elements "))
    lst.append(number)


x = int(input("Enter number to be searched "))

result = -1
 
for i in range(len(lst)):
    if x == lst[i]:
        result = i
        break

    

print(result)             