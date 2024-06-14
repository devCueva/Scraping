import json
import urllib.parse

def load_titles(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def generate_urls(titles_data):
    base_url = "https://www.perueduca.pe/#/home/materiales-educativos/"
    all_urls = {}
    
    for level, titles in titles_data.items():
        level_urls = []
        for title in titles:
            # Convertir título a URL-friendly string (reemplazando espacios con guiones y codificación de caracteres especiales)
            full_url = f"{base_url}{level}/{title}"
            level_urls.append(full_url)
        
        all_urls[level] = level_urls
    
    return all_urls

def save_urls(urls, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(urls, file, indent=4)

# Suponiendo que el archivo JSON con títulos se llama 'titles.json'
titles_data = load_titles('all-titles.json')
urls = generate_urls(titles_data)
save_urls(urls, 'urls.json')

print("URLs guardadas en 'urls.json'.")
