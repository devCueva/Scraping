from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import json
import time

def scroll_to_bottom(driver):
    """Función para realizar scroll hasta el final de la página con pausas más largas."""
    old_position = driver.execute_script("return window.scrollY")
    while True:
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        # Esperar 3 segundos antes de verificar si se ha alcanzado el fondo
        time.sleep(3)
        new_position = driver.execute_script("return window.scrollY")
        if new_position == old_position:
            break
        old_position = new_position

def extract_data_from_urls(urls_file):
    # Configuración del WebDriver
    driver = webdriver.Chrome()
    
    # Cargar los datos de URL desde el archivo JSON
    with open(urls_file, 'r', encoding='utf-8') as file:
        urls_data = json.load(file)
    
    all_data = {}

    for level, urls in urls_data.items():
        level_data = []
        for url in urls:
            print(f"Procesando URL: {url}")
            driver.get(url)
            driver.implicitly_wait(5)

            try:
                element = driver.find_element(By.XPATH, '//p[contains(text(), "Directivo")]')
                element.click()
                time.sleep(3)
            except NoSuchElementException:
                print("Elemento 'Directivo' no encontrado, continuando con el scroll y la extracción de datos.")

            scroll_to_bottom(driver)

            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".container-result-cards app-card-education-material"))
            )

            article_titles_elements = driver.find_elements(By.CSS_SELECTOR, ".container-result-cards app-card-education-material .title-article div")
            article_titles = [element.text for element in article_titles_elements]

            level_data.extend(article_titles)
            driver.refresh()
        
        all_data[level] = level_data

    with open('extracted_titles_totales.json', 'w', encoding='utf-8') as file:
        json.dump(all_data, file, ensure_ascii=False, indent=4)

    print("Datos extraídos guardados en 'extracted_titles_totales_2.json'.")
    
    driver.quit()

# Llamar a la función con el nombre del archivo JSON que contiene las URLs
extract_data_from_urls('urls.json')
