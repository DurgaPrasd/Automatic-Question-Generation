import unittest 
import os
import sys
sys.path.append('..')
from aqg.utils.file_reader import File_Reader
from aqg.utils.file_writer import File_Writer

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class TestOS(unittest.TestCase):
    def test_reader(self):
        test_path = os.path.dirname(os.path.realpath(__file__))
        fr = File_Reader()
        self.assertIsInstance(fr.read_file(test_path+'/obama.txt'), str)

    def test_writer(self):
    	candidate_path = os.environ.get('CANDIDATE_PATH')
    	fw = File_Writer()
    	fw.write_candidate_questions("test", 'test.txt')
    	with open(candidate_path+'test.txt', 'r') as f:
    		self.assertEqual(f.readline().replace('"',''), "test")



if __name__ == '__main__':
	unittest.main()
        
        
