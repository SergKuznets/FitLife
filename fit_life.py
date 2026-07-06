# Проект FitLife - MVP версия 1.0
WATER_PER_ML = 30
WATER_PER_L = 1000
# Шаг1-Знакомство с пользователем и получение от него данных
print('Добро пожаловать в фитнес-трекер FitLife')
user_name = input("Введите ваше имя:")
user_name = user_name.title()
user_age = int(input('Сколько Вам лет:'))
# Шаг2-Запрос веса в кг и роста в метрах
user_weight = float(input('Введите свой вес в кг, используйте точку:'))
user_height = float(input('Введите свой рост в м, используя точку:'))
# Рассчёт индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)
# Рассчёт нормы воды в миллилитрах
water_ml = user_weight * WATER_PER_ML
# Перевод нормы воды в литры и округление до 2 десятичных знаков
water_l = round((water_ml / WATER_PER_L), 2)
print()
# Шаг3-красиво оформляем
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой индекс массы тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print()
print('Расчет окончен. Будьте здоровы!')
