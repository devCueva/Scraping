import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Leer las URLs desde el archivo JSON
with open('resultados.json', 'r') as file:
    urls = json.load(file)

# Inicializar el navegador web (asegúrate de tener el driver de Selenium en tu PATH)
driver = webdriver.Chrome()

# Diccionario para almacenar los resultados
resultados = {}

# Iterar sobre las URLs
for url in urls:
    try:
        # Cargar la URL
        driver.get(url)

        time.sleep(1)
        
        # Verificar si el elemento existe
        elemento = driver.find_element(By.XPATH, '//div[contains(text(), "Ficha informativa")]')
        
        # Si se encuentra el elemento, agregar 'si existe' al resultado
        resultados[url] = "si existe"
    except:
        # Si no se encuentra el elemento, agregar 'no ingresa' al resultado
        resultados[url] = "no ingresa"

# Cerrar el navegador
driver.quit()

# Guardar los resultados en un archivo JSON
with open('verificado_2.json', 'w') as file:
    json.dump(resultados, file, indent=4)

print("¡Proceso completado! Los resultados se han guardado en 'verificado.json'.")
