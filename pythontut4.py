# # rand_string = "  this is an important string  "
# #
# # rand_string = rand_string.lstrip() # Remove white spaces to the left
# #
# # rand_string = rand_string.rstrip() # Remove white spaces to the right
# #
# # rand_string = rand_string.strip() # Remove white spaces to the left and right
# #
# # print(rand_string.capitalize())
# #
# # print(rand_string.upper())
# #
# # print(rand_string.lower())
# #
# # a_list = ["Bunch", "of", "random", "words"]
# # print(" ".join(a_list)) # Turns a list into a string
# #
# # a_list_2 = rand_string.split()
# # for i in a_list_2:
# #     print(i)
# #
# # print("How many is : ", rand_string.count("is"))
# # print("Where is : ", rand_string.find("is"))
# # print(rand_string.replace("is", "a kind of "))
# # =======================================
# # Generate an Acronym
# orig_string = input("Convert to Acronym: ")
#
# orig_string = orig_string.upper()
#
# list_of_words = orig_string.split()
#
# for word in list_of_words:
#     print(word[0], end="")
# print()