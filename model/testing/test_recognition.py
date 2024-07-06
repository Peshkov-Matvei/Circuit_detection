import unittest
from recognition.recognize_elements import recognize_elements
from model.load_pretrained_model import load_pretrained_model


class TestRecognition(unittest.TestCase):
    def test_recognition(self):
        model = load_pretrained_model("yolov5s.pt")
        results = recognize_elements(model, "../data/test_images/sample.jpg")
        self.assertIsNotNone(results)

if __name__ == "__main__":
    unittest.main()
