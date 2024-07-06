import torch
from load_pretrained_model import load_pretrained_model


def recognize_elements(model, image_path):
    results = model(image_path)
    return results


if __name__ == "__main__":
    model = load_pretrained_model("../data/models/yolov5s.pt")
    results = recognize_elements(model, "../data/test_images/sample.jpg")
    results.show()
