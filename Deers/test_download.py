import requests
import os

# Функция для загрузки изображения по URL и сохранения в папку
def download_image(url, folder_path):
    try:
        # Создаем папку, если она не существует
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


        
        # Получаем имя файла из URL
        filename = os.path.join(folder_path, "image.jpg")

        # Запрос к URL для загрузки данных
        print(f"Пытаюсь загрузить изображение по URL: {url}")
        response = requests.get(url, stream=True)

        # Проверяем успешность запроса
        if response.status_code == 200:
            # Записываем содержимое ответа в файл
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Изображение успешно скачано и сохранено в {filename}")
        else:
            print("Не удалось скачать изображение. Код ответа:", response.status_code)
    except Exception as e:
        print("Ошибка:", e)

# Пример использования
image_url = "https://img.freepik.com/free-photo/two-deer-with-beautiful-horns-foggy-valley_181624-6410.jpg?semt=ais"
save_path = "C:\deer"
download_image(image_url, save_path)
