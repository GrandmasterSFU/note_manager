headers = []
while True:
    a = input('Запишите заголовки своей заметки: ')
    if a == '' or a == 'stop':
        break
    headers.append(a)
print(f'Основные детейлс заметки: {", ".join(headers)}')


a = 'хЕРНЯ'