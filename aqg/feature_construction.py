from __init__ import *

class Feature_Construction:
	def __init__(self):
		pass

	def _num_tokens_in_answer(self, row):
	    """Count number of tokens in answer
	    Args:
	        row(pandas.dataframe): input pandas dataframe
	    Return:
	        row(int): return number of tokens in answer(gap)
	    """
	    answer = row.Answer
	    try:
	        return len(answer.split())
	    except:
	        return 0

	def _num_token_in_sentence(self, row):
		"""Count number of features in sentence
		Args:
		    row(pandas.dataframe): input pandas dataframe
		Returns:
		    row(int): number of tokens in sentence (question)
		"""
		question = row.Question
	    try:
	        return len(question.split())
	    except:
	        return 0

	def _percentage_token_in_answer(self, df):
		"""Percent of the sentence tokens that are in the answer (exclude answer length)
		Args:
		    df(pandas.dataframe): input pandas dataframe
		Returns:
		    df(pandas.dataframe): result a pandas dataframe with new feature
		"""
	    answer_len = row.Num_Tokens_In_Answer
	    sentence_len = row.Num_Tokens_In_Sentence - answer_len
	    try:
	        return float(answer_len)/sentence_len
	    except:
	        return 0

