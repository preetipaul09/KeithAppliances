import os
import csv
import re
import requests
import mysql.connector
import logging
from bs4 import BeautifulSoup
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxOptions
from datetime import datetime, timedelta, date
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from random import randint ,uniform
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from seleniumwire import webdriver as wire_webdriver  # If using selenium-wire
from seleniumwire import webdriver as wire_webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
# import pyautogui
import time
import random
import json
# from chromedriver_py import binary_path
# import pygetwindow as gw
# import undetected_chromedriver as uc
# import chromedriver_autoinstaller

from modules.saveRanks import commence as evalRanking
from modules.runTimeSecrets import HOST, DB, USER, PASS, HOST2, DB2, USER2, PASS2, HOST3, DB3, USER3, PASS3
# HOST, DB, USER, PASS = '157.245.132.95','kmpnthbyjc','kmpnthbyjc','7s4TGvU4VC'

# HOST, DB, USER, PASS = "162.243.170.201", "wfnpyvxqtp", "wfnpyvxqtp", "tvv2kGXHjE"
# # HOST2, DB2, USER2, PASS2 = "162.243.170.201","wfnpyvxqtp","wfnpyvxqtp","tvv2kGXHjE"
# # HOST3, DB3, USER3, PASS3 = "162.243.170.201", "wfnpyvxqtp", "wfnpyvxqtp", "tvv2kGXHjE"


# logger
# ------------------------------------------------------------
def loggerInit(logFileName):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
    file_handler = logging.FileHandler(f'logs/{logFileName}')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)
    return logger
logger = loggerInit(logFileName="ProdDetails.log")
# ---------------------------------------------------------------

# ---------------------- WEBDRIVER SETUP ----------------------

def simulate_mouse_movement():
    width, height = pyautogui.size()
    for _ in range(random.randint(3, 6)):
        x = random.randint(0, width)
        y = random.randint(0, height)
        pyautogui.moveTo(x, y, duration=random.uniform(0.3, 1.2))
        time.sleep(random.uniform(0.1, 0.4))

def human_scroll(driver):
    total_scrolls = random.randint(2, 5)
    for i in range(total_scrolls):
        scroll_by = random.randint(200, 600)
        driver.execute_script(f"window.scrollBy(0, {scroll_by});")
        time.sleep(random.uniform(0.5, 1.5))


# def triggerSeleniumOpera(useVPN=False, checkIP=False):
#     logger.debug("Selenium (Opera) triggered")

#     opera_browser_path = r"C:\Users\user\AppData\Local\Programs\Opera\opera.exe"
#     chromedriver_path = r"D:\_PreetiProjects\May\FBSappliance\driver134\chromedriver.exe"
    
#     # if not os.path.exists(binary_path):    
#     #     raise FileNotFoundError(f"ChromeDriver not found at: {binary_path}")
#     # if not os.path.exists(opera_browser_path):
#     #     raise FileNotFoundError(f"Opera browser not found at: {opera_browser_path}")

#     with open("vpn.config.json") as json_data_file:
#         configs = json.load(json_data_file)

#     attempts = 0
#     while attempts < 3:
#         try:
#             VPN_IP_PORT = random.choice(configs.get('VPN_IP_PORT', []))
#             seleniumwire_options = {
#                 'proxy': {
#                     "http": f"http://{VPN_IP_PORT}",
#                     "https": f"http://{VPN_IP_PORT}",
#                     'no_proxy': 'localhost,127.0.0.1'
#                 }
#             }

#             options = ChromeOptions()
#             options.binary_location = opera_browser_path
#             # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")
          
#             user_agents = [
#                 "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
#                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
#                 "Mozilla/5.0 (Windows NT 10.0; WOW64)...",
#             ]
#             options.add_argument(f"user-agent={random.choice(user_agents)}")
#             service = ChromeService(executable_path=chromedriver_path)
#             driver = (
#                 wire_webdriver.Chrome(service=service, options=options, seleniumwire_options=seleniumwire_options)
#                 if useVPN else
#                 webdriver.Chrome(service=service, options=options)
#             )

#             driver.set_page_load_timeout(60)
#             driver.set_script_timeout(60)

#             # Let page load
#             time.sleep(3)

#             # Open new tab using CTRL+T
#             pyautogui.hotkey('ctrl', 't')
#             time.sleep(1)

#             # Type URL and press Enter
#             target_url = "https://ip.me/" if checkIP else "https://example.com"
#             pyautogui.typewrite(target_url, interval=0.05)
#             pyautogui.press("enter")
#             time.sleep(3)

#             # Switch control to latest tab (important for .find_element to work)
#             driver.switch_to.window(driver.window_handles[-1])

#             if checkIP:
#                 time.sleep(random.uniform(2, 4))
#                 driver.refresh()
#                 ip_value = driver.find_element(By.CSS_SELECTOR, 'input#ip-lookup').get_attribute('value')
#                 logger.debug(f"New Rotated IP (Opera): {ip_value}")

#             return driver

#         except Exception as e:
#             logger.debug(f"[Opera] Attempt {attempts + 1}/3 failed with error: {e}")
#             attempts += 1
#             if attempts == 3:
#                 logger.error("triggerSeleniumOpera() failed after 3 attempts")
#                 raise e



# import json, logging, time, random, os
# from datetime import datetime
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.common.by import By

# logger = logging.getLogger(__name__)

