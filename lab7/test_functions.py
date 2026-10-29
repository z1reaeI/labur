from functions import average, normalize_text, sum_digits, select_numbers

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
print("Базовые проверки пройдены")

assert select_numbers([-5, 0, 2, 5], 2) == [5]

assert select_numbers([], 2) == []
assert select_numbers([-5, 0, 2], 100) == []

assert select_numbers([2], 2) == []
assert select_numbers([3], 2) == [3]
assert select_numbers([1], 2) == []

assert select_numbers([4, 4, 7, 9], 3) == [4, 4, 7, 9]
assert select_numbers([5, 1, 5, 5], 4) == [5, 5, 5]

assert select_numbers([9, 1, 7, 3], 2) == [9, 7, 3]

original = [-5, 0, 2, 5]
saved = original.copy()
select_numbers(original, 2)
assert original == saved

assert abs(average([1, 2]) - 1.5) < 1e-9

print("Все проверки пройдены")
