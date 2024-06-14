from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

def scroll_to_bottom(driver):
    """Función para realizar scroll hasta el final de la página."""
    old_position = driver.execute_script("return window.scrollY")
    while True:
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(3)  # Ajusta según la latencia de la red y la velocidad de respuesta del servidor
        new_position = driver.execute_script("return window.scrollY")
        if new_position == old_position:
            break
        old_position = new_position

# Inicializar el WebDriver
driver = webdriver.Chrome()

# Acceder a la página web
driver.get("https://www.perueduca.pe/#/home/materiales-educativos/inicial/herramientas-pedagogicas-inicial")
driver.implicitly_wait(5)

element = driver.find_element(By.XPATH, '//p[contains(text(), "Estudiante")]')
element.click()
time.sleep(3)

# Realizar scroll hacia abajo para asegurar que todos los elementos están cargados
scroll_to_bottom(driver)

# Esperar explícitamente a que los elementos deseados estén visibles
WebDriverWait(driver, 20).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".container-result-cards app-card-education-material"))
)

# Buscar todos los divs que contienen los títulos de artículos
article_titles_elements = driver.find_elements(By.CSS_SELECTOR, ".container-result-cards app-card-education-material .title-article div")

# Extraer el texto de cada elemento encontrado
article_titles = [element.text for element in article_titles_elements]

# Guardar los títulos extraídos en un archivo JSON
with open('extracted_titles.json', 'w', encoding='utf-8') as file:
    json.dump(article_titles, file, ensure_ascii=False ,indent=4 )

print(f"Títulos guardados en 'extracted_titles.json'. Encontrados {len(article_titles)} títulos.")

# Cerrar el navegador
driver.quit()
