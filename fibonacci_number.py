def fibonacci_number(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)


# print fibonacci_number(19)

# Function for nth fibonacci number - Dynamic Programing
# Taking 1st two fibonacci nubers as 0 and 1

# FibArray = [0, 1]
#
#
# def fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#     elif n <= len(FibArray):
#         return FibArray[n - 1]
#     else:
#         temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
#         FibArray.append(temp_fib)
#         return temp_fib
#
#
# # Driver
# # Program
# print(fibonacci(9))


# Function for nth fibonacci number - Space Optimisataion
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0 or n == 1:
        return n
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b + a


# Driver Program

print(fibonacci(10))

# This code is contributed by Saket Modi
