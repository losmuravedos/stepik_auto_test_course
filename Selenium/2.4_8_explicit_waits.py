from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, "book")

    # this construction allows us wait the moment when price equals 100$
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button.click()

    # solve task section
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    field = browser.find_element(By.ID, "answer")
    field.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()


finally:
    # wait to visually evaluate the results of the script passing
    time.sleep(10)
    # close the browser after all the manipulations
    browser.quit()

