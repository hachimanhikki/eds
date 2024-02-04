import requests


class NCANodeClient:
    def __init__(self):
        self.url = 'http://localhost:14579'
    
    def test_connection(self):
        request = requests.get(f'{self.url}/actuator/health')
        print(request.content)
    
    def get_key_info(self, key, password):
        body = {
          "revocationCheck": [
            "OCSP"
          ],
          "keys": [
            {
              "key": key,
              "password": password,
              "keyAlias": None
            }
          ]
        }
        request = requests.post(f'{self.url}/pkcs12/info', json=body)
        print(request.json())
        return request.json()
    
    def sign_document(self, document, key, password):
        body = {
          "data": document,
          "signers": [
            {
              "key": key,
              "password": password,
              "keyAlias": None
            }
          ],
          "withTsp": True,
          "tsaPolicy": "TSA_GOST_POLICY",
          "detached": False
        }
        request = requests.post(f'{self.url}/cms/sign', json=body)
        print(request.json())
        return request.json()

    def verify_document(self, cms):
        body = {
          "revocationCheck": [
            "OCSP"
          ],
          "cms": cms
        }
        request = requests.post(f'{self.url}/cms/verify', json=body)
        return request.json()

    def extract_from_cms(self, cms):
        body = {
            "cms": cms
        }
        request = requests.post(f'{self.url}/cms/extract', json=body)
        print(request.json())
        return request.json()

nca_node_client = NCANodeClient()