def triggerSelenium(useVPN=False, checkIP=False):
    logger.debug("Selenium triggered")

    geckoPath = r"driver\\geckodriver.exe"
    if not os.path.exists(geckoPath):
        raise FileNotFoundError(f"GeckoDriver not found at: {geckoPath}")

    with open("vpn.config.json") as json_data_file:
        configs = json.load(json_data_file)

    attempts = 0
    while attempts < 3:
        try:
            VPN_IP_PORT = random.choice(configs.get("VPN_IP_PORT", []))

            options = FirefoxOptions()
            # options.add_argument('-headless')  # Uncomment if needed
            # options.add_argument('-private')    # Uncomment if needed

            service = Service(executable_path=geckoPath)

            if useVPN:
                from seleniumwire import webdriver as wire_webdriver  # Import only if VPN is used
                seleniumwire_options = {
                    'proxy': {
                        "http": f"http://{VPN_IP_PORT}",
                        "https": f"http://{VPN_IP_PORT}",
                        'no_proxy': 'localhost,127.0.0.1'
                    }
                }
                driver = wire_webdriver.Firefox(
                    service=service,
                    options=options,
                    seleniumwire_options=seleniumwire_options
                )
            else:
                from selenium import webdriver as vanilla_webdriver
                driver = vanilla_webdriver.Firefox(
                    service=service,
                    options=options
                )

            if checkIP:
                time.sleep(random.uniform(1, 3))
                driver.get("https://ip.me/")
                time.sleep(random.uniform(0.5, 1.5))
                driver.refresh()
                ip_value = driver.find_element(By.CSS_SELECTOR, 'input#ip-lookup').get_attribute('value')
                logger.debug(f"New Rotated IP: {ip_value}")

            return driver

        except Exception as e:
            logger.debug(f"Attempt {attempts + 1}/3 failed with error: {e}")
            attempts += 1
            if attempts == 3:
                logger.error("triggerSelenium() failed after 3 attempts")
                raise e

# VgFTsBvymAWgFJx

def try_press_and_hold_captcha(driver):
    try:
        logger.info("Checking for 'Press & Hold' CAPTCHA...")
        time.sleep(2)

        # Save snapshot of page for debugging
        driver.save_screenshot("captcha_detected.png")
        with open("captcha_page.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        # Detect and log all iframes
        from selenium.webdriver.remote.webelement import WebElement

        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        logger.info(f"Found {len(iframes)} iframes on the page.")

        for idx, frame in enumerate(iframes):
            logger.info(f"Iframe {idx} is WebElement: {isinstance(frame, WebElement)}")
            if not isinstance(frame, WebElement):
                logger.warning(f"Iframe {idx} is not a WebElement. Type: {type(frame)}")
                continue

            try:
                title = frame.get_attribute("title")
                src = frame.get_attribute("src")
                logger.info(f"Iframe {idx}: title='{title}', src='{src}'")
            except Exception as frame_exc:
                logger.warning(f"Issue accessing iframe {idx}: {frame_exc}")

        # Check if CAPTCHA is not present
        page_source = driver.page_source
        if "Press and hold" not in page_source and "px-captcha" not in page_source:
            logger.info("No CAPTCHA prompt detected — continuing scrape.")
            driver.switch_to.default_content()
            return True

        # Wait for CAPTCHA container
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "px-captcha"))
            )
            logger.info("CAPTCHA container found.")
        except:
            logger.warning("CAPTCHA container not found. Possibly already passed.")
            driver.switch_to.default_content()
            return True

        # Try multiple selectors to find the CAPTCHA press-and-hold button
        selectors = [
            ".px-captcha-error-button",
            ".px-captcha-btn",
            "div[data-testid='px-captcha-button']",
            ".button-holder > div",
            "#px-captcha button",
        ]

        button = None
        for selector in selectors:
            try:
                button = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                logger.info(f"Found CAPTCHA button using selector: {selector}")
                break
            except:
                continue

        if not button:
            driver.save_screenshot("captcha_button_not_found.png")
            logger.error("CAPTCHA button could not be located.")
            driver.switch_to.default_content()
            return False

        # Simulate press and hold
        ActionChains(driver).move_to_element_with_offset(button, 5, 5).click_and_hold().pause(10).release().perform()
        logger.info("Simulated press-and-hold action.")
        time.sleep(5)

        # Switch back to main content
        driver.switch_to.default_content()

        # Verify if CAPTCHA is still present
        if "Press and hold" in driver.page_source or "px-captcha" in driver.page_source:
            driver.save_screenshot("captcha_still_present.png")
            logger.warning("CAPTCHA still detected after interaction.")
            return False

        logger.info("CAPTCHA passed successfully.")
        return True

    except Exception as e:
        logger.exception(f"Exception while handling CAPTCHA: {e}")
        driver.switch_to.default_content()
        return False


def dump_debug(driver):
    try:
        with open("debug_page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        driver.save_screenshot("debug_screenshot.png")
    except Exception as e:
        logger.error(f"Error during debug dump: {e}")

def random_pause(min_time=2, max_time=5):
    """
    Add a random pause to simulate human thinking or waiting.
    """
    time.sleep(uniform(min_time, max_time))

def getAllProUrl(category_url):
    product_urls = set()
    new_category_url = category_url
    pageNumber = 1 
    try:
        # trigger driver funtion call here
        driver = triggerSelenium(useVPN=False,checkIP=True)
        while True:
            url = new_category_url if pageNumber == 1 else f'{new_category_url}&page={pageNumber}'
            driver.get(url)
            time.sleep(5)
            driver.refresh()
            random_pause(20,50)

            driver.save_full_page_screenshot("ss.png")
            
            human_scroll(driver)

            # simulate_mouse_movement()

            success = try_press_and_hold_captcha(driver)
            if not success:
                raise Exception("CAPTCHA could not be bypassed.")

            try:
                WebDriverWait(driver, 80).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#__next"))
                )
                time.sleep(random.uniform(1, 3))  # Additional delay
                human_scroll(driver)  # Additional human mimicry
            except TimeoutException:
                if "Press and hold" in driver.page_source:
                    logger.warning("CAPTCHA still present after waiting.")
                    driver.refresh()
                    random_pause(10,20)
                else:
                    logger.error("Timeout: Product elements did not load.")
                    driver.refresh()
                    random_pause(10,20)
                driver.save_screenshot("captcha_or_timeout.png")
                raise

            # dump_debug(driver)

            # products = driver.find_elements(By.CSS_SELECTOR, '#__next a[class="MuiTypography-root jss265 MuiTypography-body1"]')
            products = driver.find_elements(By.CSS_SELECTOR,"a[href*='/product/']")

            # Special case: URLs in data-uw-original-href
            alt_products = driver.find_elements(By.CSS_SELECTOR,"a[data-uw-original-href*='/product/']")

            # Process both sets
            for product in products + alt_products:
                product_url = product.get_attribute("href") or product.get_attribute("data-uw-original-href")
                if product_url and product_url not in product_urls:
                    product_urls.add(product_url)
                    with open("productUrls-GE-Profile.txt", "a", encoding="utf-8") as f:
                        f.write(product_url + "\n")

            print(f"Total unique product URLs found so far: {len(product_urls)}")
            pageNumber += 1
            if pageNumber == 50:
                break

        return product_urls
    except Exception as e :
        logger.debug(f"Driver not found")
    finally:
        driver.quit()
        
