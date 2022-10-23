
import pandas as pd
from ui import printCSV, request
from action import list_all, list_unw, list_w, list_p, list_z
from data_base import readCSV
from logger import logger_info


def maine_f():
    db_title = readCSV('job_title.csv')
    db_imp = readCSV('list_of_imployees.csv')
    db_salary = readCSV('salary.csv')
    pd.set_option('colheader_justify', 'center')
    db_res = list_all(db_imp, db_title)
    printCSV(db_res, '\t\tСписок всех сотрудников')
    flag = True
    while flag:
        select = request()
        match select:
            case 1:
                db_res = list_all(db_imp, db_title)
                printCSV(db_res, '\t\tСписок всех сотрудников')
                logger_info('список всех сотрудников')
            case 2:
                db_res = list_unw(db_imp, db_title)
                printCSV(db_res, '\t\tСписок уволенных сотрудников')
                logger_info('список уволенных сотрудников')
            case 3:
                db_res = list_w(db_imp, db_title)
                printCSV(db_res, '\t\tСписок работающих сотрудников')
                logger_info('список работающих сотрудников')
            case 4:
                db_res, name = list_p(db_imp, db_title)
                printCSV(db_res, '\tПодробная информация по сотруднику')
                logger_info(f'подробная информация по сотруднику - {name}')
            case 5:
                name, db_res = list_z(db_imp, db_salary)
                printCSV(db_res, f'Заработная плата {name}')
                logger_info(f'заработная плата - {name}')
            case 6:
                flag = False
