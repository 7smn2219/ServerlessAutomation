import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def main():
    print("Starting headless Selenium scraping...")

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")

    # Setup ChromeDriver service
    service = Service(ChromeDriverManager().install())

    # Initialize WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to a website
        url = 'https://github.com/google-gemini/gemini-cli'

        print(f"Navigating to {url}")
        driver.get(url)

        # Print page title
        print(f"Page title: {driver.title}")

        # Take a screenshot (optional)
        driver.save_screenshot("screenshot.png")
        print("Screenshot saved as screenshot.png")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    main()
