from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# If you're using WebDriver Manager:
from webdriver_manager.chrome import ChromeDriverManager

def search_target_selenium(search_query):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Optional: run in headless mode

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    base_url = "https://www.target.com/s?searchTerm="
    driver.get(base_url + search_query)

    # Wait (naive) a few seconds for the page to load
    time.sleep(5)

    # Find all product-title anchors
    title_links = driver.find_elements(By.CSS_SELECTOR, "[data-test='product-title']")

    results = []
    for link in title_links:
        # The text content inside the <a>, which includes <div>
        text_content = link.text

        # The product URL
        product_url = link.get_attribute("href")

        # We store whichever fields you want. Let’s store text and link:
        results.append({
            "name": text_content,
            "url": product_url,
        })

    driver.quit()
    return results

if __name__ == "__main__":
    query = "Scarlet & Violet 151"
    products = search_target_selenium(query)

    print(f"Search results for '{query}':")
    for idx, product in enumerate(products, start=1):
        print(
            f"{idx}. {product['name']}\n"
            f"   URL: {product['url']}\n"
        )
