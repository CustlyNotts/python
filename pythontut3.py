# # # # while True:
# # # #     try:
# # # #         number = int(input("Please enter a number: "))
# # # #         break
# # # #
# # # #     except ValueError:
# # # #         print("You didn't enter a number")
# # # #
# # # #     except:
# # # #         print("An unknown error occurred")
# # # #
# # # # print("Thank you for entering a number")
# # #
# # # secret_num = 7
# # # while True:
# # #     guess = int(input("Guess a number between 1 and 10 : "))
# # #
# # #     if guess == secret_num:
# # #         print("you guessed it!")
# # #         break
# # # A - Z 65 - 90
# # # a - z 97 - 122
# #
# # print("A = ", ord("A"))
# # print("65 = ", chr(65))
# # =========================
# # Input enter a string to hide in upper case
# norm_string = input("Enter a string to hide in Uppercase : ")
#
# secret_string = ""
#
# # Cycle through each character in the string
# for char in norm_string:
#
#     # Store each character code in a new string
#     secret_string += str(ord(char) - 23)
#
# # Print Secret Message
# print("Secret Message : ", secret_string)
#
# # Cycle through each character code 2 at a time
# norm_string = ""
# for i in range(0, len(secret_string)-1, 2):
#
#     # Get the 1st and 2nd for the 2 digit number
#     char_code = secret_string[i] + secret_string[i+1]
#
#     # Convert the code into characters and add them to a new string
#     norm_string += chr(int(char_code) + 23)
#
# # Print Original Message
# print("Original Message : ", norm_string)