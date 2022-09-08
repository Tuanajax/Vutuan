Nu_1, Nu_2 = float(input("Enter number 1:")), float(input("Enter number 2:"))
Selec_oper = input("Select operator:")
if Selec_oper == "+":
    print("result:", Nu_1+Nu_2)
elif Selec_oper == "-" :
    print("result:", Nu_1-Nu_2)
elif Selec_oper == "x" :
    print("result:", Nu_1*Nu_2)
else:
    if(Nu_2==0):
       print("Not excute")
    else:
       print("result:", Nu_1//Nu_2)






    


    
    