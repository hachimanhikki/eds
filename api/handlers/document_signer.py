import base64
from .NCANodeClient import nca_node_client

class DocumentSigner:
    @staticmethod
    def sign_document(document, key, password):
        request = nca_node_client.sign_document(document, key, password)
        return request