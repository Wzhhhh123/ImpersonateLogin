from selenium import webdriver

from time import sleep

option = webdriver.FirefoxOptions()
option.add_argument('--headless')
driver = webdriver.Firefox(firefox_options=option, executable_path='/usr/local/bin/geckodriver')


zhanghao="chenlei"
mima="chenlei"



driver.get("http://8.131.54.75:1678/admin/login.jsp")
driver.find_element_by_id("adminname").send_keys(zhanghao)
driver.find_element_by_id("password").send_keys(mima)
driver.find_element_by_id("goLogin").click()
sleep(1)
driver.get("http://8.131.54.75:1678/admin/")
driver.get("http://8.131.54.75:1678/admin/menu_courses.jsp")
driver.get("http://8.131.54.75:1678/admin/redirect.jsp?adminItem=27")
driver.get("http://8.131.54.75:1678/admin/courseAdmin/index.jsp")

driver.get("http://8.131.54.75:1678/admin/courseAdmin/tabs.jsp")
driver.get("http://8.131.54.75:1678/admin/courseAdmin/sidebar.jsp?sidebar=exp&headerFrame=true&tabIndex=expAdmin/guides/expGuides.jsp")
driver.get("http://8.131.54.75:1678/admin/courseAdmin/expAdmin/guides/workspaceDesk_pub.jsp")



driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[1]/td[2]/a").click()
all_h = driver.window_handles
driver.switch_to.window(all_h[1])
while True:
    sleep(1)
    print("我已经打开虚拟机啦")
    sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/nav/div/div[2]/ul/li[4]/a").click()
    sleep(60)
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/nav/div/div[2]/ul/li[4]/ul/li[1]/a").click()
    except:
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/nav/div/div[2]/ul/li[4]/a").click()
        sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/nav/div/div[2]/ul/li[4]/ul/li[1]/a").click()
