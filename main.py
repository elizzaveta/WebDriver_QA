import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path=r"D:\Downloads\chromedriver.exe")
browser.get('https://dou.ua/')
browser.implicitly_wait(10)

search_value = "c#"
browser.find_element_by_css_selector('[name="q"]').send_keys(search_value)
browser.find_element_by_css_selector('[name="q"]').send_keys(Keys.RETURN)
actual_search_value = browser.find_element_by_id('gsc-i-id1').get_attribute('value')
assert actual_search_value == search_value


wait = WebDriverWait(browser, 500)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "gs-title")))
search_result = browser.find_elements_by_css_selector('a.gs-title')
search_result[0].click()
assert (len(browser.window_handles) > 1)









