# Проект FitLife - MVP версия 1.0
WATER_PER_ML = 30
WATER_PER_L = 1000
#Шаг1-Знакомство с пользователем и получение от него данных и запись этих данных в переменные
print('Добро пожаловать в фитнес-трекер Fitlife')
user_name = input("Введите ваше имя?")
user_age = int(input('Сколько Вам лет:'))
#Шаг2-Запрос веса в кг и роста в метрах
user_weight = float(input('Введите свой вес в кг, при необходимости используйте точку:'))
user_height = float(input('Введите свой рост в м, используя точку:'))
bmi = round(user_weight / (user_height ** 2), 1) #Рассчёт индекса массы тела
water_ml = user_weight * WATER_PER_ML #Рассчёт нормы воды в миллилитрах
water_l = round((water_ml / WATER_PER_L), 2) #Перевод нормы воды в литры и округление до 2 десятичных знаков
print()
#Шаг3-красиво оформляем
message = f"Отчёт для пользователя:{user_name.title()} ({user_age} г.)"
print(message)
print('Твой индекс массы тела:', bmi)
print('Рекомендуемая норма воды:', water_l, 'л. в день')
print()
print ('Расчет окончен. Будьте здоровы!')