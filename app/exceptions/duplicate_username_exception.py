class Duplicate_Username_Exception(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)