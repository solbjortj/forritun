import math
num_int = int(input("Input a number: "))    
# Fill in the missing code
num1_int = 0
num2_int = 0

while num_int > 0:
    num1_int = num_int
    if num1_int > num2_int:
        num2_int = num1_int
    else:
        num_int = int(input("Input a number: ")) 

print("The maximum is", num2_) 