def fetch_product_data(product_url,vendor_id):
    from selenium.common.exceptions import NoSuchElementException
    import re, os, csv, time
    
    try:
        driver = triggerSelenium(checkIP=True)
        driver.get(product_url)
        time.sleep(10)
        random_pause(10, 60)

        temp = {}
        temp2 = {}
        url = product_url
        logger.debug(f"Fetching: {url}")

        # ✅ Extract product name from page
        try:
            productNameDiv = driver.find_element(By.CSS_SELECTOR, "h1#videoly-product-title")
            product_name = productNameDiv.text.strip()
            temp['product_name'] = product_name
        except NoSuchElementException:
            temp['product_name'] = None

        if not temp['product_name']:
            print(f"⏩ Skipping product because name not found: {url}")
            return None, None
    
        # ✅ Extract SKU (last numeric value from URL)
        sku_match = re.search(r"-(\d+)$", url)
        temp["vendor_sku"] = sku_match.group(1) if sku_match else None
        
        try:
            brand_meta = driver.find_element(By.CSS_SELECTOR, 'meta[property="product:brand"]')
            brand_name = brand_meta.get_attribute("content").strip()
            temp["brand_name"] = brand_name
        except NoSuchElementException:
            # fallback: try from product name (first word or two)
            words = product_name.split()
            temp["brand_name"] = " ".join(words[:2]) if len(words) > 1 else words[0]

        # # ✅ Extract brand (first keyword in URL after /product/)
        # try:
        #     url_part = url.split("/product/")[1]
        #     first_keyword = url_part.split("-")[0]
        #     # Ensure brand is part of product name
        #     if first_keyword.lower() in product_name.lower():
        #         temp["brand_name"] = first_keyword.capitalize()
        #     else:
        #         # fallback: extract brand from product name (first word)
        #         temp["brand_name"] = product_name.split()[0]
        # except Exception:
        #     temp["brand_name"] = None

        # ✅ Extract MPN
        # mpn_part = re.sub(r"-\d+$", "", url.split("/product/")[-1])  # remove numeric SKU
        # url_tokens = mpn_part.split("-")

        # # Normalize product name → lowercase alphanumeric tokens
        # name_tokens = re.sub(r'[^A-Za-z0-9]+', ' ', temp['product_name']).lower().split()

        # # Merge adjacent digits into single tokens (e.g. "4" "3" -> "43")
        # normalized_name_tokens = []
        # i = 0
        # while i < len(name_tokens):
        #     if name_tokens[i].isdigit():
        #         num = name_tokens[i]
        #         while i + 1 < len(name_tokens) and name_tokens[i+1].isdigit():
        #             num += name_tokens[i+1]
        #             i += 1
        #         normalized_name_tokens.append(num)
        #     else:
        #         normalized_name_tokens.append(name_tokens[i])
        #     i += 1

        # # Build MPN by taking URL tokens not in product name
        # mpn_tokens = [
        #     t for t in url_tokens 
        #     if t.lower() not in normalized_name_tokens and t.lower() != temp['brand_name'].lower()
        # ]

        # temp["product_mpn"] = "-".join(mpn_tokens).upper() if mpn_tokens else None

        # --- fallback: meta[name="keywords"] ---
        # if not temp["product_mpn"]:
        try:
            meta_keywords = driver.find_element(By.CSS_SELECTOR, 'meta[name="keywords"]').get_attribute("content")
            if meta_keywords:
                # Pick first token with letters+digits (likely the MPN)
                for token in meta_keywords.split(","):
                    token = token.strip()
                    if re.search(r"[A-Za-z]+\d+", token):
                        temp["product_mpn"] = token.upper()
                        break
        except NoSuchElementException:
            temp["product_mpn"] = None

        print("////////////////////////////////////////////////")
        print(f"Brand: {temp['brand_name']} | MPN: {temp['product_mpn']} | SKU: {temp['vendor_sku']}")
        print("////////////////////////////////////////////////")

        # ✅ MSRP
        try:
            productMsrp = driver.find_element(By.CSS_SELECTOR, 'p[data-uw-rm-sr="price"]')
            msrp_text = productMsrp.text.strip()
            if "-" in msrp_text:
                print(f"Skipping product due to MSRP range: {msrp_text}")
                return None, None
            product_msrp = msrp_text.replace("Rs.", "").replace("$", "").replace(",", "").replace(r"\ea", "").strip()
        except NoSuchElementException:
            product_msrp = None
        temp["msrp"] = product_msrp
        temp2["msrp"] = product_msrp

        # ✅ Image
        script_tags = driver.find_elements(By.TAG_NAME, "script")
        image_url = None
        for script in script_tags:
            script_content = script.get_attribute("innerHTML")
            if script_content and "linqcdn.avbportal.com/images" in script_content:
                match = re.search(r'https://linqcdn\.avbportal\.com/images/[a-zA-Z0-9\-]+\.jpg', script_content)
                if match:
                    image_url = match.group()
                    break
        temp['product_image'] = image_url
        temp["product_url"] = url
        temp2['url'] = url

        # ✅ Base Price
        try:
            basePice = driver.find_element(By.CSS_SELECTOR, 'div#product-content')
            price_text = basePice.text.strip()
            if "-" in price_text:
                print(f"Skipping product due to base price range: {price_text}")
                return None, None
            base_price = price_text.replace("$", "").replace(",", "").replace("Sale", "").replace("Rs.", "").replace(r"\ea", "").strip()
        except NoSuchElementException:
            base_price = None
        temp2['vendorprice_price'] = base_price
        temp2["vendorprice_finalprice"] = base_price

        # try:
        #     offers = []

        #     # 1. Click the rebate "Details" button
        #     details_button = WebDriverWait(driver, 5).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Show more details on this rebate"]'))
        #     )
        #     details_button.click()

        #     # 2. Wait for the rebate dialog to appear
        #     rebate_ul = WebDriverWait(driver, 5).until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR, "body div.MuiDrawer-root.MuiDrawer-modal ul.jss709"))
        #     )

        #     # 3. Scrape all li items from the popup
        #     items = rebate_ul.find_elements(By.TAG_NAME, "li")
        #     for item in items:
        #         text = item.text.strip()
        #         if text:
        #             offers.append(text)

        #     temp2["buy_more_save_more_text"] = offers if offers else None

        #     # 4. Close the rebate popup (optional, if needed for next product)
        #     try:
        #         close_btn = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Close']")
        #         close_btn.click()
        #     except:
        #         pass

        # except Exception as e:
        #     temp2["buy_more_save_more_text"] = None
        #     logger.debug(f"No rebate details found: {e}")
                
        # if temp2.get("buy_more_save_more_text"):
        #     temp2["buy_more_save_more_text"] = " ; ".join(temp2["buy_more_save_more_text"])


        # ✅ Extra metadata
        temp2['scraped_by_system'] = "Preeti pc"
        temp2['source'] = "direct_from_website"
        temp2['product_condition'] = 'New'

        # ✅ CSV output
        csv_file = "ProductCsv(preeti).csv"
        fieldnames = ["Name", "Brand", "SKU", "MPN", "base_price", "MSRP", "Image"]
        file_exists = os.path.isfile(csv_file)
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                "Name": temp.get("product_name"),
                "Brand": temp.get("brand_name"),
                "SKU": temp.get("vendor_sku"),
                "MPN": temp.get("product_mpn"),
                "base_price": base_price,
                "MSRP": product_msrp,
                "Image": temp.get("product_image")
            })
        print("✅ Product data appended to CSV.")
        print("--------------------------------------------------------")
        print(temp)
        print(temp2)
        print("--------------------------------------------------------")

        product_id, vendor_product_id = insertIntoMsp(temp, vendor_id)
        print("--------------------------------------------------------")
        print(product_id, vendor_product_id)
        print("--------------------------------------------------------")
        if temp2['vendorprice_price'] is None:
            logger.debug(f"vendorprice_price not found for product ID {product_id}")
            with open("priceNotFound.txt", "a") as file:
                file.write(f"{vendor_product_id}\n")
            return
        elif isinstance(temp2['vendorprice_price'], str):
            price_lower = temp2['vendorprice_price'].lower()
            if 'best price' in price_lower or 'price unavailable' in price_lower or 'call for best price' in price_lower:
                logger.debug(f"vendorprice_price not found!! - Price requires contact: {temp2['vendorprice_price']}")
                return
            else:
                insertall(product_id, vendor_product_id, temp2, vendor_id)
                evalRanking(vendor_id , product_id)
        return temp, temp2
    except Exception as e:
        logger.error(f"An error occurred while fetching product data: {e}")
    finally:
        if driver:
            driver.quit()

