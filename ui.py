import pandas as pd

def request():
    print('\n1. Список всех сотрудников\
        \n2. Список уволенных работников\
        \n3. Список работающих сотрудников\
        \n4. Подробная информация по сотруднику\
        \n5. Информация о выплате заработной платы сотруднику\
        \n6. Закончить работу с файлом')
    while True:
        res = input('\nВведите номер действия - ')
        try:
            if int(res) >= 0 and int(res) <= 6:
                return int(res)
        except:
            continue


def printCSV(df_f, text='Результат'):
    print('\n------------------------------------------------------\n'
      ,text,'\n'
      '------------------------------------------------------')
    print(df_f)
    print('------------------------------------------------------')
    
def list_p_ui(db_r):
    while True:
        res = input('\nВведите номер сотрудника - ')
        try:
            if int(res) >= 0 and int(res) < db_r.shape[0]:
                return int(res)
        except:
            continue
