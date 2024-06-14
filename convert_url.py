import json
import unidecode

# Ruta del JSON original
ruta_json_original = "./Json/extracted_titles_totales.json"

# Ruta para guardar el JSON extraído
ruta_json_extraido = "./Json/url-titles.json"

def normalizar_texto(texto):
    # Convertir a minúsculas
    texto = texto.lower()
    # Eliminar tildes
    texto = unidecode.unidecode(texto)
    # Reemplazar 'años' y 'año' por 'anios' y 'anio'
    texto = texto.replace('años', 'anios')
    # Reemplazar caracteres especiales y espacios por '-'
    texto = texto.replace(' ', '-').replace(':', '-').replace('/', '-').replace(',','-').replace('.','-').replace('(','-').replace(')','-').replace('¿','-').replace('?','-').replace('\\','-').replace('"','-')
    # Eliminar guiones múltiples
    while '--' in texto:
        texto = texto.replace('--', '-')
    # Eliminar guiones al final de la cadena
    texto = texto.rstrip('-')
    return texto

def extraer_y_procesar_titles(json_data):
    titles_list = []
    for key, entries in json_data.items():
        for entry in entries:
            if 'titles' in entry:
                titles_list.extend([normalizar_texto(title) for title in entry['titles']])
    return titles_list

def guardar_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    with open(ruta_json_original, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    processed_titles = extraer_y_procesar_titles(data)
    guardar_json(processed_titles, ruta_json_extraido)
    print("Se han procesado y guardado todos los títulos en url-titles.json")

if __name__ == "__main__":
    main()
