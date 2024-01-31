import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    digits_and_plus = re.sub(r'\D', '', phone_number)

    # Перевіряємо, чи номер починається з '+'
    if digits_and_plus.startswith('+'):
        return digits_and_plus
    elif digits_and_plus.startswith('380'):
        # Якщо номер починається з '380', додаємо лише '+'
        return '+' + digits_and_plus[3:]
    else:
        # Якщо номер не має міжнародного коду, додаємо '+38'
        return '+38' + digits_and_plus

# Приклад використання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
