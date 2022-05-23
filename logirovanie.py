from datetime import datetime as dt
#rom using_interface import get_value
#from using_interface import viwe_data
#from controler import result_work as res


def log_it(res):
    time = dt.now().strftime('%H:%M')
    with open('logirovanie.txt', 'a') as logfile:
        logfile.write(f'{time} - {res}\n')