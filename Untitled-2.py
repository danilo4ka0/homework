import random

def get_numbers_ticket(minimum, maximum, quantity):
    # Перевірка коректності вхідних даних
    if not (1 <= minimum <= maximum <= 1000) or not (1 <= quantity <= maximum - minimum + 1):
        print("Некоректні параметри. Перевірте вхідні дані.")
        return []

    # Генерація унікальних чисел у заданому діапазоні
    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(minimum, maximum))

    # Повертаємо відсортований список унікальних чисел
    return sorted(list(numbers_set))

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
