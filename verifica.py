from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import json
import time

def fetch_data(driver, url):
    # Attempt to fetch page elements based on the provided URL
    try:
                element = driver.find_element(By.XPATH, '//p[contains(text(), "Directivo")]')
                element.click()
                time.sleep(3)
    except Exception as e :
        try:
            driver.get(url)
            driver.implicitly_wait(10)  # Implicit wait

            # Checking for 'Página no encontrada'
            not_found = driver.find_elements(By.CSS_SELECTOR, ".not-found__header")
            if not_found:
                print(f"Página no encontrada for {url}")
                return "Página no encontrada"

            # Extracting details if page is found
            data = {
                'Autor': driver.find_element(By.XPATH, '//div[contains(text(), "Autor:")]/following-sibling::div').text,
                'Resumen': driver.find_element(By.XPATH, '//div[contains(text(), "Resumen:")]/following-sibling::div').text,
                'Tema': driver.find_element(By.XPATH, '//div[contains(text(), "Tema:")]/following-sibling::div').text,
                'Anio': driver.find_element(By.XPATH, '//div[contains(text(), "Año:")]/following-sibling::div').text,
                'Fuente': driver.find_element(By.XPATH, '//div[contains(text(), "Fuente:") and not(contains(text(), "Idioma"))]/following-sibling::div').text,
                'Idioma': driver.find_element(By.XPATH, '//div[contains(text(), "Idioma/Lengua:")]/following-sibling::div').text,
                'Estrategia': driver.find_element(By.XPATH, '//div[contains(text(), "Estrategia:")]/following-sibling::div').text,
                'Competencia': driver.find_element(By.XPATH, '//div[contains(text(), "Competencia:")]/following-sibling::div').text,
                'Enfoques': driver.find_element(By.XPATH, '//div[contains(text(), "Enfoques:")]/following-sibling::div').text
            }
            return data
        except Exception as e:
            print(f"Error processing {url}: {e}")
            return {}

def main():
    with open('./Json/url-titles.json', 'r') as file:
        titles = json.load(file)

    # WebDriver setup
    driver = webdriver.Chrome()

    results = {}
    base_url = "https://www.perueduca.pe/#/home/materiales-educativos/detalle/"
    for title in titles:
        full_url = f"{base_url}{title}"
        result = fetch_data(driver, full_url)
        results[title] = result
        print(f"Data fetched for {title}")

    # Save results to JSON
    with open('datos-completos.json', 'w', encoding='utf-8') as outfile:
        json.dump(results, outfile, ensure_ascii=False, indent=4)

    driver.quit()

if __name__ == "__main__":
    main()
