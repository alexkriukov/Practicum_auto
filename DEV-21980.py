import time
from array import array
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_url(language_code: str) -> str:
    """Returns the URL for the given language code."""
    base_url = 'https://growth-nm-meow-team.stands.team.practicum.com/try/career-advisor/'
    return f"{base_url}?country=es-{language_code}"

def verify_url(url: str, language_code: str) -> None:
    """Verifies that the given URL is the expected URL for the given language code."""
    expected_url = f"https://growth-nm-meow-team.stands.team.practicum.com/es-{language_code}/"
    if url == expected_url:
        print(f"OK URL for {language_code}")
    else:
        print(f"Bad URL for {language_code}")

chrome_service = Service('C:\\selenium_course\\python\\venv\\123\\Selenium\\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

with webdriver.Chrome(options=options, service=chrome_service) as chrome_driver:
    language_codes = ["ecu", "mex", "per", "chl"]
    for code in language_codes:
        url = get_url(code)
        print(url)
        chrome_driver.get(url)
        try:
            back_button = chrome_driver.find_element(By.CSS_SELECTOR, ".link")
            wait = WebDriverWait(chrome_driver, 10)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".link")))
            back_button.click()
            current_url = chrome_driver.current_url
            verify_url(current_url, code)
        except Exception as e:
            print(f"Error finding or clicking back button for {code}: {e}")
