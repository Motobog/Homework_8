from datetime import datetime as dt

def logger_info(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt','a', encoding='utf-8') as file:
        file.write(f'{time} : {data}\n')
