import pyautogui
import time
import threading
import subprocess
from pynput import keyboard
from AppKit import NSWorkspace
import argparse
import os
import signal

# Функция для выполнения кликов в определенном окне
def clicker_in_window(interval, duration, window_name, key_mode):
    print(f"Starting clicker in window '{window_name}'...")
    end_time = time.time() + duration
    while time.time() < end_time:
        if get_active_window_title() == window_name:
            if key_mode:
                press_keys_interval(interval)
            else:
                pyautogui.click()  # Нажать левую кнопку мыши
                time.sleep(interval)  # Подождать перед следующим кликом

# Зажимание клавиш с интервалом keys = ['w', 'a', 's', 'd'], а чтобы не кикало за АФК
def press_keys_interval(interval):
    #keys = ['w', 'a', 's', 'd']
    keys = ['w', ' ']
    for key in keys:
        pyautogui.keyDown(key)
        time.sleep(interval)
        pyautogui.keyUp(key)

# Получение заголовка активного окна
def get_active_window_title():
    active_app_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    return active_app_name

# Функция для остановки кликера
def stop_clicker():
    print("Stopping clicker...")
    pid = os.getpid()  # Получить идентификатор процесса текущего скрипта
    os.kill(pid, signal.SIGTERM)  # Завершить процесс

# Стартовать кликер в отдельном потоке
def start_clicker(interval, duration, window_name, key_mode):
    thread = threading.Thread(target=clicker_in_window, args=(interval, duration, window_name, key_mode))
    thread.start()

# Настройка обработчика нажатия клавиш
def on_press(key):
    try:
        if key.char == 'q':
            stop_clicker()  # Остановить кликер при нажатии клавиши 'q'
    except AttributeError:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Mouse clicker')
    parser.add_argument('interval', type=float, help='Click interval in seconds')
    parser.add_argument('duration', type=float, help='Click duration in seconds')
    parser.add_argument('window_name', type=str, help='Window name to click in')
    parser.add_argument('-K', action='store_true', help='Enable key mode')

    args = parser.parse_args()

    # Начать слушать нажатия клавиш
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Запустить кликер в отдельном потоке
    start_clicker(args.interval, args.duration, args.window_name, args.K)
