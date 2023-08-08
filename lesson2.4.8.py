from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()
    
    #button = browser.find_element(By.TAG_NAME, "button")
    #button.click()
    #confirm = browser.switch_to.alert
    #confirm.accept()
    
    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    

    button = browser.find_element(By.ID, "solve")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла