from PIL import Image
import os
import glob

# Получаем путь к папке, где находится скрипт
folder_path = os.path.dirname(os.path.abspath(__file__))
print(folder_path)
# # Получаем список всех .jpeg файлов в папке
# jpeg_files = glob.glob(os.path.join(folder_path, "*.jpeg"))

# # Сортируем файлы по дате изменения (от самого старого к самому новому)
# jpeg_files.sort(key=lambda x: os.path.getmtime(x))

# # Переименовываем файлы
# for index, file_path in enumerate(jpeg_files, start=1):
#     # Формируем новое имя файла
#     new_name = os.path.join(folder_path, f"{index}.jpeg")
    
#     # Переименовываем файл
#     os.rename(file_path, new_name)

# print("Переименование завершено.")


# def resize_image(input_path, output_path, scale_percent):
#     """
#     Уменьшает изображение на указанный процент.
    
#     :param input_path: Путь к исходному изображению.
#     :param output_path: Путь для сохранения уменьшенного изображения.
#     :param scale_percent: Процент от исходного размера для уменьшения (например, 50 для уменьшения до 50%).
#     """
#     with Image.open(input_path) as img:
#         # Рассчитываем новый размер
#         new_width = int(img.width * scale_percent / 100)
#         new_height = int(img.height * scale_percent / 100)
        
#         # Изменяем размер изображения
#         resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        
#         # Сохраняем уменьшенное изображение
#         resized_img.save(output_path, "JPEG", quality=85)

# def process_directory(scale_percent=50):
#     """
#     Уменьшает все изображения в текущей папке на указанный процент.
    
#     :param scale_percent: Процент уменьшения от исходного размера.
#     """
#     current_dir = os.getcwd()  # Текущая рабочая директория
#     output_dir = os.path.join(current_dir, "resized")  # Папка для уменьшенных изображений
    
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
    
#     for filename in os.listdir(current_dir):
#         if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
#             input_path = os.path.join(current_dir, filename)
#             output_path = os.path.join(output_dir, filename)
#             resize_image(input_path, output_path, scale_percent)
#             print(f"Изображение {filename} уменьшено на {scale_percent}% и сохранено в {output_path}")

# # Пример использования
# scale_percent = 50  # Процент уменьшения от исходного размера (например, 50% от исходного размера)
# process_directory(scale_percent)
