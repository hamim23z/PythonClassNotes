#10/8/24
#Write a program that obtains three floating point numbers from the user and determines the largest#

user_num1 = float(input("Enter first number: "))
user_num2 = float(input("Enter second number: "))
user_num3 = float(input("Enter third number: "))

if user_num1 >= user_num2 and user_num1 >= user_num3:
    print("The largest number is: ", user_num1)
elif user_num2 >= user_num1 and user_num2 >= user_num3:
    print("The largest number is: ", user_num2)
else:
    print("The largest number is: ", user_num3)