# Saving data to the MSP
def insertIntoMsp(row, vendor_id):
    product_id = vendor_product_id = None  # Initialize to None
    try:
        print("**************************")
        brand_id = checkInsertBrand(vendor_id, row['brand_name'])
        product_id = checkInsertProduct(vendor_id, brand_id, row['product_mpn'], row['product_name'], row['msrp'], row['product_image'])
        vendor_product_id = checkInsertProductVendor(vendor_id, product_id, row['vendor_sku'], row['product_name'], row['product_url'], row['msrp'])
        checkInsertProductVendorURL(vendor_id, vendor_product_id, row['product_url'])
    except Exception as e:
        logger.error(f"Error in insertIntoMsp: {e}")
    return product_id, vendor_product_id


def getBrandRawName(brand_name):
    letters, numbers, spaces = [], [], []
    for character in brand_name:
        if character.isalpha():
            letters.append(character)
        elif character.isnumeric():
            numbers.append(character)
        elif character.isspace():
            spaces.append(character)
    if len(letters) > 0: raw_name = "".join(spaces + letters)
    else: raw_name = "".join(spaces + numbers)
    return raw_name


# Add brand if doesn't exists
def checkInsertBrand(vendor_id, brand_name):
    import mysql.connector
    from mysql.connector import Error

    conn = None
    this = None

    try:
        print("Insert in checkInsertBrand")
        print(HOST, DB, USER, PASS)

        try:
            conn = mysql.connector.connect(
                host=HOST,
                port=3306,
                database=DB,
                user=USER,
                password=PASS
            )
            if conn.is_connected():
                print("✅ Connected to MySQL DB")
            else:
                print("❌ Connection failed")
                return None
        except Error as e:
            print(f"❌ Error connecting to MySQL: {e}")
            return None

        print("Connected db in checkInsertBrand")
        this = conn.cursor(buffered=True)

        this.execute("SELECT brand_id FROM BrandSynonyms WHERE brand_synonym = %s", (brand_name,))
        brand_id = this.fetchone()
        if brand_id:
            logger.info(f"{vendor_id} >> Found brand synonym: {brand_name} ({brand_id[0]})")
            return brand_id[0]
        else:
            brandRawNname = getBrandRawName(brand_name)
            brandRaw = brandRawNname.lower().strip()
            this.execute("SELECT brand_id, brand_name FROM Brand WHERE brand_raw_name = %s", (brandRaw,))
            records = this.fetchone()
            if records:
                fetchedBrandId = records[0]
                fetchedBrandName = records[1]
                if fetchedBrandName != brand_name:
                    insertBrandSynonymsQuery = "INSERT INTO BrandSynonyms (brand_id, brand_synonym) VALUES (%s, %s);"
                    this.execute(insertBrandSynonymsQuery, (fetchedBrandId, brand_name))
                    conn.commit()
                    logger.info(f"Inserted {brandRawNname} as a synonym for {fetchedBrandName}.")
                else:
                    logger.info(f"{brandRaw} Brand Name Matched")
                    return fetchedBrandId
            else:
                insertBrandQuery = "INSERT INTO Brand (brand_name, brand_key, brand_raw_name) VALUES (%s, %s, %s);"
                this.execute(insertBrandQuery, (brand_name, brand_name.replace(" ", "-").lower(), brandRaw))
                conn.commit()
                logger.info(f'{vendor_id} >> Added new brand "{brand_name} ({this.lastrowid})".')
                return this.lastrowid
    except Error as e:
        logger.warning(f"{vendor_id} >> MySQL ERROR checkInsertBrand() >> {e}")
        logger.warning(f"{vendor_id}, {brand_name}")
    finally:
        if this:
            this.close()
        if conn and conn.is_connected():
            conn.close()

