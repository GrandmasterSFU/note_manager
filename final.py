from datetime import datetime as dt

username = str(input('Введите имя пользователя: '))
title = str(input('Введите название заметки: '))
content = str(input('Добавьте описание вашей заметки: '))
status = str(input('опишите статус заметки: '))
first = input('Введите название первого заголовка: ')
second = input('Введите название второго заголовка: ')
third = input('Введите название третьего заголовка: ')
headers = [first, second, third]
created_date = dt.strptime(input('Дата создания заметки: '), '%d-%m-%Y')
issue_date = dt.strptime(input('Дата истечения дедлайна: '), '%d-%m-%Y')

notes = {
    'username': username,
    'title': title,
    'content': content,
    'status': status,
    'headers': headers,
    'created_date': created_date.strftime('%d %B'),
    'issue_date': issue_date.strftime('%d %B'),
}
print(notes)




