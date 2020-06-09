from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    label = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )



    
    button = browser.find_element_by_css_selector("button#book")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)


    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    
    button2 = browser.find_element_by_css_selector("button#solve")
    button2.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла



#button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click()
