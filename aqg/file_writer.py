import config
import json

class File_Writer:
    def __init__(self):
        self.candidate_path = config.CANDIDATES_STORAGE

    def write_candidate_questions(self, content, file_name):
        '''
        @usage: write document length to local storage
        @arg content: content need to write
        '''
        with open(self.candidate_path + file_name, 'w') as c:
            json.dump(content,c)