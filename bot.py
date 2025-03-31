from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

cookie = driver.find_element(by=By.ID, value="cookie")

five_min = time.time() + 60 * 5
last_upgrade_time = time.time()


upgrade_ids = [
    "buyCursor",
    "buyGrandma",
    "buyFactory",
    "buyMine",
    "buyShipment",
    "buyAlchemy lab",
    "buyPortal",
    "buyTime machine",
    "buyElder Pledge",
]




while True:
    current_time = time.time()
    try:
        cookie.click()
    except Exception:
        cookie = driver.find_element(By.ID, "cookie")
        cookie.click()


    if current_time - last_upgrade_time >= 4:
        last_upgrade_time = current_time

        buyable_upgrades = []
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        parsed_costs = []

        for price in all_prices:
            text = price.text
            if text != "":
                cost = int(text.split("-")[1].strip().replace(",", ""))
                parsed_costs.append(cost)

        for upgrade_id, cost in zip(upgrade_ids, parsed_costs):
            try:
                element = driver.find_element(By.ID, upgrade_id)
                if "grayed" not in element.get_attribute("class"):
                    buyable_upgrades.append((element, cost))
            except Exception:
                continue

        if buyable_upgrades:
            buyable_upgrades.sort(key=lambda x: x[1], reverse=True)
            buyable_upgrades[0][0].click()

    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break