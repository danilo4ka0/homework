from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворюємо рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        input_date = datetime.strptime(date, "%Y-%m-%d")
        
        # Отримуємо поточну дату
        current_date = datetime.today()
        
        # Розраховуємо різницю між поточною датою та заданою датою
        date_difference = current_date - input_date
        
        # Повертаємо різницю у днях як ціле число
        return date_difference.days
    except ValueError:
        # Обробляємо виняток, якщо введена дата має неправильний формат
        print("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'")
        return None

# Приклад використання
today = "2021-05-05"
result = get_days_from_today("2021-10-09")

if result is not None:
    print(f"Кількість днів між {today} та '2021-10-09': {result}")