# Add product if doesn't exists
def checkInsertProduct(vendor_id, brand_id, mpn, name, msrp, image):
    try:
        conn = mysql.connector.connect(host=HOST, database=DB, user=USER, password=PASS)
        if conn.is_connected():
            this = conn.cursor(buffered=True)
            checkProductQuery = "SELECT product_id FROM Product WHERE brand_id = %s AND product_mpn = %s"
            this.execute(checkProductQuery, [brand_id,mpn])
            records = this.fetchone()
            # Change this section
            if records is None:  # If no record found
                # Insert new product
                if msrp != '':
                    insertProductQuery = "INSERT INTO Product (brand_id,product_name,product_mpn,msrp,product_image) VALUES (%s,%s,%s,%s,%s)"
                    this.execute(insertProductQuery, (brand_id,name,mpn,msrp,image))
                else:
                    insertProductQuery = "INSERT INTO Product (brand_id,product_name,product_mpn,product_image) VALUES (%s,%s,%s,%s)"
                    this.execute(insertProductQuery, (brand_id,name,mpn,image))
                conn.commit()
                logger.info(f'{vendor_id} >> Added new product with mpn "{mpn} ({this.lastrowid})".')
                return this.lastrowid
            else:
                product_id = int(records[0])
                this.execute("UPDATE Product SET product_name = %s, product_image = %s WHERE product_id = %s", [name,image,product_id])
                conn.commit()
                if msrp != '':
                    this.execute("UPDATE Product SET msrp = %s WHERE product_id = %s AND msrp IS NULL", [msrp,product_id])
                    conn.commit()
                logger.info(f'{vendor_id} >> Updated details for product with mpn "{mpn} ({product_id})".')
                return product_id
    except mysql.connector.Error as e:
        logger.warning(f"{vendor_id} >> MySQL ERROR checkInsertProduct() >> {e}")
        logger.warning(f"{vendor_id}, {brand_id}, {mpn}, {name}, {msrp}, {image}")
        return None
    finally:
        if conn.is_connected():
            conn.close()
            this.close()

# Add product vendor if doesn't exists
def checkInsertProductVendor(vendor_id, product_id, sku, name, product_url, msrp):
    try:
        # First check if we have valid input
        if product_id is None:
            logger.warning(f"{vendor_id} >> Cannot insert vendor product: product_id is None")
            return None
            
        conn = mysql.connector.connect(host=HOST, database=DB, user=USER, password=PASS)
        if conn.is_connected():
            this = conn.cursor(buffered=True)
            if msrp == '' or msrp is None:
                msrp = None  # or set to 0.0 if you prefer a default value

            checkProductVendorQuery = "SELECT vendor_product_id FROM ProductVendor WHERE vendor_id = %s AND product_id = %s LIMIT 1"
            this.execute(checkProductVendorQuery, [vendor_id, product_id])
            records = this.fetchone()
            
            # Handle case where no records found
            if records is None:
                # Insert new record
                insertProductVendorQuery = "INSERT INTO ProductVendor (vendor_id, product_id, product_name, vendor_sku, msrp) VALUES (%s, %s, %s, %s, %s)"
                this.execute(insertProductVendorQuery, (vendor_id, product_id, name, sku, msrp))
                conn.commit()
                logger.info(f'{vendor_id} >> Added new product in ProductVendor "{vendor_id} x {product_id}".')
                return this.lastrowid
            else:
                # Update existing record
                vp_id = int(records[0])
                updateProductDetailQuery = "UPDATE ProductVendor SET vendor_sku = %s, product_name = %s, msrp = %s WHERE vendor_product_id = %s"
                this.execute(updateProductDetailQuery, [sku, name, msrp, vp_id])
                conn.commit()
                if this.rowcount == 1:
                    logger.info(f'{vendor_id} >> Updated details for vendor_product_id ({vp_id}).')
                logger.info(f'{vendor_id} >> Returned vendor_product_id ({vp_id}).')
                return vp_id
    except mysql.connector.Error as e:
        logger.error(f"{vendor_id} >> MySQL ERROR checkInsertProductVendor() >> {e}")
        return None
    finally:
        if conn.is_connected():
            conn.close()
            this.close()

