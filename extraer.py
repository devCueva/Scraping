from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json

options = Options()
options.headless = True  # Activar modo sin cabez
# Leer las URLs desde un archivo JSON
with open('./Json/verifia.json', 'r') as file:
    urls = json.load(file)

# Inicializar el WebDriver
driver = webdriver.Chrome(options=options)

# Resultados
results = []

# Procesar cada URL
for url in urls:
    # Abrir la página
    driver.get(url)
    driver.implicitly_wait(12)  # Espera implícita
    # Intenta encontrar los elementos y capturar la información
    element = driver.find_element(By.XPATH, '//div[contains(text(), "Ficha informativa")]')
    element.click()
    time.sleep(10)
    try:
        data = {
            'Autor': driver.find_element(By.XPATH, '//div[contains(text(), "Autor:")]/following-sibling::div').text,
            'Resumen': driver.find_element(By.XPATH, '//div[contains(text(), "Resumen:")]/following-sibling::div').text,
            'Tema': driver.find_element(By.XPATH, '//div[contains(text(), "Tema:")]/following-sibling::div').text,
            'Anio': driver.find_element(By.XPATH, '//div[contains(text(), "Año:")]/following-sibling::div').text,
            'Fuente': driver.find_element(By.XPATH, '//div[contains(text(), "Fuente:") and not(contains(text(), "Idioma"))]/following-sibling::div').text,
            'Idioma': driver.find_element(By.XPATH, '//div[contains(text(), "Idioma/Lengua:")]/following-sibling::div').text,
            # 'Estrategia': driver.find_element(By.XPATH, '//div[contains(text(), "Estrategia:")]/following-sibling::div').text,
            # 'Competencia': driver.find_element(By.XPATH, '//div[contains(text(), "Competencia:")]/following-sibling::div').text,
            # 'Enfoques': driver.find_element(By.XPATH, '//div[contains(text(), "Enfoques:")]/following-sibling::div').text
        }
        results.append(data)
    except Exception as e:
        print(f"Error procesando la URL {url}: {e}")

# Guardar los resultados en un archivo JSON
with open('data_output.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, ensure_ascii=False, indent=4)

# Cerrar el navegador
driver.quit()
