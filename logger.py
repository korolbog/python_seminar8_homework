
from datetime import datetime as dt

def add_log_entry(data):
    time = dt.now().strftime('%H:%M:%S')
    with open('log.txt', 'a', encoding="utf-8") as file:
        file.write(f'{time} - {data}.\n')