from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import json

# Inicializar el WebDriver
driver = webdriver.Chrome()

# Abrir la página
driver.get('https://www.perueduca.pe/#/home/materiales-educativos/detalle/yo-tambien-me-cuido-aprendo-en-casa-2021-tv-inicial-26-de-abril')

# Esperar que la página cargue (opcional, dependiendo del caso)
driver.implicitly_wait(10)  # Espera implícita de 10 segundos

# Seleccionar el elemento que contiene el texto "Ficha informativa"
element = driver.find_element(By.XPATH, '//div[contains(text(), "Ficha informativa")]')
element.click()
time.sleep(10)

# Acciones adicionales, por ejemplo, imprimir el texto del elemento
print(element.text)

data = {
    'Autor': driver.find_element(By.XPATH, '//div[contains(text(), "Autor:")]/following-sibling::div').text,
    'Resumen': driver.find_element(By.XPATH, '//div[contains(text(), "Resumen:")]/following-sibling::div').text,
    'Tema': driver.find_element(By.XPATH, '//div[contains(text(), "Tema:")]/following-sibling::div').text,
    'Anio': driver.find_element(By.XPATH, '//div[contains(text(), "Año:")]/following-sibling::div').text,
    'Fuente': driver.find_element(By.XPATH, '//div[contains(text(), "Fuente:") and not(contains(text(), "Idioma"))]/following-sibling::div').text,
    'Idioma': driver.find_element(By.XPATH, '//div[contains(text(), "Idioma/Lengua:")]/following-sibling::div').text
    #'Estrategia': driver.find_element(By.XPATH, '//div[contains(text(), "Estrategia:")]/following-sibling::div').text,
    #'Competencia': driver.find_element(By.XPATH, '//div[contains(text(), "Competencia:")]/following-sibling::div').text,
    #'Enfoques': driver.find_element(By.XPATH, '//div[contains(text(), "Enfoques:")]/following-sibling::div').text
}
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
# Cerrar el navegador
driver.quit()
