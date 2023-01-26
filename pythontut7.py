# # myDict = {"fName": "Kehinde", "lName": "Aturuka", "address": "Lagos"}
# #
# # print("My name : ", myDict["fName"])
# #
# # for k, v in myDict.items():
# #     print(k, v)
# #
# # print(myDict.get("mName", "Not here"))
# #
# # employees = []
# #
# # fname, lname = input ("Enter employee name: ").split()
# #
# # employees.append({'fname': fname, 'lname': lname})
# #
# # print(employees)
# # =====================================================
#
# customers = []
#
# while True:
#     createEntry = input("Enter customer (Yes/No) :")
#     createEntry = createEntry[0].lower()
#
#     if createEntry == 'n':
#         break
#
#     else:
#         fname, lname = input("Enter customer name : ").split()
#
#         customers.append({'fname': fname, 'lname': lname})
#
# for cust in customers:
#     print(cust['fname'], cust['lname'])
# # =====================================================
# def factorial(num):
#
#     if num <= 1:
#         return 1
#     else:
#
#         result = num * factorial(num - 1)
#         return result
#
# print("80! = ", factorial(80))

# Fibonacci numbers

def fibonacci(num):

    if num == 1:
        return 1

    elif num == 0:
        return 0
    else:
        result = fibonacci(num - 1) + fibonacci(num - 2)
        return result

print(fibonacci(5))