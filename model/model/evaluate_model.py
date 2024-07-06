import torch
from load_pretrained_model import load_pretrained_model
import os

def evaluate_model(model, data_path, conf_threshold=0.25):
    """
    Функция для оценки производительности модели YOLOv5 на тестовых данных.

    Args:
        model: Загруженная модель YOLOv5.
        data_path (str): Путь к каталогу с тестовыми изображениями.
        conf_threshold (float): Порог уверенности для вывода результатов (по умолчанию 0.25).
    """
    # Установка порога уверенности
    model.conf = conf_threshold

    # Список файлов с тестовыми изображениями
    test_images = [os.path.join(data_path, img) for img in os.listdir(data_path) if img.endswith(('.jpg', '.png', '.jpeg'))]

    # Проведение оценки на каждом изображении
    for img_path in test_images:
        results = model(img_path)
        results.print()  # Вывод результатов в консоль
        results.show()   # Визуализация результатов

    # Вывод сводки по результатам
    results = model(test_images)
    results.print()
    results.save(save_dir='evaluation_results')

if __name__ == "__main__":
    model = load_pretrained_model("yolov5s")

    data_path = "../data/test_images"

    evaluate_model(model, data_path)
