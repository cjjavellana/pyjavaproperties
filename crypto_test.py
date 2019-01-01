#! /usr/bin/env python

import unittest
import crypto
import logging


class CryptoTest(unittest.TestCase):

    def setUp(self):
        self.aes = crypto.AESCipher('aabbccddeeffgghh')

    def testEncryptPlainText(self):
        encrypted = self.aes.encrypt("aaabbbccc111222333")
        logging.info("Encrypted value => [enc]{}".format(encrypted))
        self.assertNotEqual("aaabbbccc111222333", encrypted)

    def testDecryptPlainText(self):
        decrypted = self.aes.decrypt("vY80nfAwBX4BtLYrpsIFLZkjq8Z+bcE604tWRe6sHOAHpB5qTNg/VtCT2yzY2/6k")
        self.assertEqual("aaabbbccc111222333", decrypted)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')
    unittest.main()
