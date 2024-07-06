import torch


def load_pretrained_model(model_path="yolov5s"):
    model = torch.hub.load('ultralytics/yolov5', model_path)
    return model


if __name__ == "__main__":
    model = load_pretrained_model("yolov5s")
    print("Model loaded successfully")
