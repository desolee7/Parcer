from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os
from tqdm import tqdm
from PIL import Image
import urllib
import urllib.request



# Функция для создания директории, если она не существует
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# Функция для загрузки изображения по URL
def download_image(url, folder_path):
    # Создаем папку, если она не существует
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Получаем имя файла из URL
    filename = os.path.join(folder_path, url.split("/")[-2])

    # Запрос к URL для загрузки данных
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Записываем содержимое ответа в файл
        with open(filename, 'wb') as f:
            f.write(response.content)
        #print("Изображение успешно скачано и сохранено в", filename)
    else:
        print("Не удалось скачать изображение. Код ответа:", response.status_code)


# Функция для скачивания изображений с сайта
def download_images(url, folder_id, limit):
    # Создание директории для сохранения изображений
    create_directory(folder_id)

    # Счетчик скачанных изображений
    count = 0
    print(count)
    # Инициализация веб-драйвера
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.headless = False  # Отображение браузера (True - скрытый режим)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Открываем страницу
        driver.get(url)

        # Пауза для загрузки контента
        time.sleep(5)

        # Цикл прокрутки страницы до тех пор, пока не будет скачано достаточное количество изображений
        pbar = tqdm(total=limit, desc=f'Скачивание для папки {folder_id}')
        while count < limit:
            # Прокручиваем страницу вниз
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Пауза для загрузки контента

            # Получаем HTML-код страницы
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            # Поиск всех элементов с классом "item__img"
            img_divs = soup.find_all('a', class_='_1286nb1h _1286nb1k _1286nb14jx _1286nb14l9 _1286nb14ml _1286nb14nx _1286nb189 _1286nb199 _1286nb19x _1286nb1yx _1286nb13df _1286nb13kr')

            # Перебор найденных элементов
            for img_div in img_divs:
                # Получение тега <img>
                img_tag = img_div.find('img')

                if img_tag:
                    # Получение URL изображения из атрибута src
                    img_url = img_tag.get('src')
                    print(img_url)
                    if img_url:
                        # Загрузка изображения

                        # download_image(img_url, str(folder_id))
                        
                        # Увеличиваем счетчик скачанных изображений
                        count += 1
                        pbar.update(1)
                        filename = os.path.join(folder_id, f"{count}.jpg")
                        urllib.request.urlretrieve(img_url, filename)
                        if count >= limit:
                            break

        pbar.close()
        print(f"Скачивание для папки {folder_id} завершено.")
    finally:
        # Закрываем браузер после завершения работы
        driver.quit()


# URL сайтов и количество изображений для скачивания
sites = [
    {"url": "https://ru.freepik.com/search?ai=excluded&format=search&last_filter=query&last_value=олени+на+природе&people=exclude&query=олени+на+природе&selection=1&type=photo", "folder_id": "1", "limit": 50},
    {"url": "https://ru.freepik.com/search?ai=excluded&format=search&last_filter=page&last_value=2&page=2&people=exclude&query=олени+на+природе&selection=1&type=photo#uuid=eb36b8ac-f934-4491-86d0-d0708151b735", "folder_id": "2", "limit": 50},
    {"url": "https://ru.freepik.com/search?ai=excluded&format=search&last_filter=page&last_value=3&page=3&people=exclude&query=олени+на+природе&selection=1&type=photo#uuid=eb36b8ac-f934-4491-86d0-d0708151b735", "folder_id": "3", "limit": 50},
    {"url": "https://ru.freepik.com/search?ai=excluded&format=search&last_filter=page&last_value=4&page=4&people=exclude&query=олени+на+природе&selection=1&type=photo#uuid=eb36b8ac-f934-4491-86d0-d0708151b735", "folder_id": "4", "limit": 50},
    {"url": "https://ru.freepik.com/search?ai=excluded&format=search&last_filter=page&last_value=5&page=5&people=exclude&query=олени+на+природе&selection=1&type=photo#uuid=eb36b8ac-f934-4491-86d0-d0708151b735", "folder_id": "5", "limit": 50},
    {"url": "https://ru.freepik.com/search?ai=excluded&format=search&last_filter=page&last_value=6&page=6&people=exclude&query=олени+на+природе&selection=1&type=photo#uuid=eb36b8ac-f934-4491-86d0-d0708151b735", "folder_id": "6", "limit": 50},
    {"url": "https://ru.freepik.com/search?ai=excluded&format=search&last_filter=page&last_value=7&page=7&people=exclude&query=олени+на+природе&selection=1&type=photo#uuid=eb36b8ac-f934-4491-86d0-d0708151b735", "folder_id": "7", "limit": 50},
    {"url": "https://ru.freepik.com/search?ai=excluded&format=search&last_filter=page&last_value=8&page=8&people=exclude&query=олени+на+природе&selection=1&type=photo#uuid=eb36b8ac-f934-4491-86d0-d0708151b735", "folder_id": "8", "limit": 50},
    {"url": "https://ru.freepik.com/search?ai=excluded&format=search&last_filter=page&last_value=9&page=9&people=exclude&query=олени+на+природе&selection=1&type=photo#uuid=eb36b8ac-f934-4491-86d0-d0708151b735", "folder_id": "9", "limit": 50},
    {"url": "https://ru.freepik.com/search?ai=excluded&format=search&last_filter=page&last_value=10&page=10&people=exclude&query=олени+на+природе&selection=1&type=photo#uuid=eb36b8ac-f934-4491-86d0-d0708151b735", "folder_id": "10", "limit": 50},
    {"url": "https://ru.freepik.com/search?ai=excluded&format=search&last_filter=page&last_value=11&page=11&people=exclude&query=олени+на+природе&selection=1&type=photo#uuid=eb36b8ac-f934-4491-86d0-d0708151b735", "folder_id": "11", "limit": 50},
    {"url": "https://ru.freepik.com/search?ai=excluded&format=search&last_filter=page&last_value=12&page=12&people=exclude&query=олени+на+природе&selection=1&type=photo#uuid=eb36b8ac-f934-4491-86d0-d0708151b735", "folder_id": "12", "limit": 50}
]

# Скачивание изображений для каждого сайта
for site in sites:
    download_images(site['url'], site['folder_id'], site['limit'])

