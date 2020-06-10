from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from tabulate import tabulate
import time

CASPER_URL_BASE = "https://casper.com/uk/en"

driver = webdriver.Chrome(executable_path="./chromedriver.exe")

favourite_products = [

]

categories = {
    "mattresses": {
        "hybrid-mattress": "https://casper.com/uk/en/mattresses/hybrid-mattress/",
        "casper": "https://casper.com/uk/en/mattresses/casper/",
        "casper-essential": "https://casper.com/uk/en/mattresses/casper-essential/"
    },
    "pillow": {
        "pillow": "https://casper.com/uk/en/pillows/"
    },
    "bedframes": {
        "platform-bed": "https://casper.com/uk/en/platform-bed/",
        "electric-adjustable-beds": "https://casper.com/uk/en/electric-adjustable-beds/",
        "upholstered-bedframe": "https://casper.com/uk/en/upholstered-bedframe/"
    },
    "bedding": {
        "sheets": "https://casper.com/uk/en/sheets/",
        "duvet": "https://casper.com/uk/en/duvet/",
        "mattress-protector": "https://casper.com/uk/en/mattress-protector/"
    },
    "accessories": {
        "glowlight": "https://casper.com/uk/en/glow-light/buy/",
        "nightstand": "https://casper.com/uk/en/nightstand/",
        "dogbed": "https://casper.com/uk/en/dog-bed/"
    }
}

products = {}


# seems to work without this
def dismiss_cookies():
    # load the homepage
    driver.get(CASPER_URL_BASE)

    # dismiss cookie dialog
    WebDriverWait(driver, 10).until(
        ec.frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//iframe[@title="TrustArc Cookie Consent Manager"]')
        )
    )
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.XPATH, "//a[@class='call'][text()='Agree and Proceed']")
        )
    ).click()


if __name__ == "__main__":
    dismiss_cookies()

    for category, ranges in categories.items():
        for product, url in ranges.items():
            print("loading %s" % product)
            xpath = "//select[@id='input-selectedProductVariant']"
            driver.get(url)
            select = driver.find_element_by_xpath(xpath)
            variants = select.find_elements_by_tag_name("option")
            for variant in variants:
                segments = [x.strip() for x in variant.text.split('-')]
                friendly_name = segments[0]
                price = segments[1]

                name = variant.get_attribute("value")
                naive_in_stock = variant.is_enabled()
                print("%s %s %s %s %s" % (product, friendly_name, name, naive_in_stock, price))
                p = {
                    "product": product,
                    "title": friendly_name,
                    "variant": name,
                    "price": price,  # will also say "out of stock"
                    "discount_price": float(price[1:].replace(',', '')) * 0.4 if "£" in price else "n/a",  # will also say "out of stock"
                    "naive_in_stock": naive_in_stock,
                }
                try:
                    products[category].append(p)
                except KeyError:
                    products[category] = [p]

    for category, product in products.items():
        print("%s:" % category)
        print(tabulate(product, headers="keys", tablefmt="pretty"))