# Add product vendor url if doesn't exists
def checkInsertProductVendorURL(vendor_id, vendor_product_id, product_url):
    url = product_url.split('&')[0]
    try:
        if not vendor_product_id:
            logger.warning(f"{vendor_id} >> Invalid vendor_product_id: {vendor_product_id}")
            return  # Exit the function early
        conn = mysql.connector.connect(host=HOST, database=DB, user=USER, password=PASS)
        if conn.is_connected():
            this = conn.cursor(buffered=True)
            checkProductVendorURLQuery = "SELECT vendor_product_id FROM VendorURL WHERE vendor_product_id = %s"
            this.execute(checkProductVendorURLQuery, [vendor_product_id,])
            records = this.fetchall()
            if len(records) == 0:
                insertProductVendorURLQuery = "INSERT INTO VendorURL (vendor_product_id, vendor_raw_url, vendor_url) VALUES (%s, %s, %s)"
                this.execute(insertProductVendorURLQuery, [vendor_product_id, product_url, url])
                conn.commit()
                logger.info(f'{vendor_id} >> Added product vendor URL for vendor_product_id "{vendor_product_id}".')
                return this.lastrowid
            else:
                # fatchquary = "SELECT vendor_url_id, vendor_raw_url, vendor_url FROM VendorURL WHERE vendor_product_id = %s"
                # this.execute(fatchquary, [vendor_product_id])
                # results = this.fetchall()
                # if results[0][2] != url:
                # Update the existing record
                updateProductVendorURLQuery = """UPDATE VendorURL SET vendor_raw_url = %s, vendor_url = %s WHERE vendor_product_id = %s"""
                this.execute(updateProductVendorURLQuery, [product_url, url, vendor_product_id])
                conn.commit()
                logger.info(f'{vendor_id} >> Updated product vendor URL for vendor_product_id "{vendor_product_id}".')
                # else:
                #     logger.info(f'{vendor_id} >> Same Product vendor URL already exists for vendor_product_id "{vendor_product_id}".')
                # try:
                #     vendor_url_id, vendor_raw_url, vendor_url = results[0][0], results[0][1], results[0][2]
                #     checkProductVendorURLQuery = "SELECT vendor_bakup_url_id FROM BuilddotcomeDirectScraping_VendorURLBackup WHERE vendor_product_id = %s"
                #     this.execute(checkProductVendorURLQuery, [vendor_product_id,])
                #     Record = this.fetchone()
                #     if Record is None or len(Record) == 0:
                #         insertProductVendorURLQuery = "INSERT INTO BuilddotcomeDirectScraping_VendorURLBackup (vendor_url_id, vendor_product_id, vendor_raw_url, vendor_url) VALUES (%s, %s, %s, %s)"
                #         this.execute(insertProductVendorURLQuery, [vendor_url_id, vendor_product_id, vendor_raw_url, vendor_url])
                #         conn.commit()
                #         logger.info(f'Added product vendor_url for vendor_product_id "{vendor_product_id}" for vendor_bakup_url_id {this.lastrowid}.')
                #     else:
                #         if Record[0] is not None:
                #             fatchquary = "SELECT vendor_url_id, vendor_raw_url, vendor_url FROM BuilddotcomeDirectScraping_VendorURLBackup WHERE vendor_bakup_url_id = %s"
                #             this.execute(fatchquary, [Record[0],])
                #             Records = this.fetchone()
                #             if Records and Records[2] != vendor_url:
                #                 # Update the existing record
                #                 updateProductVendorURLQuery = """UPDATE BuilddotcomeDirectScraping_VendorURLBackup SET vendor_raw_url = %s, vendor_url = %s WHERE vendor_bakup_url_id = %s"""
                #                 this.execute(updateProductVendorURLQuery, [vendor_raw_url, vendor_url, Record[0]])
                #                 conn.commit()
                #                 logger.info(f'Updated vendor_raw_url, vendor_url for vendor_bakup_url_id "{Record[0]}".')
                #             else:
                #                 logger.info(f'Same Product vendor URL already exists for vendor_bakup_url_id "{Record[0]}".')
                # except mysql.connector.Error as e:
                #     logger.warning(f"MySQL ERROR checkInsertProductVendorURL() >> {e}")
                # results.append(Records)
    except mysql.connector.Error as e:
        logger.warning(f"{vendor_id} >> MySQL ERROR checkInsertProductVendorURL() >> {e}")
    finally:
        if conn.is_connected():
            conn.close()
            this.close()

# call all function into this function
def insertall(product_id, vendor_product_id, temp, vendor_id):
    try:
        vendorTempPricing(vendor_product_id, temp)
        rpVendorPricingHistory(vendor_product_id, temp, vendor_id)
        productMsrpUpdate(product_id, temp)
        productVendorMsrpUpdate(vendor_product_id, temp)
    except Exception as e:
        logger.error(f"Error in insertall(): {e}")

def getDatetime():
    currentDatetime = datetime.now()
    return currentDatetime.strftime("%Y-%m-%d %H:%M:%S")

