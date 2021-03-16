import math

def sum(x, y):
  return str(int(x1) + int(y1))

from selenium import webdriver
#from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('num1')
    y = browser.find_element_by_id('num2')
    x1 = x.text
    y1 = y.text
    print("x=", x1)
    print("y=", y1)
    sum_el = sum(x, y)
    print("value of sum_el: ", sum_el)
    
    browser.find_element_by_id("dropdown").click()
    browser.find_element_by_css_selector((f"[value='{sum_el}']")).click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()