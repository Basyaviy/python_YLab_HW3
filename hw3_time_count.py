import time


def sleep():
    return 'func_result'


def my_decorator(func):
    def wrapper(call_count, start_sleep_time, factor, border_sleep_time):
        print('Кол-во запусков = ', call_count)
        print('Начало работы')
        for n in range(call_count):
            t = start_sleep_time * factor ** n
            if t >= border_sleep_time:
                t = border_sleep_time
            result = func()
            print(f'Запуск номер {n+1}. Ожидание: {t} секунд. Результат декорируемой функции = {result}')

        return result
    return wrapper


my_result = my_decorator(sleep)

my_result({
    'call_count': 5,
    'start_sleep_time': 4,
    'factor': 3,
    'border_sleep_time': 100
 })
