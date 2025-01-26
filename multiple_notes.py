print('Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку')
note_list = []
note ={
        'title': None,
        'content': None,
    }
while True:
    tittle = input('Введите название заметки')
    if tittle == 'YES':
    qa = input('Хотите ли вы создать новую заметку? ')
    if qa == 'YES':
        username = input('Введите имя пользователя: ')
        tittle = input('Введите заголовок заметки: ')
        content = input('Введите описание заметки: ')
        note['title'] = tittle
        note['content'] = content
        print('Заметка успешно создана!')
    note_list.append(note)
    if qa == 'NO':
        break
    content = input('Введите содержание заметки')
    status = input('Введите статус заметки')

    note.update()
print(note)
