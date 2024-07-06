import torch
from model_architecture import get_model


def train_model(data_path, epochs=100):
    model = get_model()
    model.train(data_path, epochs=epochs)


if __name__ == "__main__":
    train_model("model/data/annotated_images")
