from plyer import notification
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from tabulate import tabulate
import time

CASPER_URL_BASE = "https://casper.com/uk/en"
SHOW_ME_ALL_THE_DATA = True

opt = Options()
opt.add_argument("--headless")
opt.add_argument("--log-level=3")

driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=opt)

favourite_products = [
    {"product": "sheets", "type": "pillowcase"},
    {"product": "sheets", "type": "fitted-sheet", "size": "double"},
    {"product": "sheets", "type": "fitted-sheet", "size": "king"},
    {"product": "sheets", "type": "duvet-cover", "size": "double-200-x-200-cm"},
    {"product": "sheets", "type": "duvet-cover", "size": "king-225-x-220-cm"},
    {"product": "casper"},
    {"product": "pillow"},
    {"product": "casper-essential"},
    {"product": "hybrid-mattress"},
    {"product": "glowlight"},
    {"product": "casper", "size": "uk-king"},
    {"product": "duvet"}
]

products = {
    "mattresses": {
        "hybrid-mattress": "https://casper.com/uk/en/mattresses/hybrid-mattress/",
        "casper": "https://casper.com/uk/en/mattresses/casper/",
        "casper-essential": "https://casper.com/uk/en/mattresses/casper-essential/"
    },
    "pillow": {
        "pillow": "https://casper.com/uk/en/pillows/"
    },
    "bedding": {
        "sheets": "https://casper.com/uk/en/sheets/",
        "duvet": "https://casper.com/uk/en/duvet/",
        "mattress-protector": "https://casper.com/uk/en/mattress-protector/"
    },
    "bedframes": {
        "platform-bed": "https://casper.com/uk/en/platform-bed/",
        "electric-adjustable-beds": "https://casper.com/uk/en/electric-adjustable-beds/",
        "upholstered-bedframe": "https://casper.com/uk/en/upholstered-bedframe/"
    },
    "accessories": {
        "glowlight": "https://casper.com/uk/en/glow-light/buy/",
        "nightstand": "https://casper.com/uk/en/nightstand/",
        "dogbed": "https://casper.com/uk/en/dog-bed/"
    }
}

products_by_range = {}

all_products = []


def dismiss_cookies():
    # load the homepage
    print("loading homepage...")
    driver.get(CASPER_URL_BASE)

    # dismiss cookie dialog
    WebDriverWait(driver, 10).until(
        ec.frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//iframe[@title="TrustArc Cookie Consent Manager"]')
        )
    )
    print("waiting for cookie dialog...")
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.XPATH, "//a[@class='call'][text()='Agree and Proceed']")
        )
    ).click()
    print("clicked accept cookies")
    time.sleep(0.5)


def get_variant(product, colour=None, _type=None):
    variants = driver.find_element_by_xpath(
        "//select[@id='input-selectedProductVariant']"
    ).find_elements_by_tag_name("option")
    for variant in variants:
        segments = [x.strip() for x in variant.text.split('-')]
        friendly_name = segments[0]
        price = segments[1]
        size = variant.get_attribute("value")
        naive_in_stock = variant.is_enabled()
        p = {
            "product": product,
            "title": friendly_name,
            "size": size,
            "type": _type,
            "colour": colour,
            "price": price,  # will also say "out of stock"
            "discount_price": ("£%.2f" % (float(price[1:].replace(',', '')) * 0.3)) if "£" in price else "n/a",
            "naive_in_stock": naive_in_stock,
        }
        # print(" ".join([x if type(x) is str else "" for x in p.values()]))
        try:
            products_by_range[category].append(p)
        except KeyError:
            products_by_range[category] = [p]


def find_products(criteria, selection):
    return [
        x for x in selection if all(
            x[k] == v for k, v in criteria.items()
        )
    ]


def get_colours(product, _type=None):
    try:
        colours = driver.find_element_by_xpath(
            "//div[@data-qa='color-swatches']"
        ).find_elements_by_tag_name("button")
        for colour in colours:
            c = colour.get_attribute("aria-label")
            colour.click()
            time.sleep(2)
            print("colour: %s" % c)
            # <button aria-label="White/White" .../>
            get_variant(product, colour=c, _type=_type)
    except NoSuchElementException:
        get_variant(product)


if __name__ == "__main__":
    dismiss_cookies()

    for category, ranges in products.items():
        for product_range, url in ranges.items():
            print("loading %s" % product_range)
            driver.get(url)
            if driver.current_url != url:
                print("range %s redirected - sold out?" % product_range)
                continue
            try:
                types = driver.find_element_by_xpath(
                    "//select[@id='input-selectedProductType']"
                )
                for t in types.find_elements_by_tag_name("option"):
                    # the site uses annoying <span> and <li> tags so you can't just click the option directly
                    WebDriverWait(driver, 10).until(
                        ec.element_to_be_clickable(
                            (By.XPATH, "//span[contains(@class, 'SelectInputValueLabel')]")
                        )
                    ).click()

                    # wait for the animation
                    time.sleep(1)

                    WebDriverWait(driver, 10).until(
                        ec.element_to_be_clickable(
                            (By.XPATH, f"//li[contains(@class, 'InputDropdownListItem')][text()='{t.text}']")
                        )
                    ).click()
                    print("type: %s" % t.get_attribute("value"))
                    # wait for ajax or whatever
                    time.sleep(2)
                    get_colours(product_range, _type=t.get_attribute("value"))
            except NoSuchElementException:
                get_colours(product_range)

    driver.quit()

    for category, product_range in products_by_range.items():
        for p in product_range:
            all_products.append(p)

        if SHOW_ME_ALL_THE_DATA:
            print("%s:" % category)
            print(tabulate(product_range, headers="keys", tablefmt="pretty"))

    products_left_in_stock = []
    products_sold_out = []

    # might as well use a single loop here rather than a listcomp
    for product in all_products:
        if product["price"] != "Out of Stock":
            products_left_in_stock.append(product)

        # doesn't look like anything has been marked as actually sold out yet, so need to keep an eye on this
        elif product["price"].lower() == "sold out":
            products_sold_out.append(product)

    favourites_in_stock = [
        product
        for favourite in favourite_products
        for product in find_products(favourite, products_left_in_stock)
    ]

    if len(products_left_in_stock) > 0:
        print("here's what's left")
        print(tabulate(products_left_in_stock, headers="keys", tablefmt="pretty"))
    else:
        print("it's all gone!!!")
        print("(maybe you want to check the data? rerun with SHOW_ME_ALL_THE_DATA = True)")
        exit()

    if len(favourites_in_stock) > 0:
        print("some favourite products are in stock!")
        print(tabulate(favourites_in_stock, headers="keys", tablefmt="pretty"))
    else:
        print("all favourite products out of stock")

    if len(products_sold_out) > 0:
        print("it's going!")
        print(tabulate(products_sold_out, headers="keys", tablefmt="pretty"))

    for f in favourites_in_stock:
        notification.notify(
            "Casper",
            "Casper %s is back in stock! Price - %s" % (
                " ".join(x for x in [
                    f["product"],
                    f["type"],
                    f["title"],
                    f["colour"]
                ] if x is not None),
                f["discount_price"]),
            app_name="Casper Stock Checker",
            app_icon="./favicon.ico"
        )

    # keep notification open for a bit
    time.sleep(60)


