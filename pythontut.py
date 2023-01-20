# # # # # # # Ask the user to input their name and assign it to a variable named name
# # # # # #
# # # # # # name = input('What is your name ')
# # # # # #
# # # # # # # Print hello followed by the name they entered
# # # # # #
# # # # # # print('Hello ', name)
# # # # #
# # # # #====================================================================
# # # # # # Ask the user to input two values and store them in variables num1 num2
# # # # # num1, num2 = input('Enter 2 numbers: ').split()
# # # # #
# # # # # # Convert the strings into regular numbers Integer
# # # # # num1 = int(num1)
# # # # # num2 = int(num2)
# # # # #
# # # # # # Add the values entered and store in a variable named sum
# # # # # sum = num1 + num2
# # # # #
# # # # # # Subtract values and store in difference
# # # # # difference = num1 - num2
# # # # #
# # # # # # Multiply the values and store in product
# # # # # product = num1 * num2
# # # # #
# # # # # # Divide the values and store in quotient
# # # # # quotient = num1 / num2
# # # # #
# # # # # # Use modulus on the values to find the remainder
# # # # # remainder = num1 % num2
# # # # #
# # # # # # Print the results
# # # # # print("{} + {} = {}".format(num1, num2, sum))
# # # # # print("{} - {} = {}".format(num1, num2, difference))
# # # # # print("{} * {} = {}".format(num1, num2, product))
# # # # # print("{} / {} = {}".format(num1, num2, quotient))
# # # # # print("{} % {} = {}".format(num1, num2, remainder))
# # # #
# # # # #====================================================================
# # # #
# # # # # Problem : Receive miles and convert to kilometers
# # # # # kilometers = miles * 1.60934
# # # # # Enter Miles 5
# # # # # 5 miles equals 8.04 kilometers
# # # #
# # # # # Ask the user to input miles and assign it to the distance variable
# # # # distance = input("Enter Miles: ")
# # # #
# # # # # Convert from string to integer
# # # # distance = int(distance)
# # # #
# # # # # Perform calculation by multiplying 1.60934 times distance
# # # # kilometers = distance * 1.60934
# # # #
# # # # # Print result using format()
# # # # print("{} miles equals {} kilometers".format(distance, kilometers))
# # # #
# # # # #====================================================================
# # #
# # # # Enter Calculation: 5 * 6
# # # # 5 * 6 = 30
# # #
# # # # Store the user input of 2 numbers and the operator
# # # num1, operator, num2 = input('Enter Calculation ').split()
# # #
# # # # Convert the strings into integers
# # # num1 = int(num1)
# # # num2 = int(num2)
# # #
# # # # if + then we need to provide output based on addition
# # # # Print the result
# # # if operator == "+":
# # #     print("{} + {} = {}".format(num1, num2, num1+num2))
# # # elif operator == "-":
# # #     print("{} - {} = {}".format(num1, num2, num1-num2))
# # # elif operator == "*":
# # #     print("{} * {} = {}".format(num1, num2, num1*num2))
# # # elif operator == "/":
# # #     print("{} / {} = {}".format(num1, num2, num1/num2))
# # # else:
# # #     print("Use either + - * or / next time")
# # #
# # # # #====================================================================
# #
# # # We'll provide different output based on age
# # # 1 - 18 -> Important
# # # 21, 50, > 65 -> Important
# # # All others -> Not Important
# #
# # # Receive age and store in age
# # age = eval(input("Enter age: "))
# #
# # # if age is both greater than or equal to 1 and less than or equal to 18 Important
# # if (age >= 1) and (age <= 18):
# #     print("Important Birthday")
# # # if age is either 21 or 50 Important
# # elif (age == 21) or (age == 50):
# #     print("Important Birthday")
# # # We check if age is less than 65 and then convert true to false and vice versa
# # elif not (age < 65):
# #     print("Important Birthday")
# # # Else Not important
# # else:
# #     print("Sorry, Not Important Birthday")
# #
# # #====================================================================
# #
# # If age is 5 Go to Kindergarten
# # Ages 6 through 17 goes to grades 1 through 12
# # If age is greater than 17 say go to college
# # Try to complete with 10 or less lines
#
# age = eval(input("Enter age: "))
# if (age == 5):
#     print("Go to Kindergarten")
# elif (age > 5) and (age <= 17):
#     grade = age -5
#     print("Go to Grade {}".format(grade))
# elif (age > 17):
#     print("Go to College")
# else:
#     print("Where is your mom?")