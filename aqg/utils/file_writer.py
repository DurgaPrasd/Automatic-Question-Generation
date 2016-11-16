import json
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class File_Writer:
    def __init__(self):
        self.candidate_path = CANDIDATE_PATH 

    def write_candidate_questions(self, content, file_name):
        '''
        @usage: write document length to local storage
        @arg content: content need to write
        '''
        with open(self.candidate_path + file_name, 'w') as c:
            json.dump(content,c)
