a= input("Enter number: ")
i = 0
j = 1
x = 2
b = 0
while x <len(a):
    if abs(int(a[i])-int(a[x])) >=int(a[j]) and (int(a[x]) != int(a[j])) and (int(a[i])<=int(a[j])): 
        b = b + abs(abs(int(a[i])-int(a[x]))- int(a[j])) + 1 
    else:
        b = b + 0                                                                                                                
    j+=1
    i+=1
    x+=1                                                                        
print(b)