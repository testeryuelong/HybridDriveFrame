# -*-coding:utf-8 -*-
# @Author : Zhigang

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"启动浏览器，访问网址"
url="https://mail.126.com/"
driver=webdriver.Chrome(executable_path="d:\\chromedriver.exe")
driver.get(url)
driver.implicitly_wait(10)  #隐式等待
wait=WebDriverWait(driver,10,0.2)

"切换iframe"
wait.until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath('//iframe[contains(@id,"x-URS-iframe")]')))
"定位账号框输入"
input=wait.until(EC.visibility_of(driver.find_element_by_xpath('//input[@name="email"]')))
input.clear()
input.send_keys("XXXX")

"定位密码框输入"
passwd=wait.until(EC.visibility_of(driver.find_element_by_xpath('//input[@name="password"]')))
passwd.clear()
passwd.send_keys("XXXX")

"定位登陆按钮"
wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@id="dologin"]'))).click()
#wait.until(EC.element_to_be_clickable((By.ID,"dologin"))).click()

"点击通讯录"
wait.until(EC.element_to_be_clickable((By.XPATH,'//div[.="通讯录"]'))).click()

"点击新建联系人"
wait.until(EC.element_to_be_clickable((By.XPATH,'//span[.="新建联系人"]'))).click()

"输入姓名"
username=wait.until(EC.visibility_of(driver.find_element_by_xpath('//input[@id="input_N"]')))
username.clear()
username.send_keys("testyu")

"输入电子邮箱"
emailAddress=wait.until(EC.visibility_of(driver.find_element_by_xpath\
            ('//div[@id="iaddress_MAIL_wrap"]//input[@class="nui-ipt-input"]')))
emailAddress.clear()
emailAddress.send_keys("88888@qq.com")

"设为星标联系人"
starContact=wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@id="iaddress_MAIL_wrap"]/following-sibling::*[1]//b[contains(@id,"fly")]')))
starContact.click()

"输入手机号码"
telephone=wait.until(EC.visibility_of(driver.find_element_by_xpath('//div[@id="iaddress_TEL_wrap"]//input')))
telephone.clear()
telephone.send_keys("13800138000")

"输入备注"
remarks=wait.until(EC.visibility_of(driver.find_element_by_xpath('//textarea[@id="input_DETAIL"]')))
remarks.clear()
remarks.send_keys("测试联系人")

"点击确定"
ensureButton=wait.until(EC.element_to_be_clickable((By.XPATH,'//span[text()="确 定"]')))
ensureButton.click()

time.sleep(2)
assert "13800138000" and "88888@qq.com" in driver.page_source
print ("成功添加联系人")

"点击首页"
wait.until(EC.element_to_be_clickable((By.XPATH,'//div[.="首页"]'))).click()

"点击写信"
wait.until(EC.element_to_be_clickable((By.XPATH,'//li[contains(@id,"_mail_component")]//span[.="写 信"]'))).click()

"输入收件人"
addressee=wait.until(EC.visibility_of(driver.find_element_by_xpath('//input[@class="nui-editableAddr-ipt"]')))
addressee.send_keys("807237157@qq.com")

"输入主题"
theme=wait.until(EC.visibility_of(driver.find_element_by_xpath('//input[contains(@id,"subjectInput")]')))
theme.send_keys("测试邮件")

"上传附件,还可以使用剪切板，复制实现自动化上传附件"
upload=driver.find_element_by_xpath('//input[@type="file"]')
upload.send_keys("C:\\Users\\zhigang\\Desktop\\ss.py")

"切换iframe,写入文件内容"
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@class="APP-editor-iframe"]'))
driver.find_element_by_xpath('//body[@class="nui-scroll"]').send_keys("测试邮件内容，请查收")
driver.switch_to.default_content()

"点击发送"
driver.find_element_by_xpath('//footer[contains(@class,"jp")]/div[@role="button"]/span[.="发送"]').click()

"断言是否发送成功"
assert "发送成功"  in driver.page_source,"发送失败"
print ("邮件发送成功")

"强制等待查看效果"
time.sleep(2)

"关闭浏览器"
driver.quit()

