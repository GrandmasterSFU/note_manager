status_code = {
    '1': "Выполнено",
    '2': 'В процессе',
    '3': 'Отложено'
}
status = status_code['2']
print(f'Текующий статус заметки: {status}')
for k, v in status_code.items():
    print(f'Статус: "{k}" соответствует коду "{v}"')
while True:
    status = input('Введите новый статус вашей заметки: ')
    if status not in status_code.keys():
        print('не корректный код')
    else:
        print(f'Актуальный статус вашей заметки: {status_code[status]}')
        break