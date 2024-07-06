import os
import shutil


def convert_annotations(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        shutil.copy(os.path.join(input_dir, filename), output_dir)


if __name__ == "__main__":
    convert_annotations("model/data/raw_annotations", "model/data/processed_annotations")
