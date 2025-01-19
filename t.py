import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    # Configure Chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Headless mode
    chrome_options.add_argument("--no-sandbox")  # Needed in some Linux environments
    chrome_options.add_argument(
        "--disable-dev-shm-usage"
    )  # Avoid memory issues
    chrome_options.add_argument("--disable-gpu")  # Disable GPU (optional)

    # Initialize WebDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(driver_version="132.0.6834.83").install()),
        options=chrome_options,
    )
    driver.get("https://br.investing.com/indices/bloomberg-commodity-historical-data")
    # Wait until a specific element is present on the page (you can choose any element that signals page load)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "logo")))  # Wait for the logo to appear as an example
    return driver


def main():
    # Start the driver and wait for the page to load
    driver = setup_driver()

    fullxpath = "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]"
    element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, fullxpath)))
    element.click()

    fullxpath = "/html/body/div[4]/div/div/form/div/button"
    element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, fullxpath)))
    element.click()

    fullxpath = "/html/body/div[4]/div/div/form/div/button"
    element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, fullxpath)))
    element.click()

    # url = f'https://api.investing.com/api/financialdata/historical/948434?start-date=1991-01-19&end-date=2025-01-19&time-frame=Monthly&add-missing-rows=false'

    # headers = {
    #     "accept": "*/*",
    #     "accept-encoding": "gzip, deflate, br, zstd",
    #     "accept-language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    #     "content-type": "application/json",
    #     "domain-id": "www",
    #     "origin": "https://br.investing.com/indices/bloomberg-commodity-historical-data",
    #     "referer": "https://br.investing.com/indices/bloomberg-commodity-historical-data",
    #     "sec-fetch-dest": "empty",
    #     "sec-fetch-mode": "cors",
    #     "sec-fetch-site": "same-site",
    #     "user-agent": "Mozilla/5.0"
    # }


    # Now you can make the GET request
    # response = requests.get(url, headers=headers)

    # # Print the status code
    # print("Status Code:", response.status_code)

    driver.quit()


if __name__ == "__main__":
    main()