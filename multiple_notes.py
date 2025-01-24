from update_status import manage_status
from datetime import datetime as dt


def multiply_notes():
    id_ = 0
    note_list = []
    print('Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку')
    while True:
        qa = input('Хотите ли вы создать новую заметку? ')
        if qa == 'YES':
            id_ += 1
            username = input('Введите имя пользователя: ')
            tittle = input('Введите заголовок заметки: ')
            content = input('Введите описание заметки: ')
            status_ = manage_status()
            note_deadline = dt.strptime(input('Введите дату дедлайна: '), '%d-%m-%Y')
            note_list.append(
                {'ID заметки': id_,
                 "Имя пользователя": username,
                 'Заголовок': tittle,
                 'Описание': content,
                 'Статус': status_,
                 'Дата создания': dt.today(),
                 'Дедлайн': note_deadline,
                 }
            )
            print('Заметка успешно создана!')
        if qa == 'NO':
            break
    return note_list


print(multiply_notes())
