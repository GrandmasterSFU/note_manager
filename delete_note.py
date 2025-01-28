# Удаление заметок
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
    qa = input('Хотите ли вы удалить заметки? ').lower()
    if qa == 'да':
        removal_criteria = input('Укажите заголовок или имя пользователя заметки для удаления: ')
        for i, d in enumerate(notes_list):
            if d['title'].lower() == removal_criteria.lower() or d['username'].lower() == removal_criteria.lower():
                del notes_list[i]
                print(f'Заметка успешно удалена, остались следующие заметки: {notes_list}')
            else:
                break
        print('Заметка по таким критериям не найдена')
        break
    if qa == 'нет': break

