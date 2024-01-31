#from Crypto.PublicKey import RSA
#from Crypto.Signature import pkcs1_15
import base64

class DocumentSigner:
    @staticmethod
    def sign_document(hash, private_key):
        #signer = pkcs1_15.new(RSA.import_key(private_key))
        #signature = signer.sign(hash)
        return base64.b64encode(b"PLUM PLUM PLUM")