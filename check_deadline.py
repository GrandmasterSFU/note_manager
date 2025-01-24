from datetime import datetime as dt

current_date = dt.today()
print(f"Сегодняшняя дата: {current_date.strftime('%d-%m-%Y')}")
issue_date = dt.strptime(input('Введите дату дедлайна: '), '%d-%m-%Y')
days_until_deadline = (issue_date - current_date).days
if days_until_deadline > 0:
    print(f"Дедлайн через {days_until_deadline} дня(ей).")
else:
    print(f'Дедлайн просрочен')
