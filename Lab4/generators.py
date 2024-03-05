# def squares_generator(N):
#     for i in range(1, N + 1):
#         yield i ** 2

# N = int(input("Enter a value for N: "))
# for square in squares_generator(N):
#     print(square)

# def even(N):
#     for i in range(0, N + 1, 2):
#         yield i


# N = int(input("Enter a value for N: "))

# even_numbers = even(N)
# print(','.join(map(str, even_numbers)))

# def division(N):
#     for i in range(0, N + 1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i

# N = int(input("Enter a value for N: "))

# for num in division(N):
#     print(num)

# def squares(a, b):
#     for i in range(a, b + 1):
#         yield i ** 2

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# for square in squares(a, b):
#     print(square)


# def countdown(n):
#     while n >= 0:
#         yield n
#         n -= 1

# n = int(input("Enter a value for n: "))

# for num in countdown(n):
#     print(num)
