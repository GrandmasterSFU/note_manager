from datetime import datetime as dt

username = str(input('Введите имя пользователя: '))
title = str(input('Введите название заметки: '))
content = str(input('Добавьте описание вашей заметки: '))
status = str(input('опишите статус заметки: '))
created_date = dt.strptime(input('Дата создания заметки: '), '%d-%m-%Y')
issue_date = dt.strptime(input('Дата истечения дедлайна: '), '%d-%m-%Y')

print(f'''
Имя пользователя: {username}
Название заметки: {title}
Описание заметки: {content}
Статус заметки: {status}
Дата создания заметки: {created_date.strftime('%d %B')}
Дата истечения заметки: {issue_date.strftime('%d %B')}
''')
