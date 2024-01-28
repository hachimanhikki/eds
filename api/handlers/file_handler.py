from Crypto.Hash import SHA256


class FileHandler:
    def __init__(self, file):
        self.file = file
        return None
    
    def get_data(self):
        return self.file

    def get_hash(self):
        hash = SHA256.new(self.get_data())
        return hash