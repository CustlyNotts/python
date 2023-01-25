# # def add_numbers(num1, num2):
# #     return num1 + num2
# #
# # print("5 + 4 = ", add_numbers(5,4))
# # # =====================================
# def solve_eq(equation):
#     x, add, num1, equal, num2 = equation.split()
#
#     num1, num2 = int(num1), int(num2)
#
#     return "x = " + str(num2 - num1)
#
# print(solve_eq("x + 13 = 2"))
# ===========================================
# Returning multiple values
#
# def mult_div(num1, num2):
#     return (num1 * num2), (num1 / num2)
#
# mult, divide = mult_div(5, 4)
#
# print("5 * 4 = ", mult)
# print("5 / 4 = ", divide)
# ===================================
# Prime numbers
#
# def is_prime(num):
#     for i in range(2, num):
#         if (num % i) == 0:
#             return False
#
#     return True
#
# def getPrimes(max_num):
#     list_of_primes = []
#     for num1 in range(2, max_num):
#         if is_prime(num1):
#             list_of_primes.append(num1)
#
#     return list_of_primes
#
# max_num_to_check = int(input("Search for primes up to :"))
#
# list_of_primes = getPrimes(max_num_to_check)
#
# for prime in list_of_primes:
#     print(prime)
# =======================
# Handling unknown number of input variables

def sumAll(*args):

    sum = 0

    for i in args:
        sum += i

    return sum

print(sumAll(1,2,3,4,5,3,4,2,4,2,4,2,4,2,4,2,42,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,5,6,6,7,7,5,4,4,6,4,6,3,3,4,3,2,32,2,3,2,3,2,23,2,2,23,2,2,2,23,2,23,32,3,23,2,3,23))