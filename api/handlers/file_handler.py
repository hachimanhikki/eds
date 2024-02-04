#from crypto.Hash import SHA256
from django.core.files.uploadedfile import InMemoryUploadedFile
import base64

class FileHandler:
    def __init__(self, file: InMemoryUploadedFile):
        self.file = file
    
    def get_data(self):
        data = self.file.read()
        return data.decode('utf-8')

    def base64_encode(self):
        b64_encoded = base64.b64encode(self.file.read())
        return b64_encoded.decode('utf-8')
        
    def get_hash(self):
        file_data = self.get_data()
        #hash_obj = SHA256.new(data=file_data)
        return "PLUM PLUM PLUM"