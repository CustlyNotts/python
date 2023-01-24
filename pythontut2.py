# # # # # for i in [2,4,6,8,10]:
# # # # #     print("i = ", i)
# # # # # for i in range(2,10):
# # # # #     print("i = ", i)
# # # # #================================
# # # # # Use for loop through the list from 1 to 21
# # # # for i in range(1,21):
# # # #
# # # # # Use modulus to check that the result is NOT EQUAL to 0
# # # #   if (i % 2 != 0):
# # # # # Print the odds
# # # #      print(i)
# # # #======================================
# # # # float numbers
# # #
# # # your_float = input("Enter a float: ")
# # #
# # # your_float = float(your_float)
# # #
# # # print("Round to 2 decimals: {:.2f}".format(your_float))
# #
# # # ===============================
# # # Have the user enter their investment amount and expected interest
# # # Each year, their investment will increase by their investment + their investment * interest rate
# # # Print out the earning after a 10 tear period
# #
# # # Ask for the money invested + the interest rate
# # principal, rate = input("Enter the investment and interest rate").split()
# # # Convert the value into a float
# # principal = float(principal)
# # principal1 = float(principal)
# # # Convert the value to a float and round the percentage rate by 2 digits
# # rate = float(rate) * 0.01
# # # Cycle through 10 years using a for loop and range from 0 to 10
# # for i in range(9):
# #     principal = principal + (rate * principal)
# # # Output the result
# # print("The total after 10 years is #{}, being a {:.0f}% increase".format(principal, ((principal * 100)/principal1)))
# # ==============================================
# import random
#
# rand_num = random.randrange(1,51)
#
# i = 1
#
# while (i != rand_num):
#     i += 1
#
# print("The random value is : ", rand_num)
# Print a pine tree
'''
    #
   ###
  #####
 #######
    #
'''
# How tall is the tree?
# Decrement spaces by 1 each time through the loop
# Increment the hashes by 2 each time
# Save spaces to stump by calculating tree height - 1
# Print spaces then hashes for each row
# Print stump spaces and 1 hash
# Get the number of rows
tree_height = input("How tall is the tree? ")
# Convert into an integer
tree_height = int(tree_height)
# Get the starting spaces for the top of tree
spaces = tree_height - 1
# There is one hash to start that will be incremented
hashes = 1
# Save stump spaces till later
stimp_spaces = tree_height - 1
# Make sure the right number of rows are printed
while tree_height != 0:
# Print the spaces
    for i in range(spaces):
        print(' ', end="")

# Print the hashes
    for i in range(hashes):
        print('#', end="")

# Newline after each row is printed
    print()

# Space is decremented by 1 each time
    spaces -= 1

# Hashes is incremented by 2
    hashes += 2

# Decrement tree height each time to jump out of the loop
    tree_height -= 1

# Print the spaces before the stump abd then the hash
for i in range(stimp_spaces):
    print(' ',end="")
print("#")