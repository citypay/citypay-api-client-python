import unittest

from citypay.utils.direct_post_mac import direct_post_create_mac, verify


class TestDirectPostMac(unittest.TestCase):
    def test_direct_post_create_mac(self):
        self.assertEqual("163DBAB194D743866A9BCC7FC9C8A88FCD99C6BBBF08D619291212D1B91EE12E", direct_post_create_mac("LK123456789", bytearray.fromhex("0123456789ABCDEF"), 27595, "OD-12345678"))

    def test_verify(self):
        self.assertTrue(verify("LK123456789", bytearray.fromhex("0123456789ABCDEF"), 27595, "OD-12345678", "163DBAB194D743866A9BCC7FC9C8A88FCD99C6BBBF08D619291212D1B91EE12E"))


if __name__ == '__main__':
    unittest.main()
