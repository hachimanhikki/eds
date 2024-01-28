from Crypto.Hash import SHA256
from django.core.files.uploadedfile import InMemoryUploadedFile

class FileHandler:
    def __init__(self, file: InMemoryUploadedFile):
        self.file = file
    
    def get_data(self):
        return self.file.read()

    def get_hash(self):
        file_data = self.get_data()
        hash_obj = SHA256.new(data=file_data)
        return hash_obj