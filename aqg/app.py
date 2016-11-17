from __init__ import *
from sklearn import svm
from sklearn.externals import joblib

from gap_selection import GapSelection
from sentence_selection import SentenceSelection
from feature_construction import FeatureConstruction

def pipeline(document):
	"""Pipeline of Automatic Question Generation 
	Args:
	    document(str): path of input document
	Return:
	    question_answers(pandas.dataframe): Q/A/Prediction
	"""
	#init classes
	ss = SentenceSelection()
	gs = GapSelection()
	fc = FeatureConstruction()
	#build candidate questions, extract features
	sentences = ss.prepare_sentences(document)
	candidates = gs.get_candidates(sentences)
	candidates_with_features = fc.extract_feature(candidates)
	question_answers = classify(candidates_with_features)
	return question_answers

def classify(df):
	"""Classification
	Args:
	    df(pandas.dataframe): candidate qa pairs with extracted features 
	Return:
	    question_answers(pandas.dataframe): Question, Answer, Prediction (label)
	"""
	clf = joblib.load(os.environ.get('CLASSIFIER_PATH'))
	question_answers = df[['Question','Answer']]
	X = df.drop(['Answer','Question','Sentence'], axis=1).as_matrix()
	y = clf.predict(X)
	question_answers['Prediction'] = y
	return question_answers


if __name__ == '__main__':
	doc = sys.argv[1:]
	print pipeline(doc)
