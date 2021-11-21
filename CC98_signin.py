from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://www.cc98.org/logOn")
WebDriverWait(driver, 5, 0.1).until(EC.presence_of_element_located((By.ID, "loginName")))#98页面加载比nexushd稍慢，需要等待，否则找不到element会报错无法进行下一步
element_username = driver.find_element_by_id("loginName")
element_username.send_keys("UserName")#将UserName改为你的用户名
element_password = driver.find_element_by_id("loginPassword")
element_password.send_keys("Password")#将Password改为你的密码
element_login = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/form/button')
element_login.click()#点击登录
WebDriverWait(driver, 5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, "errorIcon")))
driver.get("https://www.cc98.org/signin")#在同一个标签页内访问加载页面
WebDriverWait(driver, 5, 0.1).until(EC.presence_of_element_located((By.ID, "post-topic-button")))
element_content = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[4]/div[2]/div[1]/textarea')
element_content.send_keys("希望大家今天能开心")#双引号内为签到内容，好像就算写了，签到楼内也只会显示“签到回复”
element_signin = driver.find_element_by_xpath('//*[@id="post-topic-button"]')
element_signin.click()#完成签到
driver.quit()#关闭浏览器