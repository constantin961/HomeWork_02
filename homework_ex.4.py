factor = int(input(f'Introduceti nr N '))
factorial_sum = 1
for n in range(1, (factor + 1)):
    factorial_sum = n * factorial_sum
print(factorial_sum)



# nr = int(input('Number'))
#
# if nr < 1:
#     print(f'Cannot calculate factorial for {nr}')
# else:
#     accumulator = 1
#     for a in range(1, nr + 1):
#         accumulator *= a
#     print(accumulator)