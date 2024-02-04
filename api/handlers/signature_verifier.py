from .NCANodeClient import nca_node_client
import base64


class SignatureVerifier:
    @staticmethod
    def verify_signature(cms):
        data = nca_node_client.verify_document(cms)
        return data
