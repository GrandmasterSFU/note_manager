from datetime import datetime as dt


created_date = dt.strptime(input('Дата создания заметки: '), '%d-%m-%Y')
issue_date = dt.strptime(input('Дата истечения дедлайна: '), '%d-%m-%Y')

print(f'''
Дата создания заметки: {created_date.strftime('%d %B')}
Дата истечения заметки: {issue_date.strftime('%d %B')}
''')
