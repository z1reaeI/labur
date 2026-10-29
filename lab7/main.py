from functions import sum_digits, average, normalize_text, select_numbers

number = int(input("Целое число: "))
print(f"Сумма цифр: {sum_digits(number)}")

raw = input("Числа через пробел: ")
numbers = []
for part in raw.split():
    numbers.append(int(part))

result = average(numbers)
if result is None:
    print("Нет данных")
else:
    print(f"Среднее: {result:.2f}")

text = input("Текст: ")
print(f"Нормализованный текст: {normalize_text(text)}")

threshold = int(input("Порог: "))
selected = select_numbers(numbers, threshold)
print(f"Выборка: {selected}")
