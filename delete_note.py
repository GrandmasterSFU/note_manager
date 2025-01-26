notes_list = [
    {
        'username': 'User 1',
        'title': 'Заголовок 1',
        'content': 'Описание заметки 1',
        'status': 'в процессе',
    },
    {
        'username': 'User 2',
        'title': 'Заголовок 2',
        'content': 'Описание заметки 2',
        'status': 'завершена',
    },
    {
        'username': 'User 3',
        'title': 'Заголовок 3',
        'content': 'Описание заметки 3',
        'status': 'в процессе',
    }
]

while True:
    intr = input('Хотите ли вы удалить заметки?')
    if intr == 'да':
        query = input('Укажите критерий для удаления: Заголовок или Имя пользователя ')
        if query == 'Заголовок':
            title_to_delete = input('Укажите заголовок заметки для удаления: ')
            for note in notes_list:
                if note['title'] == title_to_delete:
                    notes_list.remove(note)
                    print('Заметка успешно удалена.')
                    break
            else:
                print('Заметка не найдена.')

        if query == 'Имя пользователя':
            title_to_delete = input('Укажите имя пользователя заметки для удаления: ')
            for note in notes_list:
                if note['username'] == title_to_delete:
                    notes_list.remove(note)
                    print('Заметка успешно удалена.')
                    break
            else:
                print('Заметка не найдена.')
        else:
            print('Критерий не определен')
    if intr == 'нет': break
print(notes_list)
