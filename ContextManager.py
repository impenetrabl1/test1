class FileOpen:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.opened_file = open(self.file_name, self.mode)
        return self.opened_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.opened_file.close()




