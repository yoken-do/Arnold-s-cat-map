from PIL import Image
import os
import re

image_folder = '.'

images = []

def extract_number(filename):
    match = re.search(r'_(\d+)\.', filename)
    return int(match.group(1)) if match else float('inf')

for filename in sorted(os.listdir(image_folder), key=extract_number):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):  # Поддерживаемые форматы
        img_path = os.path.join(image_folder, filename)
        img = Image.open(img_path)
        images.append(img)
        print(f"Добавлен файл {filename}")  # Выводим имя добавленного файла

if images:
    # Сохраняем в формате GIF
    images[0].save('output.gif',
                   save_all=True,
                   append_images=images[1:],
                   duration=100,  # Время между кадрами в миллисекундах
                   loop=0)  # 0 - бесконечный цикл
    print("GIF успешно создан: output.gif")
else:
    print("В текущей директории нет изображений для создания GIF.")