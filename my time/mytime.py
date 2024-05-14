
import datetime
import time
import sys
import os

def print_current_time():
    while True:
        current_time = datetime.datetime.now()
        weekday = current_time.strftime("%A")  # День недели
        month = current_time.strftime("%B")   # Месяц
        year = current_time.year               # Год
        day_of_month = current_time.day        # День месяца
        week_of_month = (current_time.day - 1) // 7 + 1  # Номер недели в месяце

        clock_str = current_time.strftime("%H:%M:%S")
        os.system('clear')  # Очищаем экран перед выводом новой информации
        print("Нажмите 'q' для завершения программы.")
        print("Текущее время:", clock_str)
        print("День недели:", weekday)
        print("Месяц:", month)
        print("Год:", year)
        print("День месяца:", day_of_month)
        print("Неделя в месяце:", week_of_month)
        time.sleep(1)

        # Проверяем, была ли нажата клавиша 'q'
        if os.name == 'nt':
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b'q':
                    break
        else:
            import select
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                line = sys.stdin.readline()
                if line.rstrip() == 'q':
                    break

if __name__ == "__main__":
    print_current_time()
