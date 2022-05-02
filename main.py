from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\ADMIN\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")


driver.get("http://www.google.com")
#gettitle=driver.title
#print("the title is",gettitle)
#driver.find_element_by_name("q").send_keys("selenium")
driver.find_element(by=By.NAME,value="q").send_keys("selenium")

def test12(self):
    expected="welcome"
    actual=driver.title

    self.assertEquals(expected,actual)

driver.close()




