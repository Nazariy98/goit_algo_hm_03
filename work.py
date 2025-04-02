import re
import random
from datetime import datetime


def get_days_from_today(input_date: str) -> int:
    """
    Розраховує кількість днів між заданою датою та поточною.
    """
    try:
        now = datetime.today().date()
        correct_format_date = datetime.strptime(input_date, "%Y-%m-%d").date()
        difference_date = (correct_format_date - now).days
        return difference_date
    except ValueError:
        raise ValueError("Введіть дату у форматі 'РРРР-ММ-ДД'!")


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Повертає випадковий, унікальний набір чисел у межах заданих параметрів.
    """
    if min <= 0 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1):
        return []
    return sorted(random.sample(range(min, max+1), quantity))


def normalize_phone(phone_number: str) -> str:
    """
    Перетворює тел. на стандартний формат, залишаючи тільки цифри та символ '+'.
    """
    pattern = r"[^\+\d]"
    repl = ""
    clean_phone = re.sub(pattern, repl, phone_number)
    
    if clean_phone.startswith('+380'):
        return clean_phone
    if clean_phone.startswith('380'):
        return f"+{clean_phone}"
    if clean_phone.startswith('0'):
        return f"+38{clean_phone}"
    if clean_phone.startswith('+'):
        return clean_phone
    return f"+3{clean_phone}"


if __name__ == "__main__":
    # task_1:
    # user_input = input("Введіть дату у форматі РРРР-ММ-ДД: ")
    # print(get_days_from_today(user_input))
    print(get_days_from_today("2022-02-24"))
    print(get_days_from_today("2025-08-24"))
    print('-'*50)
    # task_2:
    try:
        print(get_numbers_ticket(0, 50, 5))     # має повернути []
        print(get_numbers_ticket(1, 1001, 10))  # має повернути []
        print(get_numbers_ticket(50, 50, 5))    # має повернути []
        print(get_numbers_ticket(1, 50, 0))     # має повернути []
        print(get_numbers_ticket(1, 50, 51))    # має повернути []
        print(get_numbers_ticket(10, 20, 15))   # має повернути []
        print(get_numbers_ticket(1, 10, 6))  # має повернути відсортований список унікальних чисел від 1 до 10 (6 чисел)
    except Exception as e:
        print(e)
    print('-'*50)
    # task_3:
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
    print(f"Нормалізовані номери телефонів для SMS-розсилки:\n{sanitized_numbers}")
    test = True if [e for e in sanitized_numbers if len(e) == 13 and e.startswith('+380')] else False
    print(test)
