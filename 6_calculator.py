v1 = int(input("Enter 1st Number : "))
v2 = int(input("Enter 2nd Number : "))
operator = input("Enter operator : ")
result = 0

if operator == "+":
    result = v1 + v2
elif operator == "-" :
    result = v1 - v2
elif operator == "*" :
    result = v1 * v2
elif operator == "/":
    result = v1 / v2
else : 
    result = "Operator is Not Valide"
    
print(result)
    
    