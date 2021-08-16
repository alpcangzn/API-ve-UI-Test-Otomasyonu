from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:\Drivers\chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
url = "https://www.hepsiburada.com/"
driver.get(url)
driver.maximize_window()

searchInput = driver.find_element_by_class_name("desktopOldAutosuggestTheme-input")
searchInput.send_keys("iphone")
searchInput.send_keys(Keys.ENTER)
time.sleep(3)
#driver.get(url+"iphone-12-mini-128-gb-p-HBV00000YEBHX")
selectedProduct = driver.find_elements_by_css_selector("#f920abe3-f7ec-423e-88c9-178c75070fb5 li")[10]
#selectedProduct = driver.find_element_by_xpath('')
selectedProduct.click()
time.sleep(3)
reviewsButton = driver.find_element_by_class_name("list-container").find_element_by_id("reviewsTabTrigger")
reviewsButton.click()
time.sleep(3)
like = driver.find_element_by_xpath('//*[@id="hermes-voltran-comments"]/div[4]/div[3]/div/div[1]/div[2]/div[5]/div[1]/div/div[1]')
like.click()
time.sleep(7)
driver.close()
driver.quit()
print("Test Tamamlandi")