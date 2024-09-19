import json  
import subprocess  
import os  
import threading  
from pynput import mouse, keyboard  
  
# 获取当前脚本的目录  
script_dir = os.getcwd().replace('\\', '/')  
  
# 拼接config.json的路径  
config_path = os.path.join(script_dir, 'config', 'config.json')  
  
# 读取config.json文件  
try:  
    with open(config_path, 'r', encoding='utf-8') as f:  
        config = json.load(f)  
        sleep_time = config.get('sleep_time', 600)  # 默认等待时间为600秒  
except FileNotFoundError:  
    print(f"配置文件 {config_path} 未找到！")  
    exit(1)  
except json.JSONDecodeError:  
    print(f"解析 {config_path} 时出错，请检查JSON格式是否正确！")  
    exit(1)  
  
# 拼接Xiaomi PC Service.exe的路径  
exe_path = os.path.join(script_dir, 'bin', 'Xiaomi PC Service.exe')  
  
# 检查EXE文件是否存在  
if not os.path.exists(exe_path):  
    print(f"可执行文件 {exe_path} 未找到！")  
    exit(1)  
  
# 定时器全局变量  
timer = None  
  
# 定时器回调函数  
def execute_exe():  
    try:  
        subprocess.run([exe_path], check=True)  
        print("Xiaomi PC Service.exe 执行成功。")  
    except subprocess.CalledProcessError:  
        print("Xiaomi PC Service.exe 执行失败。")  
  
# 重置定时器  
def reset_timer():  
    global timer  
    if timer is not None and timer.is_alive():  
        timer.cancel()  
    timer = threading.Timer(sleep_time, execute_exe)  
    timer.start()  
  
# 鼠标和键盘监听器  
def on_click(x, y, button, pressed):  
    if pressed:  
        print('Mouse clicked:', button, 'at', (x, y))  
        reset_timer()  
  
def on_move(x, y):  
    print('Mouse moved to:', (x, y))  
    reset_timer()  
  
def on_press(key):  
    try:  
        print('Key pressed:', key.char)  
    except AttributeError:  
        print('Special key pressed:', key)  
    reset_timer()  
  
# 初始化定时器  
reset_timer()  
  
# 监听鼠标和键盘  
with mouse.Listener(on_click=on_click, on_move=on_move) as listener_mouse, keyboard.Listener(on_press=on_press) as listener_keyboard:  
    # 注意：由于with语句块会阻塞直到监听器被关闭（例如，通过用户中断），  
    # 这里不需要显式调用join()，因为程序会在此处等待直到外部中断。  
    # 如果需要优雅地关闭监听器，可以在另一个线程中设置一个标志，并在检测到该标志时调用listener.stop()。  
    try:  
        listener_mouse.join()  # 实际上在这个with语句块中，这一行是多余的，因为with会处理  
        listener_keyboard.join()  # 同样，这一行也是多余的  
    except KeyboardInterrupt:  
        print("监听器被用户中断。")  
  
    # 如果需要，可以在这里添加清理代码，比如取消定时器  
    if timer is not None and timer.is_alive():  
        timer.cancel()