# Temp vnendor pricing data
def vendorTempPricing(vendor_product_id, temp):
    dateTime = getDatetime()
    try:
        conn = mysql.connector.connect(host=HOST, database=DB, user=USER, password=PASS)
        if conn.is_connected():
            this = conn.cursor(buffered=True)
            checkQuery = "SELECT vendor_product_id FROM TempVendorPricing WHERE vendor_product_id = %s AND source = %s LIMIT 1"
            this.execute(checkQuery, (vendor_product_id, temp['source']))
            records = this.fetchone()
            if records:
                getPricequary = "SELECT * FROM TempVendorPricing WHERE vendor_product_id = %s AND source = 'direct_from_website'"
                this.execute(getPricequary, (records[0],))
                result = this.fetchone()
                savedprice = str(result[2]).strip()
                scrapedprice = str(temp['vendorprice_price']).strip()
                if savedprice == scrapedprice:
                    logger.info(f"Same vendor price already exists for vendor_product_id {vendor_product_id}")
                else:
                    updateQuery = """UPDATE TempVendorPricing SET is_price_changed = %s, price_changed_date = %s WHERE vendor_product_id = %s AND source = %s"""
                    values = ("1", dateTime, vendor_product_id, temp['source'])
                    this.execute(updateQuery, values)
                    conn.commit()
                    logger.info(f"is_price_changed set 1 for vendor_product_id ({vendor_product_id}).")
                updateQuery = """UPDATE TempVendorPricing SET vendorprice_price = %s, vendorprice_finalprice = %s, vendorprice_date = %s, product_condition = %s, is_rp_calculated = %s, is_member = %s, scraped_by_system = %s
                    WHERE vendor_product_id = %s AND source = %s"""
                values = (temp['vendorprice_price'], temp['vendorprice_finalprice'], dateTime, temp['product_condition'], '2', '0', temp['scraped_by_system'], vendor_product_id, temp['source'])
                this.execute(updateQuery, values)
                conn.commit()
                logger.info(f"Record Updated for vendor_product_id ({vendor_product_id}) and source ({temp['source']})")
            else:
                insertQuery = """INSERT INTO TempVendorPricing (vendor_product_id, vendorprice_price, vendorprice_finalprice, vendorprice_date, product_condition, source, is_rp_calculated, is_member, scraped_by_system) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)"""
                values = (vendor_product_id, temp['vendorprice_price'], temp['vendorprice_finalprice'], dateTime, temp['product_condition'], temp['source'], '2', '0', temp['scraped_by_system'])
                this.execute(insertQuery, values)
                conn.commit()
                logger.info(f"Record Inserted for vendor_product_id ({vendor_product_id}) and source ({temp['source']})")
    except mysql.connector.Error as e:
        logger.warning(f"MySQL ERROR vendorTempPricing() >> {e}")
    finally:
        if conn.is_connected():
            conn.close()
            this.close() 

def get_table_structure(host, db, user, password, table_name):
    """Retrieve column details from a table, preserving the column order."""
    try:
        conn = mysql.connector.connect(host=host, database=db, user=user, password=password)
        cursor = conn.cursor()            
        cursor.execute(f"DESCRIBE {table_name}")
        structure = [(row[0], row[1], row[2], row[3], row[4], row[5]) for row in cursor.fetchall()]  
        # (Column Name, Column Type, NULL, Key, Default, Extra)
    except Exception as e:
        logger.error(f"Error fetching table structure for {table_name}: {e}")
        structure = []
    finally:
        cursor.close()
        conn.close()
    return structure

def match_table_structure(source_structure, target_structure):
    """Find missing columns with full definitions and their correct positions."""
    target_columns = {col[0]: col for col in target_structure}  # {Column Name: Column Details}
    missing_columns = []

    for index, column in enumerate(source_structure):
        col_name, col_type, is_null, key, default, extra = column
        if col_name not in target_columns:
            after_column = source_structure[index - 1][0] if index > 0 else None
            missing_columns.append((col_name, col_type, is_null, key, default, extra, after_column))
    if missing_columns and len(missing_columns) > 0:
        logger.info(f"Missing columns: {missing_columns}")
    logger.info(f"History Table is up-to-date.")
    return missing_columns

