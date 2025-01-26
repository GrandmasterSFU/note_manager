print('Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку')
note ={
        'title': None,
        'content': None,
    }
while True:
    tittle = input('Введите название заметки')
    if tittle == 'YES':
        break
    content = input('Введите содержание заметки')
    status = input('Введите статус заметки')

    note.update()