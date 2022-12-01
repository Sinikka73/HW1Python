"""
 Пользователь вводит время в секундах.
 Переведите время в часы, минуты и секунды и выведите
 в формате чч:мм:сс. Используйте форматирование строк.
"""
seconds = int(input("Введите интервал времени в секундах: "))
hours = seconds // 3600
minute = seconds // 60 % 60
sec = seconds % 60
print(f'{seconds} секунд соответствует интервалу в {hours:02} ч.'
      f'{minute:02} мин.{sec:02} с.')
print(f"{seconds // 3600:02}:{seconds // 60 % 60:02}:{seconds % 60:02}")