def rpVendorPricingHistory(vendor_product_id, temp, vendor_id):
    dateTime = getDatetime()
    try:
        # save to AF/HP if vendor_id is one of them
        if vendor_id == 10021 or vendor_id == 10024: conn = mysql.connector.connect(host=HOST2, database=DB2, user=USER2, password=PASS2)
        else: conn = mysql.connector.connect(host=HOST3, database=DB3, user=USER3, password=PASS3)
        if conn.is_connected():
            this = conn.cursor(buffered=True)
            # check if vendor specific vendorPricing table exists or not
            vendor_pricing_table = f"z_{vendor_id}_VendorPricing"
            this.execute(f"""SELECT * 
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_NAME = '{vendor_pricing_table}'
            LIMIT 1""")
            result = this.fetchone()
            source_structure = get_table_structure(HOST, DB, USER, PASS, 'TempVendorPricing')
            if not result:
                logger.info(f"Table {vendor_pricing_table} does not exist. Creating table...")
                column_definitions = []
                primary_key = None  # Store primary key column if exists
                for col_name, col_type, is_null, key, default, extra in source_structure:
                    null_option = "NULL" if is_null == "YES" else "NOT NULL"
                    # Handle default values properly
                    if default is not None:
                        if "timestamp" in col_type.lower() or "datetime" in col_type.lower():
                            default_option = "DEFAULT CURRENT_TIMESTAMP" if default.lower() == "current_timestamp()" else ""
                        else:
                            default_option = f"DEFAULT {repr(default)}"
                    else:
                        default_option = ""
                    extra_option = extra if extra else ""
                    # Ensure AUTO_INCREMENT is properly handled
                    if "auto_increment" in extra.lower():
                        extra_option = "AUTO_INCREMENT"
                        primary_key = col_name  # Store primary key
                    column_definitions.append(f"`{col_name}` {col_type} {null_option} {default_option} {extra_option}")
                create_table_query = f"""
                    CREATE TABLE `{vendor_pricing_table}` (
                        {', '.join(column_definitions)}
                        {f", PRIMARY KEY (`{primary_key}`)" if primary_key else ""}
                    );
                """.strip()
                this.execute(create_table_query)
                conn.commit()
                logger.info(f"Table {vendor_pricing_table} created successfully.")
                logger.info(f"==========================================")
            else:
                if vendor_id == 10021 or vendor_id == 10024:
                    target_structure = get_table_structure(HOST2, DB2, USER2, PASS2, vendor_pricing_table)
                else:
                    target_structure = get_table_structure(HOST3, DB3, USER3, PASS3, vendor_pricing_table)
                missing_columns = match_table_structure(source_structure, target_structure)
                if missing_columns and len(missing_columns) > 0:
                    # Add missing columns if table exists
                    for col_name, col_type, is_null, key, default, extra, after_column in missing_columns:
                        null_option = "NULL" if is_null == "YES" else "NOT NULL"
                        # Handle default values properly
                        if default is not None:
                            if "timestamp" in col_type.lower() or "datetime" in col_type.lower():
                                default_option = "DEFAULT CURRENT_TIMESTAMP" if default.lower() == "current_timestamp()" else ""
                            else:
                                default_option = f"DEFAULT {repr(default)}"
                        else:
                            default_option = ""
                        extra_option = extra if extra else ""
                        after_option = f"AFTER `{after_column}`" if after_column else "FIRST"
                        # Prevent adding AUTO_INCREMENT column incorrectly
                        if "auto_increment" in extra.lower():
                            logger.warning(f"Skipping column `{col_name}` because it has AUTO_INCREMENT.")
                            continue  # Do not add AUTO_INCREMENT column
                        alter_query = f"""
                            ALTER TABLE `{vendor_pricing_table}`
                            ADD COLUMN `{col_name}` {col_type} {null_option} {default_option} {extra_option} {after_option};
                        """.strip()
                        this.execute(alter_query)
                    conn.commit()
                    logger.info(f"Table {vendor_pricing_table} altered successfully.")
                    logger.info(f"==========================================")

            insertQuery = f"""INSERT INTO {vendor_pricing_table} (vendor_product_id, vendorprice_price, vendorprice_finalprice, vendorprice_date, 
                product_condition, source, is_rp_calculated, is_member, scraped_by_system) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (vendor_product_id, temp['vendorprice_price'], temp['vendorprice_finalprice'], dateTime, temp['product_condition'], temp['source'], '2', '0', temp['scraped_by_system'])
            this.execute(insertQuery, values)
            conn.commit()
            logger.info(f"Record Inserted for vendor_product_id ({vendor_product_id}) and source ({temp['source']}) In {vendor_pricing_table} history table.")
    except mysql.connector.Error as e:
        logger.warning(f"MySQL ERROR {vendor_pricing_table} >> {e}")
    finally:
        if conn.is_connected():
            conn.close()
            this.close()

# Updating MSRF in Product table
def productMsrpUpdate(product_id, temp):
    try:
        conn = mysql.connector.connect(host=HOST, database=DB, user=USER, password=PASS)
        if conn.is_connected():
            this = conn.cursor(buffered=True)
            this.execute("SELECT msrp FROM Product WHERE product_id = %s", (product_id,))
            result = this.fetchone()
            if result:
                # Update MSRP
                if temp['msrp']:
                    this.execute("UPDATE Product SET msrp = %s WHERE product_id = %s", (temp['msrp'], product_id))
                    conn.commit()
                    logger.info(f"Record Updated for product_id ({product_id}).")
    except mysql.connector.Error as e:
        logger.warning(f"{product_id} >> MySQL ERROR productMsrpUpdate() >> {e}")
    finally:
        if conn.is_connected():
            conn.close()
            this.close()

# Updating MSRF in ProductVendor table
def productVendorMsrpUpdate(vendor_product_id, temp):
    try:
        conn = mysql.connector.connect(host=HOST, database=DB, user=USER, password=PASS)
        if conn.is_connected():
            this = conn.cursor(buffered=True)
            this.execute("SELECT msrp FROM ProductVendor WHERE vendor_product_id = %s", (vendor_product_id,))
            result = this.fetchone()
            if result:
                # Update MSRP
                if temp['msrp']:
                    this.execute("UPDATE ProductVendor SET msrp = %s WHERE vendor_product_id = %s", (temp['msrp'], vendor_product_id))
                    conn.commit()
                    logger.info(f"Record Updated for vendor_product_id ({vendor_product_id}).")
    except mysql.connector.Error as e:
        logger.warning(f"{vendor_product_id} >> MySQL ERROR productVendorMsrpUpdate() >> {e}")
    finally:
        if conn.is_connected():
            conn.close()
            this.close()

def read_product_urls_from_file(filepath):
    with open(filepath, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def focus_browser_window(window_title_contains="Opera"):
    windows = gw.getWindowsWithTitle(window_title_contains)
    if windows:
        win = windows[0]
        win.activate()
        time.sleep(1)  # Give it a moment to focus

def open_url_human_like(url, window_title_contains="Opera"):
    focus_browser_window(window_title_contains)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1.5)  # Wait for new tab to open
    pyautogui.typewrite(url, interval=0.07)  # Simulate human typing
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(3)  # Wait for page to load (adjust as needed)

if __name__ == "__main__":  
    start = time.perf_counter() 
    catUrllist = [
        "https://www.keithsappliances.com/catalog/special/manufacturer/ge%20profile"
        # "https://www.keithsappliances.com/catalog/special/manufacturer/bosch?srsltid=AfmBOoqL-9K2nA8t_-L4G9J21FIcjZPDQ-ZUoRw22d4McU08Yy58bIjf"
    ]
    vendor_url = "https://www.keithsappliances.com/"
    domain = "https://www.keithsappliances.com"
    vendor_id = 20233 #17672 #20233
    # try:
        # driver = triggerSeleniumOpera(useVPN=False, checkIP=True)
        
        # if driver:
    # for cat_url in catUrllist:
    #     product_urls = getAllProUrl(cat_url)
    #     if not product_urls:
    #         logger.debug(f"No products found for {cat_url}.")
    #     # Use multiprocessing to fetch data for all product URLs in parallel
    #     logger.debug(f"Total {len(product_urls)} products found for {cat_url}.")
    #             # for product_url in product_urls:
    #             #     open_url_human_like(product_url)
                #     fetch_product_data(driver, product_url, vendor_id)
    # try:
        # driver = triggerSelenium(checkIP=True)
        # time.sleep(5)
    product_urls = read_product_urls_from_file("productUrls-GE-Profile.txt")
    if not product_urls:
        logger.debug("No products found in productUrls.txt.")
    else:
        logger.debug(f"Total {len(product_urls)} products found in productUrls.txt.")
        for product_url in product_urls:
            fetch_product_data(product_url,vendor_id)
    # finally:
    #     if driver:
    #         driver.quit()
    finish = time.perf_counter()
    logger.debug(f'Finished ThreadMain in {round(finish - start, 2)} second(s)')
