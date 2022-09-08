from dataclasses import replace
from queue import PriorityQueue


S1 = "American"
S2 = "Japan"
print(S1[0]+S2[0:3]+S2[-1])
print('"Tuan"')
Mid = S1[len(S1)//2 -1 : len(S1)+2]
print(S1[2:5])
print("*"*len(S1))
print(S1.replace(S1[0],"abc",1))
print("abc"+S1[1:])
a =int(5) 
b = int(6) 
print(S1[:a]+" "*b+S1[a:])