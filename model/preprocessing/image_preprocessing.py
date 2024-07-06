import cv2
import os


def preprocess_images(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        img = cv2.imread(os.path.join(input_dir, filename))
        if img is not None:
            resized_img = cv2.resize(img, (640, 640))
            cv2.imwrite(os.path.join(output_dir, filename), resized_img)


if __name__ == "__main__":
    preprocess_images("model/data/raw_images", "model/data/anntoated_images")
