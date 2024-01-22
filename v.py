# Task 1: Check for a leap year
def check_leap_year():
    year = int(input("Введите год: "))
    era = input("Введите эру (ДНЭ или НЭ): ").upper()

    if era == "ДНЭ":
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    else:
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if leap_year:
        print(f"{year} год {era} – високосный")
    else:
        print(f"{year} год {era} – не високосный")

# Task 2: Add the word "kopek"
def add_kopek_word():
    number = int(input("Введите число от 1 до 99: "))

    if 10 < number < 20:
        form = "копеек"
    else:
        last_digit = number % 10
        if last_digit == 1:
            form = "копейка"
        elif 2 <= last_digit <= 4:
            form = "копейки"
        else:
            form = "копеек"

    print(f"{number} {form}")

# Task 3: Determine the day of the week by the day number of the year
def determine_day_of_week():
    day_number = int(input("Введите номер дня года (от 1 до 365): "))

    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    day_of_week = days_of_week[(day_number - 1) % 7]

    print(f"День недели для {day_number} дня года: {day_of_week}")

# Task 4: Determine the Zodiac sign by the date of birth
def determine_zodiac_sign():
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    sign = ""

    if (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 19):
        sign = "Овен"
    elif (month == 4 and 20 <= day <= 30) or (month == 5 and 1 <= day <= 20):
        sign = "Телец"
    elif (month == 5 and 21 <= day <= 31) or (month == 6 and 1 <= day <= 20):
        sign = "Близнецы"
    elif (month == 6 and 21 <= day <= 30) or (month == 7 and 1 <= day <= 22):
        sign = "Рак"
    elif (month == 7 and 23 <= day <= 31) or (month == 8 and 1 <= day <= 22):
        sign = "Лев"
    elif (month == 8 and 23 <= day <= 31) or (month == 9 and 1 <= day <= 22):
        sign = "Дева"
    elif (month == 9 and 23 <= day <= 30) or (month == 10 and 1 <= day <= 22):
        sign = "Весы"
    elif (month == 10 and 23 <= day <= 31) or (month == 11 and 1 <= day <= 21):
        sign = "Скорпион"
    elif (month == 11 and 22 <= day <= 30) or (month == 12 and 1 <= day <= 21):
        sign = "Стрелец"
    elif (month == 12 and 22 <= day <= 31) or (month == 1 and 1 <= day <= 19):
        sign = "Козерог"
    elif (month == 1 and 20 <= day <= 31) or (month == 2 and 1 <= day <= 18):
        sign = "Водолей"
    elif (month == 2 and 19 <= day <= 29) or (month == 3 and 1 <= day <= 20):
        sign = "Рыбы"
    else:
        print("Неверная дата или не в указанном диапазоне.")

    if sign:
        print(f"Ваш знак Зодиака: {sign}")

# Call the functions
check_leap_year()
add_kopek_word()
determine_day_of_week()
determine_zodiac_sign()
