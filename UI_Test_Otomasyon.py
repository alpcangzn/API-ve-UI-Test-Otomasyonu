from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:\Drivers\chromedriver"
url = "https://www.hepsiburada.com/"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)
driver.maximize_window()

searchInput = driver.find_element_by_class_name("desktopOldAutosuggestTheme-input").send_keys("iphone").send_keys(Keys.ENTER)
time.sleep(3)
selectedProduct = driver.find_elements_by_css_selector("#3ea9b1a6-caf9-4b21-9d26-541ab6d3b012 li")[2].click()
time.sleep(3)
reviewsButton = driver.find_element_by_class_name("list-container").find_element_by_id("productReviewsTab").click()
time.sleep(3)
like = driver.find_element_by_xpath('//*[@id="hermes-voltran-comments"]/div[4]/div[3]/div/div[1]/div[2]/div[5]/div[1]/div/div[1]').click()
time.sleep(3)

driver.close()
driver.quit()
print("Test Tamamlandi")