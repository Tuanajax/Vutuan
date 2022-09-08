# Conditional statement:
a = input("Enter my_birthyear:")
if 2022 - int(a) >= 18:
    print("ok, pass")
else:
    print("Stop")
a = input("Enter my password:")
print(len(a)*"*")
b = input("Re-enter my_password:")
if a == b:
    print("correct")
else:
    print("Incorect")

# upper: string-in case "caplock"
a = input("Enter my_birthyear:")
if 2022 - int(a) >= 18:
    sex = input("Enter my sex:")
    if sex == "Male":
        print("Ok, so strong")
    else:
        print("ok, so beautiful")
else:
    print("get out!")
# Toan tu ba ngoi 
from operator import and_
a = float(input("Enter average:"))
if a>=8:
    print("Ex")
elif a>=7:
    print("K")
elif a>=5:
    print("TB")   
else: 
   print("Y")
#
num = input("Enter number:")
leng_num = len(num)
if int(num)%2==0:
    print("even number")
else:
    print("odd number")
    
if num[0]==num[len(num)-1]:
    print("Nice number")
else:
    print("Bad number")
# 
from curses.ascii import isupper
from dataclasses import is_dataclass
import numbers


Tu_str = input("Enter String: ")
if Tu_str[0].isupper() == "True"
    print("valid string")
else:
    print("*"+Tu_str[1:])

# 
Tu_str = input("Enter String: ") 
Tu_x = input("x: ")
if Tu_str.count(Tu_x,0,len(Tu_str)) >=2:
    print(Tu_str.replace(Tu_x,"*"))