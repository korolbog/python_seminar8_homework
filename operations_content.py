import csv
from csv import DictWriter

def read_file(file_name):
    fields = []
    rows = []
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    print('' + ''.join(field for field in fields))
    for row in rows:
        for col in row:
            print("%10s"%col,end=" "),
        print('\n')


def add_entry():
    print('Введите табельный номер: '); id_person = int(input())
    print('Введите номер пропуска: '); pass_card = int(input())
    print('Введите фамилию: '); family_name = input()
    print('Введите имя: '); first_name = input()
    print('Введите второе имя: '); second_name = input()
    print('Введите год рождения: '); birth_year = int(input())
    print('Введите название отдела: '); department = input()
    print('Введите название должности: '); position = input()
    print('Введите заработную плату в $: '); monthly_salary = int(input())
    
    personal_info_field_names = ['id_person', 'pass_card', 'family_name', 'first_name', 'second_name', 'birth_year']
    department_info_field_names = ['id_person', 'department', 'position']
    salary_info_field_names = ['id_person', 'monthly_salary']
     
    personal_info_dict = {'id_person' : id_person, 'pass_card' : pass_card,
        'family_name' : family_name, 'first_name': first_name,
        'second_name' : second_name, 'birth_year': birth_year}

    department_info_dict = {'id_person' : id_person, 'department' : department, 'position' : position}
    
    salary_info_dict = {'id_person' : id_person, 'monthly_salary': monthly_salary}

    with open('personal_info.csv.txt', 'a') as personal_info_file:
        dictwriter = DictWriter(personal_info_file, fieldnames = personal_info_field_names)
        dictwriter.writerow(personal_info_dict)
        personal_info_file.close()
    
    with open('department.csv.txt', 'a') as department_info_file:
        dictwriter = DictWriter(department_info_file, fieldnames = department_info_field_names)
        dictwriter.writerow(department_info_dict)
        department_info_file.close()

    with open('salary.csv.txt', 'a') as salary_info_file:
        dictwriter = DictWriter(salary_info_file, fieldnames = salary_info_field_names)
        dictwriter.writerow(salary_info_dict)
        department_info_file.close()
    print('Спасибо. Данные внесены.')


def search_id():
    id_to_search = input('Введите искомую фамилию сотрудника: ')

    with open('personal_info.csv.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if id_to_search in line:
                print(line)
    with open('department.csv.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if id_to_search in line:
                print(line)
    with open('salary.csv.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if id_to_search in line:
                print(line)

def delete_entry():
    surname_to_delete = input('Введите фамилию сотрудника для удаления: ')

    with open('personal_info.csv.txt', 'r') as rfile:
        lines = rfile.readlines()
        surname_to_delete = input('Введите номер телефона для удаления: ')
        with open('personal_info.csv.txt', 'w') as wfile:
            for line in lines:
                if surname_to_delete not in line:
                    wfile.write(line)
                    print(line)


    with open('department.csv.txt', 'r') as rfile:
        lines = rfile.readlines()
        surname_to_delete = input('Введите номер телефона для удаления: ')
        with open('department.csv.txt', 'w') as wfile:
            for line in lines:
                if surname_to_delete not in line:
                    wfile.write(line)
                    print(line)

    with open('salary.csv.txt', 'r') as rfile:
        lines = rfile.readlines()
        surname_to_delete = input('Введите номер телефона для удаления: ')
        with open('salary.csv.txt', 'w') as wfile:
            for line in lines:
                if surname_to_delete not in line:
                    wfile.write(line)
                    print(line)