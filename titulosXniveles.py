import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import json

def scrape_titles(educational_levels):
    # Configuración del WebDriver con WebDriver Manager
    driver = webdriver.Chrome()
    
    all_titles = {}

    for level in educational_levels:
        # Construir la URL dinámicamente basada en el nivel educativo
        url = f"https://www.perueduca.pe/#/home/materiales-educativos/{level}"
        driver.get(url)
        
        # Esperar que la página cargue inicialmente
        driver.implicitly_wait(10)  # Espera implícita de 10 segundos
        driver.refresh()
        time.sleep(10)

        # Encontrar todos los elementos que contienen títulos
        titles = driver.find_elements(By.XPATH, '//app-collection-card//p[contains(@class, "title col-12")]')
        titles_text = [title.text for title in titles]

        # Agregar los títulos al diccionario con la clave siendo el nivel educativo
        all_titles[level] = titles_text

    # Guardar todos los títulos en un archivo JSON
    with open('all-titles.json', 'w', encoding='utf-8') as file:
        json.dump(all_titles, file, ensure_ascii=False, indent=4)

    print("Todos los títulos guardados en 'all-titles.json'.")

    # Cerrar el navegador
    driver.quit()

# Ejemplo de cómo llamar a la función
scrape_titles(['inicial', 'primaria', 'secundaria'])
