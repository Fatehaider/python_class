# if else statement in Python
# num1 = int(input("Enter a number: "))

# if num1 == 10:
#     print("num1 is 10")
# elif num1 == 20:
#     print("num1 is 20")
# elif num1 == 30:
#     print("num1 is 30")

# else :
#     print("num1 is not 10")

# print ("Thanks for using the if else statement program")


# AND / OR operator in Python
# age = int(input("Enter your age: "))
# if age >= 18 and age <= 65:
#     print("You are eligible to work")
# else:
#     print("You are not eligible to work")
#     print("Your age is:", age)
# if age < 18 or age > 65:
#     print("You are not eligible to work")
# else:
#     print("You are eligible to work")

# age = int(input("Enter your age: "))
# if not ( age >= 18 or age <= 65):
#     print("You are eligible to work")
# else:
#     print("You are not eligible to work")
#     print("Your age is:", age)












# Discount Management System
total_price = float(input("Enter the total price: "))
if total_price <= 0:


    print("Invalid price entered.")


elif total_price >= 1000 and total_price < 2000:


    discount = total_price * 0.10


    final_price = total_price - discount


    print(f"You get a 10% discount! Final price is: {final_price}")    


elif total_price >= 2000 and total_price < 3000:


    discount = total_price * 0.20


    final_price = total_price - discount


    print(f"You get a 20% discount! Final price is: {final_price}")


elif total_price >= 3000 and total_price < 5000:


    discount = total_price * 0.30


    final_price = total_price - discount   


    print(f"You get a 30% discount! Final price is: {final_price}")


elif total_price >= 5000:


    discount = total_price * 0.50


    final_price = total_price - discount   


    print(f"You get a 50% discount! Final price is: {final_price}")


else:


    print(f"No discount applied. Final price is: {total_price}")
cls