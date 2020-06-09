from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/cats.html")

time.sleep(1)
browser.find_element_by_id("button")