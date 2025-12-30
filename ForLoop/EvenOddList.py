numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_list = []
odd_list = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_list.append(numbers[i])
    else:
        odd_list.append(numbers[i])

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
