from sentence_selection import SentenceSelection
from gap_selection import GapSelection
from feature_construction import FeatureConstruction

ss = SentenceSelection()
sentences = ss.prepare_sentences("/Users/wbcha/Desktop/project/Automatic_Question_Generation/tests/obama.txt")
gs = GapSelection()
candidates = gs.get_candidates(sentences)
# fc = FeatureConstruction()
# fc.built_features(candidates)
