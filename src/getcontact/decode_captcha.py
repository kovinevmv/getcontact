import base64
import random
import string

import numpy as np
import pytesseract
import cv2


class CaptchaDecode:
    def __init__(self):
        pass

    def decode_response(self, response):
        image_b64 = response['result']['image']
        image_data = self.decode_b64(image_b64)
        path = self.generate_random_name()
        self.write_data_image(image_data, path)
        return self.decrypt(path), path

    def decode_path(self, path):
        return self.decrypt(path)

    @staticmethod
    def generate_random_name():
        return 'captcha/' + ''.join([random.choice(string.ascii_letters) for _ in range(10)]) + '.jpg'

    @staticmethod
    def write_data_image(data, path):
        with open(path, 'wb') as f:
            f.write(data)

    @staticmethod
    def decode_b64(data):
        return base64.b64decode(data)

    def decrypt(self, path):
        frame = cv2.imread(path)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, np.array([30, 120, 0]), np.array([255, 255, 255]))
        return pytesseract.image_to_string(mask)
