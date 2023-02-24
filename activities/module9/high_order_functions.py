from functools import reduce

numbers = [3, 5, 2, 4, 7, 1, 12, 8]

print(f"Original list: {numbers}")

even_number = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers: ", end="")
print(list(even_number))

updated_list = map(lambda x, y: x + y, numbers, numbers[1:])
print("Updated list: ", end="")
print(list(updated_list))

max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Max number: {max_value}")

min_value = reduce(lambda x, y: x if x < y else y, numbers)
print(f"Min number: {min_value}")


def is_prime(n):
    res = list(filter(lambda x: x == 0, map(lambda y: n % y, range(2, n))))
    return len(res) == 0


print("Prime numbers: ", end="")
for i in numbers:
    if i == 1:
        continue
    if is_prime(i):
        print(i, end=" ")
