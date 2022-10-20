
def show_instructions():
    print('Для показа всех записей базы нажмите "1"')
    print('Для добавления записи о сотруднике нажмите "2"')     

def user_command():
    print('Введите номер команды от 1 до 2: ', end = '')
    return int(input())
