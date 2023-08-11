
print("**************************************************************\nWelcome to my Basic Arithemetic Calculator\n**************************************************************")

# Declare my variable
num1 = ''
num2 = ''
operator = 0
operandArr = ['+','-','*','/']

# Using Except block for Error Validation
while True:

  try:
     num1 = int(input("Please enter the first number: "))       
     num2 = int(input("Please enter the second number: "))       
  except ValueError:
     print("Not a valid input! Input must be an integer!")
     continue
  else:
     break 
    



print("\n**************************************************************")

# To check for error on choice of mathematical operation
while operator <= 0:
  operator = int(input("Please select an operation: \n1. Addition, \n2. Subtraction \n3. Multiplication \n4. Division\n************************************************************** \nEnter your choice(1,2,3 or 4): "))

  # if operator choice is below or above available options print error message...
  if operator < 0 or operator > 4:
      print('Sorry, input numbers within 1 to 4. TRY AGAIN!!!!')
      continue
  
  # else if within 1 - 4 perform the mathematical operation of choice
  else:
      for item in operandArr:
        # to get the index of the choice of mathematical operation by user and match it to operator choice by user.
        if operator == int(operandArr.index(item)+1):
           if operator == 4 and num2 == 0:
            print("Error: division by zero not allowed! RUN PROGRAM AGAIN!")
           else:
            operatorSymbol = operandArr[operator-1]
            # convert num1 and num2 back to string, so we can eval()
            num1 = str(num1)
            num2 = str(num2)
         
            # concact the variables
            result = num1+operatorSymbol+num2

            # print and eval() result value.
            print("\n")
            print(f"                   Result: {num1} {operatorSymbol} {num2} =", int(eval(result)))
            print("\n")

      
