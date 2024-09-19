<div align="center">
<h1 align="center">Blue_Screen-Paper</h1>

English / [简体中文](./README_CN.md)

A BSOD paper for All Windows.

一个适配多版本Windows系统的仿蓝屏动画壁纸。

[![Windows][Windows-image]][download-url]
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]
![Python][Python-image]
![github][github-image]

[github-image]: https://img.shields.io/badge/HonkerBit-github-8A2BE2?logoColor=purple
[download-url]: https://github.com/Yidadaa/ChatGPT-Next-Web/releases
[Windows-image]: https://img.shields.io/badge/-Windows-blue?logo=windows
[Python-image]: https://img.shields.io/badge/Python-100%25-brightgreen
[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
</div>

## 如何使用
- 下载 *[release](https://codeload.github.com/HonkerBit/Blue_Screen-Paper/zip/refs/tags/release)*

- 将mointor.exe加入开机自启

- 在config/config.json中设置误操作息屏时间(默认10分钟)

## 蓝屏动画

- 在/bin文件夹内的Xiaomi PC sService.py为蓝屏动画(至于为什么叫这个名字---嗯---伪装成电脑驱动文件更容易骗同学去运行他😂😁)

- 双击执行会立即启动蓝屏动画

- 图片使用硬编码不依赖外部图片

- 对于不同系统版本启动不同的蓝屏动画

- <kbd>Alt</kbd> + <kbd>F4</kbd>关闭动画

- ###### 使动画全屏播放：

```
self.root.attributes("-fullscreen", True)   #全屏
self.root.wm_attributes('-topmost',1)   #窗口置顶
self.root.overrideredirect(True)    #去边框，任务栏不显示
```

- ###### 判断是否为中文版：

```
def using_chinese_flag(self):
    loc_lang = locale.getdefaultlocale()
    if "zh_CN"in loc_lang:
        return True
    else:
        return False
```

- ###### 获取Windows版本：

```
def get_platform(self):
    """
    获取window版本
    :return:
    """
    platform = plat()
    if "Windows" in platform:
        windows_version = platform.split('-')[1]
        return int(windows_version)
    else:
        return None
```

## 检测程序

- 当Windows无操作时间超过/config/config.json中设置的时间时启动blue_screen蓝屏动画(默认10分钟)
- ###### 设置config.json：
```
{  
    "sleep_time": 600 #默认600秒
}
```

- ###### 使用定时器：

```
reset_timer()
```

- ###### 当检测到操作时重置定时器：

```
def reset_timer():  
    global timer  
    if timer is not None and timer.is_alive():  
        timer.cancel()  
    timer = threading.Timer(sleep_time, execute_exe)  
    timer.start()  
```

- ###### 当无操作时间超过预定时间:

```
# 定时器回调函数  
def execute_exe():  
    try:  
        subprocess.run([exe_path], check=True)  
        print("Xiaomi PC Service.exe 执行成功。")  
    except subprocess.CalledProcessError:  
        print("Xiaomi PC Service.exe 执行失败。")  
```

- ###### 鼠标移动监测：

```
def on_move(x, y):  
    print('Mouse moved to:', (x, y))  
    reset_timer() 
```

- ###### 鼠标点击监测：

```
def on_click(x, y, button, pressed):  
    if pressed:  
        print('Mouse clicked:', button, 'at', (x, y))  
        reset_timer()  
```

- ###### 键盘按键监测：

```
def on_press(key):  
    try:  
        print('Key pressed:', key.char)  
    except AttributeError:  
        print('Special key pressed:', key)  
    reset_timer()  
```
- 项目里的monitor.py留有输出，运行后会输出监测到的鼠标和键盘状态

- ###### 鼠标移动：

![image](https://github.com/user-attachments/assets/1d4904ce-c3bd-48be-bcf4-62c4ded66b4c)

- ###### 鼠标点击：

![image](https://github.com/user-attachments/assets/fd328988-26e0-4601-9c87-64640ec80cc2)

- ###### 键盘敲击：

![image](https://github.com/user-attachments/assets/68d6e36b-44fe-44d2-a288-17d44215b459)

