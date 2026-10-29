numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))
selected = []
for number in numbers:
    if number % 2 == 0:
        selected.append(number)
print(f"Исходный порядок: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Отсортированная копия: {sorted(selected)}")
