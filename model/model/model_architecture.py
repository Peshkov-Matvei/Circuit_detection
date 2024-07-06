import torch


def get_model():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    return model
