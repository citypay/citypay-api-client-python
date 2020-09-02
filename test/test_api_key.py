import unittest
from datetime import datetime
from typing import Any

import citypay
from citypay.models.api_key import *


class TestApiKey(unittest.TestCase):

    def testGenerate(self):
        dt = datetime.strptime("2020-01-01 09:23:12", "%Y-%m-%d %H:%M:%S")
        key = api_key_generate_for("PC2", "7G79TG62BAJTK669", bytearray.fromhex("acb875aef083de292299bd69fcdeb5c5"), dt)
        self.assertEqual("UEMyOkFDQjg3NUFFRjA4M0RFMjkyMjk5QkQ2OUZDREVCNUM1Ol6Q3tCMPsYvqNhFelRD2zQHYlZquBGCY/6ZpZ0AngTF",key)

        self.assertIsNotNone(api_key_generate("PC2", "LK"))
