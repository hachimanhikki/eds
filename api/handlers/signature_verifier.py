from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import base64


class SignatureVerifier:
    @staticmethod
    def verify_signature(hash, encoded_signature, public_key):
        signature = base64.b64decode(encoded_signature)
        try:
            pkcs1_15.new(RSA.import_key(public_key)).verify(hash, signature)
            return True
        except (ValueError, TypeError):
            return False
