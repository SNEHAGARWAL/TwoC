lst = []

n = int(input("Enter number of elements "))

for i in range(0,n):
    element = input()
    
    lst.append(element)

print("List is : "+ str(lst))

rep = []

for i in lst:
    if i not in rep:
        rep.append(i)
        
print("List after removing duplicates: " + str(rep))