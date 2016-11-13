import config
from os import listdir
from os.path import isfile, join

class File_Reader:
    def __init__(self):
        self.path = config.file_path

    def load_file_names(self):
        '''
        @usage: load all furniture files into list
        @return: list of file names
        '''
        #load all file names from file path
        file_names = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        if '.DS_Store' in file_names:
            file_names.remove('.DS_Store')
        return file_names

    def read_file(self, file_name):
        '''
        @usage: read file content from current file
        @arg file_name: name of current file need to read
        @return content of current file
        '''
        with open(self.path+file_name, 'r') as f:
            return f.read().replace('\n', '')
