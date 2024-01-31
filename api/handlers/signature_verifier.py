#from Crypto.PublicKey import RSA
#from Crypto.Signature import pkcs1_15
import base64
from .kalkan_com_test import kalkan_com_test


class SignatureVerifier:
    @staticmethod
    def verify_signature(data, encoded_signature):
        in_data = base64.decodebytes(data)
        in_sign = base64.decodebytes(encoded_signature)
        kalkan_com_test.verify_data(in_data, in_sign)
        return True
