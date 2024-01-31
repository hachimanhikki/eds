import base64
from .kalkan_com_test import kalkan_com_test


class DocumentSigner:
    @staticmethod
    def sign_document(hash, private_key):
        return base64.b64encode(b"PLUM PLUM PLUM")