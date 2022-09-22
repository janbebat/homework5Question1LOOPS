
import math

number1 = float(input("enter no1:"))


print("please select operation-\m"
      "1.(+)."
      "2.(-)."
      "3.(*)."
      "4.(/)."
      "5.(**)."
      "6.(%).")
operation = input()

number2 = float(input("enter no2:"))



if operation == "1" or operation == "+":
      result = number1 + number2
      print(result)

elif operation == "2" or operation == "-" :
      result = number1-number2
      print(result)

elif operation == "3" or operation ==  "*" :
      result = number1*number2
      print(result)

elif operation == "4" or operation == "/":
      result = number1/number2
      print(result)

elif operation == "5" or operation ==  "**" :
      result =number1**number2
      print(result)

elif operation == "6" or operation ==  "%" :
      result = number1%number2
      print(result)
else: print("error")




op = input("Extra choices:"
            "1_Rounded the number"
            "2_Floor the number"
            "3_Ceiling of number"
            "4_Right number"
            "5_actual result")




if op == "1":
      print(round(result))

elif op == "2":
      print(math.floor(result))

elif op == "3":
      print(math.ceil(result))

elif op == "4":
      print(int(result))

elif op == "5":
      print(result)

else:
      print("Error")


