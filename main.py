from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=chrome_options)



driver.get("https://google.com")
driver.maximize_window()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Define the CSS Selector for the element
css_selector = ".QS5gu.sy4vM"

    # Wait until the element is present and visible
wait = WebDriverWait(driver, 30)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))

    # Scroll to the element if necessary
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(2)
    
element.click()

wait = WebDriverWait(driver, 30)
input_field = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "gLFyf")))
input_field.send_keys("olx" + Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "OLX.ro: Anunturi Gratuite - Peste 4 milioane anunturi")
link.click()

wait = WebDriverWait(driver, 30)
cookies_accept = wait.until(EC.visibility_of_element_located((By.ID, "onetrust-accept-btn-handler")))
cookies_accept.click()


search = driver.find_element(By.ID, "search")
search.clear()
search.send_keys("Honda CBR 600 RR" +Keys.ENTER)


wait = WebDriverWait(driver, 30)
price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="De la"]')))
price.clear()
price.send_keys("2500")


wait = WebDriverWait(driver, 60)
price2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="până la"]')))
price2.clear()
price2.send_keys("4500")

wait = WebDriverWait(driver, 60)
euro_span = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-testid="currency-item" and text()="€"]')))
driver.execute_script("arguments[0].scrollIntoView(true);", euro_span)
euro_span.click()

wait = WebDriverWait(driver, 60)
grid_view = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'svg[data-testid="grid-icon"]')))
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[data-testid="grid-icon"]')))
driver.execute_script("arguments[0].scrollIntoView(true);", grid_view)
grid_view.click()

time.sleep(999)