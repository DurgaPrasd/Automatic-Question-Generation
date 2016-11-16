from sentence_selection import SentenceSelection
from gap_selection import GapSelection
from feature_construction import FeatureConstruction

ss = SentenceSelection()
sentences = ss.prepare_sentences("/Users/wbcha/Desktop/project/Automatic_Question_Generation/tests/obama.txt")
print sentences
gs = GapSelection()
candidates = gs.get_candidates(sentences)
print candidates
fc = FeatureConstruction()
print fc.extract_feature(candidates)
