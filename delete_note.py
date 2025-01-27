from enum import nonmember

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
for i in notes_list[:]:
    print(i)
while True:
    quary = input('Хотите ли вы удалить заметки?').lower()
    if quary == 'да':
        while True:
            title_to_delete = input('Укажите заголовок или имя пользователя заметки для удаления: ').lower()
            for note in range(len(notes_list)):
                if notes_list[note]['title'].lower() == title_to_delete or notes_list[note]['username'].lower() == title_to_delete:
                    del notes_list[note]
                    print(f'Заметка успешно удалена, остались следующие заметки: {notes_list}')
            if False:
                print('Заметка по таким критериям не найдена')
    if quary == 'нет': break
print(notes_list)
