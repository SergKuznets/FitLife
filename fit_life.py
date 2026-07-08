# Проект FitLife - MVP версия 1.0
WATER_PER_ML = 30
WATER_PER_L = 1000


# Знакомство с пользователем и получение от него данных
def main():
    """Запускаем приложение Fitlife"""
    print('Добро пожаловать в фитнес-трекер FitLife')
    user_name = input('Введите ваше имя:')
    user_name = user_name.title()
    # Запрос возраста с проверкой ввода возраста целым числом
    while True:
        try:
            user_age = int(input('Сколько Вам лет:'))
            break
        except ValueError:
            print('Введите возраст целым числом')
    # Запрос веса в кг и роста в метрах с проверкой и заменой
    while True:
        try:
            user_weight = float(input('Введите вес в кг:').replace(',', '.'))
            break
        except ValueError:
            print('Введите свой вес в кг, например 75.5 или 75,5')
    while True:
        try:
            user_height = float(input('Введите ctрост в м:').replace(',', '.'))
            break
        except ValueError:
            print('Введите свой рост в м, например 1.8 или 1,8')
    # Рассчёт индекса массы тела
    bmi = round(user_weight / (user_height ** 2), 1)
    # Рассчёт нормы воды в миллилитрах
    water_ml = user_weight * WATER_PER_ML
    # Перевод нормы воды в литры и округление до 2 десятичных знаков
    water_l = round((water_ml / WATER_PER_L), 2)
    print()
    return user_name, user_age, bmi, water_l


if __name__ == '__main__':
    user_name, user_age, bmi, water_l = main()
    # Финальный вывод отчёта для пользователя
    print(
        f"Отчет для пользователя: {user_name} ({user_age} г.)\n"
        f"Твой индекс массы тела: {bmi}\n"
        f"Рекомендуемая норма воды: {water_l} л. в день\n\n"
        "Расчет окончен. Будьте здоровы!",
    )
