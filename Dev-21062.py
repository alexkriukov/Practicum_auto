import time
from array import array
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_url(language_code: str) -> str:
    """Returns the URL for the given language code."""
    base_url = 'https://growth-nm-meow-team.stands.team.practicum.com/'
    return f"{base_url}en-{language_code}"

def verify_url(url: str, language_code_redirected: str) -> None:
    """Verifies that the given URL is the expected URL for the given language code."""
    expected_url = f"https://growth-nm-meow-team.stands.team.practicum.com/en-{language_code_redirected}/"
    if url == expected_url:
        print(f"OK URL for {language_code_redirected}")
    else:
        print(f"Bad URL for {language_code_redirected}")

chrome_service = Service('C:\\selenium_course\\python\\venv\\123\\Selenium\\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

with webdriver.Chrome(options=options, service=chrome_service) as chrome_driver:
    language_codes = ["phl", "sea", "nga", "gha","zmb", "mys/data-analyst-beta", "mys/data-scientist-beta"]
    language_codes_redirected = ["mys", "mys", "afr", "afr","afr", "mys/data-analyst", "mys/data-scientist"]
    for i, code in enumerate(language_codes):
        url = get_url(code)
        print(url)
        chrome_driver.get(url)
        try:
            wait = WebDriverWait(chrome_driver, 10)
            current_url = chrome_driver.current_url
            print(current_url)
            verify_url(current_url, language_codes_redirected[i])
        except Exception as e:
            print(f"Error finding right redirect {language_codes_redirected[i]}")
