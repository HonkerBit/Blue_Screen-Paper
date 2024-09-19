import io
import random
import locale
from tkinter import *
from os import system
from PIL import ImageTk
from base64 import b64decode
from PIL import Image as imim
from tkinter import messagebox
from  platform import platform as plat
"""
图片硬编码，不依赖外部图片
"""
 
class App:
    """
    要重写alt+tab组合键
    win10蓝屏，进度速度不同
    不同语言显示不同画面
    """
    def __init__(self):
        self.root=Tk()
        self.root.title('Your Windows Is Dead')
        self.root.attributes("-fullscreen", True)   #全屏
        self.root.wm_attributes('-topmost',1)   #窗口置顶
        self.root.overrideredirect(True)    #去边框，任务栏不显示
        self.root.bind("<Key>",self.key_watcher)
        plat_version=self.get_platform()
        self.__using_chinese_flag=self.using_chinese_flag()
        self.__qr_code_base64 = b'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'
        if plat_version==10 or plat_version==11:
            self.version_10()
        else:
            self.version_other()
        self.root.mainloop()
 
    def using_chinese_flag(self):
        loc_lang = locale.getdefaultlocale()
        if "zh_CN"in loc_lang:
            return True
        else:
            return False
 
    def version_other(self):
        self.label=Label(self.root)
        self.root.config(bg='blue')
        self.label.config(text="""A problem has been detected and Windows has been shut down to prevent damage to your computer.\n\nIf this is the first time you've seen this stop error screen,restart your computer.If this screen appears again,follow these steps:\n\nCheck to be sure you have adequate disk space.If a driver is identified in the stop message,disable the driver or check with the manufacturer for driver updates.Try changing video adapters. \n\nCheck with your hardware vendor for any BIOS updates.Disable BIOS memory options such as caching or shadowing if you need to use safe Mode to remove or disable components,restart your computer.Press F8 to select advanced startup options,and then select safe mode.\n\nTechical information:\n\n*** stop:0×0000008E （0×0000005，0×805F91E2，0×B3EE79A8，0×00000000）\n\nSafeBoxKrnl.sys - Address B6D64846 base at B6055000, DataStamp 49ad02f7""")
        self.label.config(font=("",20,"bold"),fg='white',bg='blue',wraplength=self.root.winfo_screenwidth(),justify="left")
        self.label.place(x=0,y=0,width=self.root.winfo_screenwidth(),height=500,anchor="nw",)
 
    def show_win10_progress(self):
        """
        win10蓝屏进度
        :return:
        """
        if self.__using_chinese_flag:
            self.big_words_label.config(text=f"你的电脑遇到问题，需要重新启动。\n\n我们只收集某些错误信息，然后为你重新启动。\n\n{self.n}% 完成")
            self.small_words_label.config(text="有关此问题的详细信息和可能的解决方法，请访问 http://windows/stopcode\n\n如果致电支持人员，请向他们提供一下信息\n\n终止代码：SYSTEM_SERVICE_EXCEPTION")
        else:
            self.big_words_label.config(text=f"Your PC ran into a problem and needs to restart.\n\nWe're just collecting some error,and then we'll restart for you.\n\n({self.n}% complete)")
            self.small_words_label.config(text="For more information about this issue and possible fixes, visit \nhttps://www.windows.com/stopcode\n\nIf you call a support person, give them this info:\nStop code：SYSTEM_SERVICE_EXCEPTION")
        self.n+=1
        if self.n==101:
            self.label1.after_cancel(self.show_win10_progress)
        else:
            if self.n<20:
                self.label1.after(random.randint(400,800), self.show_win10_progress)
            elif 20<self.n<80:
                self.label1.after(random.randint(80,100), self.show_win10_progress)
            elif 80<self.n<90:
                self.label1.after(random.randint(400,500), self.show_win10_progress)
            elif 90<self.n<95:
                self.label1.after(random.randint(200,300), self.show_win10_progress)
            else:
                self.label1.after(random.randint(1000,1200), self.show_win10_progress)
 
    def version_10(self):
        """
        windows10蓝屏
        :return:
        """
        self.n=1
        self.root.config(bg='#0078d7')
        self.label1=Label(self.root)
        self.big_words_label=Label(self.root)
        self.small_words_label=Label(self.root)
        self.small_words_label.config(font=("微软雅黑",13,),fg='white',bg='#0078d7',justify="left")
        paned = PanedWindow(self.root)
        photo1=b64decode(self.__qr_code_base64)
        data_stream = io.BytesIO(photo1)
        pil_image = imim.open(data_stream)
        photo = pil_image.resize((110, 110))
        paned.image = ImageTk.PhotoImage(photo)
        self.qr_img_label = Label(self.root, image=paned.image,background='#0078d7')
        self.label1.config(font=("微软雅黑",110,),fg='white',bg='#0078d7',justify="left")
        self.big_words_label.config(font=("微软雅黑",20,),fg='white',bg='#0078d7',justify="left")
        self.label1.place(relx=0.0001,rely=0.12,width=self.root.winfo_screenwidth()*0.36,height=self.root.winfo_screenheight()*0.2,anchor="nw",)
        if self.__using_chinese_flag:
            self.big_words_label.config(text=f"你的电脑遇到问题，需要重新启动。\n\n我们只收集某些错误信息，然后为你重新启动。\n\n0%完成")
            self.small_words_label.config(
                text="有关此问题的详细信息和可能的解决方法，请访问 http://windows/stopcode\n\n如果致电支持人员，请向他们提供一下信息\n\n终止代码：SYSTEM_SERVICE_EXCEPTION")
            self.big_words_label.place(relx=0.0001,rely=0.32,width=self.root.winfo_screenwidth()*0.7,height=self.root.winfo_screenheight()*0.3,anchor="nw",)
            self.small_words_label.place(relx=0.0001, rely=0.605, width=self.root.winfo_screenwidth() * 0.87,
                                height=self.root.winfo_screenheight() * 0.22, anchor="nw", )
        else:
            self.big_words_label.place(relx=0.0001,rely=0.32,width=self.root.winfo_screenwidth()*0.85,height=self.root.winfo_screenheight()*0.3,anchor="nw",)
            self.small_words_label.place(relx=0.0001, rely=0.605, width=self.root.winfo_screenwidth() * 0.82,
                                height=self.root.winfo_screenheight() * 0.22, anchor="nw", )
            self.big_words_label.config(
                text=f"Your PC ran into a problem and needs to restart.\n\nWe're just collecting some error,and then we'll restart for you.\n\n(0% complete)")
            self.small_words_label.config(
                text="For more information about this issue and possible fixes, visit \nhttps://www.windows.com/stopcode\n\nIf you call a support person, give them this info:\nStop code：SYSTEM_SERVICE_EXCEPTION")
        self.label1.config(text=":(")
        self.qr_img_label.place(relx=0.165, rely=0.65, width=110,
                                height=110, anchor="nw", )
        self.label1.after(1000,self.show_win10_progress)
 
    def get_platform(self):
        """
        获取电脑window版本
        :return:
        """
        platform = plat()
        if "Windows" in platform:
            windows_version = platform.split('-')[1]
            return int(windows_version)
        else:
            return None
 
    def key_watcher(self,event):
        if event.keycode==27 :
            if self.__using_chinese_flag:
                ret=messagebox.askyesno("重启","确定要重启？")
            else:
                ret=messagebox.askyesno("reboot","Are you sure to reboot?")
            if ret:
                system('reboot')
 
if __name__ == '__main__':
    a=App()
