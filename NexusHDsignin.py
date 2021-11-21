from selenium import webdriver

driver = webdriver.Edge()
driver.get("http://www.nexushd.org/signin.php")
element_username = driver.find_element_by_xpath('//*[@id="nav_block"]/form[2]/table/tbody/tr[1]/td[2]/input')
element_username.send_keys("UserName")#将UserName改为你的用户名
element_password = driver.find_element_by_xpath('//*[@id="nav_block"]/form[2]/table/tbody/tr[2]/td[2]/input')
element_password.send_keys("Password")#将Password改为你的密码
element_login = driver.find_element_by_xpath('//*[@id="nav_block"]/form[2]/table/tbody/tr[7]/td/button[1]')
element_login.click()#点击登录后自动跳转至签到页面
element_content = driver.find_element_by_xpath('//*[@id="sign-in-form"]/textarea')
element_content.send_keys("希望大家今天能开心")#双引号内为任意签到内容，不能为空
element_signin = driver.find_element_by_xpath('//*[@id="qr"]')
element_signin.click()#点击签到
driver.quit()#关闭浏览器
