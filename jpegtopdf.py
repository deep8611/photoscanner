from PIL import Image
import os

def images_to_pdf(output_pdf):
    """
    Объединяет все изображения JPEG в текущей директории в один PDF файл,
    сортируя их по возрастанию номеров в названии файла (например, 1.jpeg, 2.jpeg, ...).
    
    :param output_pdf: Имя выходного PDF файла.
    """
    current_dir = os.getcwd()  # Текущая рабочая директория
    print(current_dir)
    image_files = [f for f in os.listdir(current_dir) if f.lower().endswith(".jpg") or f.lower().endswith(".jpeg")]
    
    # Сортировка по числовому значению в имени файла
    image_files.sort(key=lambda f: int(os.path.splitext(f)[0]))  # Извлекаем числовую часть имени файла
    
    if not image_files:
        print("Нет изображений JPEG для объединения.")
        return
    
    images = []
    
    for image_file in image_files:
        img = Image.open(image_file)
        # Преобразуем изображение в RGB (для сохранения в PDF)
        img = img.convert("RGB")
        images.append(img)
    
    # Сохраняем первый файл и добавляем остальные
    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"PDF файл '{output_pdf}' успешно создан с {len(images)} изображениями.")

output_pdf = "output.pdf"  # Имя для выходного PDF файла
images_to_pdf(output_pdf)
