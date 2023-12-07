#---------- Task 1 Swaping 2 value -----------------
# a = 15
# b = 5

# a,b = b,a

# print(a)
# print(b)

#---------- Task 2 value -----------------
# uservalue = int(input())  #0 , 1  ==  1  , 0

# uservalue =  1-uservalue  #  1 - 1  = 0

# print(uservalue)



#---------- task 3 value -----------------
# v1 = int(input("Enter 1st value : "))
# operator = input("Enter Your Operators : ")
# v2 = int(input("Enter 2nd value : "))

# result = 0

# if operator == '+':
#     result = "Addition : ", v1+v2

# if operator == '-':
#     result =  "Substriction : " ,  (v1-v2)
    
# if operator == '*':
#     result =  "Multiplication : " , (v1*v2)
    

# if operator == '/':
#     result =  "Division : " , (v1/v2)
    

# if operator == '%':
#     result = "Reminder : " , (v1%v2)
        
# print("Result : " , result)


#---------- task 4 Marksheet -----------------
roleNo = int(input("Enter roll number : "))
name = input("Enter Your Name : ")
Peshtoo = int(input("Enter Peshtoo Marks  1 to 100 : "))
Urdu = int(input("Enter Urdu Marks  1 to 100 : "))  
Arbic = int(input("Enter Arbic Marks  1 to 100 : "))
Sindhi = int(input("Enter Sindhi Marks  1 to 100 : "))

TotalMarks = 400
obtainMarks = Peshtoo + Urdu + Arbic + Sindhi

print("Hello : " ,name)
print("Your roll # : " , roleNo)
print("Your Total Marks : ", TotalMarks)
print("Your Obtain Marks : ", obtainMarks)


#--- % ----
perc =  obtainMarks/TotalMarks * 100
print("Your OverAll Percentage Is : ", perc)

#-- grade ---
percInt = int(perc)

grade = ""

if percInt >= 40 and percInt <= 49:
    grade = "D"
    
elif percInt >= 50 and percInt <= 59:
    grade = "C"
    
elif percInt >= 60 and percInt <= 69:
    grade = "B"
    
elif percInt >= 70 and percInt <= 79:
    grade = "A"
    
elif percInt >= 80 and percInt < 100:
    grade = "A1"
    
elif percInt == 100:
    grade = "A++"
    
elif percInt < 40:
    grade = "Ghar chl"
    

print("Your grad is : ", grade)


