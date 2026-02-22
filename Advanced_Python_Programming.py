#Task1 

#Display the Following Sentences on the Screen:
# My name is: (your name here)
# Currently enrolled in: (your semester)
# Section: (your section)
# Course name is: Advance Python Programming

# print("My name is: Fateh Haider.")
# print("Currently enrolled in: 4th Semester.")
# print("Section: 4F")
# print("Course: Advanced Python Programming")

# Task2

# Take 4 numbers from user and display it like:
# First number is: 17
# Second number is: 12
# Third number is: 90
# Fourth number is: 34
# Then add first 2 numbers, subtract last 2 numbers, multiply 1 and 3, divide 2 and 4. And
# print output of these operations.

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# number3 = int(input("Enter third number: "))
# number4 = int(input("Enter fourth number: "))

# print(f"First number is: {number1}")
# print(f"Second number is: {number2}")
# print(f"Third number is: {number3}")
# print(f"Fourth number is: {number4}")

# add = number1 + number2
# subtract = number3 - number4
# multiply = number1 * number3
# divide = number2 / number4

# print(f"Sum of first two numbers is: {add}")
# print(f"Difference of last two numbers is: {subtract}")
# print(f"Product of first and third numbers is: {multiply}")
# print(f"Division of second and fourth numbers is: {divide}")

#Task3

# Price of one bike is Rs. 1000000 and the price of one pencil box is Rs. 50. Take number of
# bikes and pencil boxes from user and calculate their prices. You have to display the price
# and quantity of both bikes and pencil boxes. Like: Price of 5 pencil boxes is: Rs. 250


# OneBikePrice= 1000000
# OnePencilBoxPrice= 50

# NumberofBikes= int(input("Enter the number of Bikes: "))
# NumberofPencilBoxes=int(input("enter the number of pencil boxes: "))

# TotalBikePrice= OneBikePrice*NumberofBikes
# TolalPencilBoxPrice= OnePencilBoxPrice*NumberofPencilBoxes

# print(f"Price of {NumberofBikes} bikes is: Rs. {TotalBikePrice}")
# print(f"Price of {NumberofPencilBoxes} pencil boxes is: Rs. {TolalPencilBoxPrice}")

# Task4
# Type cast different data types to another. Show the results and explain what you understood
# in different type casting scenarios. Do tell whether is it implicit or explicit type casting?


# a =20
# b= 3.14
# c= a+b
# print(c)
# print(type(c))

# Python automatically converts the integer 'a' to a float before performing the addition with 'b',
#  which is a float. This is an example of implicit type casting, where Python handles the conversion
#  automatically without the need for explicit instructions from the programmer. The result 'c' is a 
# float, and its type is confirmed by the output of 'type(c)'.

# number= 14
# text= str(number)
# print(text)
# print(type(text))
 #in this example we are explicitly converting the integer 'number' to a string using the 'str()' function.
 #  This is an example of explicit type casting, where the programmer explicitly instructs Python to perform
 #  the conversion. The variable 'text' now holds the string representation of the number, and its type is confirmed
 #  by the output of 'type(text)'.

# Task5
# You are building a small billing system for a local shop.
#  Input the price of 3 items and calculate the total bill. 
# Give 10% discount on the total bill and print the amount before and after the discount.

# Item1_Price=float(input("Enter the price of item 1:"))
# Item2_Price=float(input("Enter the price of item 2:"))
# Item3_Price=float(input("Enter the price of item 3:"))

# Total_Bill= Item1_Price+Item2_Price+Item3_Price
# Discount= Total_Bill*0.1
# Final_Bill= Total_Bill-Discount

# print(f"Total bill before discount is: Rs. {Total_Bill}")
# print(f"Total bill after discount is: Rs. {Final_Bill}")

# Task6# 
# Store different data values in variables and print their data types assigned by the interpreter

# Interger_Value= 72
# Float_Value=5.12
# String_Value="Hello Muhammad!"
# Boolean_Value= True
# print(f"Integer value is: {Interger_Value} and its type is: {type(Interger_Value)}")    
# print(f"Float value is: {Float_Value} and its type is: {type(Float_Value)}")    
# print(f"String value is: {String_Value} and its type is: {type(String_Value)}")    
# print(f"Boolean value is: {Boolean_Value} and its type is: {type(Boolean_Value)}")    

# Task7
# You can add comments in python using # at start of the sentence. Write commented

# statements in Thonny about the concepts you have learnt so far in the lecture and lab.

#  i have learnt about variables, data types, type casting, and basic input/output operations in Python.
#  I have also learned how to perform arithmetic operations and how to use formatted strings for better output 
# presentation. Additionally, I have understood the difference between implicit and explicit type casting in Python.