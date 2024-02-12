from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
amount_id = "cookies"
product_prefix = "product"
product_price_prefix = "productPrice"
upgrades = "upgrades"

consent = driver.find_element(By.CLASS_NAME, "fc-button.fc-cta-consent.fc-primary-button")
consent.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)

counter = 0

while True:
    cookie.click()
    cookie_amount = driver.find_element(By.ID, amount_id).text.split(" ")[0]
    cookie_amount = int(cookie_amount.replace(",", ""))

    counter += 1

    if counter >= 500:
        upgrade_tab = driver.find_element(By.ID, upgrades)
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(upgrade_tab, -100, 20).click().perform()
        counter = 0

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookie_amount >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()

