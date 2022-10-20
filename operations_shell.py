import logger
import operations_content as opcon


def show_all_files_content():
    opcon.read_file("personal_info.csv.txt")
    opcon.read_file("department.csv.txt")
    opcon.read_file("salary.csv.txt")
    logger.add_log_entry(f'запрос показа всех записей информационной базы')

def add_data():
    opcon.add_entry()
    logger.add_log_entry(f'запрос на добавление данных')