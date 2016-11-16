from sentence_selection import SentenceSelection
from gap_selection import GapSelection

ss = SentenceSelection()
sentences = ss.prepare_sentences("/Users/wbcha/Desktop/project/Automatic_Question_Generation/tests/obama.txt")
gs = GapSelection()
print gs.get_candidates(sentences)
