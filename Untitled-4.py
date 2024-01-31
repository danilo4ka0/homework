from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Конвертуємо рядок дати народження у datetime.date об'єкт
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Визначаємо рік для дня народження
        birthday_this_year = birthday.replace(year=today.year)

        # Перевіряємо, чи вже минув день народження в цьому році
        if birthday_this_year < today:
            # Якщо так, розглядаємо дату на наступний рік
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Визначаємо різницю між днем народження та поточним днем
        days_until_birthday = (birthday_this_year - today).days

        # Перевіряємо, чи день народження припадає на вихідний
        if days_until_birthday <= 7 and days_until_birthday >= 0:
            # Якщо так, переносимо дату привітання на наступний понеділок
            if birthday_this_year.weekday() == 5:  # Субота
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Неділя
                birthday_this_year += timedelta(days=1)

            # Додаємо ім'я та дату привітання у результат
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
