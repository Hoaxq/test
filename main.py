with open('цифры.txt', 'r') as file:
    max_number = None
    count_numbers_in_range = 0

    for chislo in file:
        number = int(chislo)
        if max_number is None or number > max_number:
            max_number = number
        if 1000 <= number < 1500:
            count_numbers_in_range += 1

print(f"Максимальное число: {max_number}")
print(f"Количество чисел в промежутке [1000;1500): {count_numbers_in_range}")
