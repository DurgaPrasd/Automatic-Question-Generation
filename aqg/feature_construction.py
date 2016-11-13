from __init__ import *

class Feature_Construction:
	def __init__(self):
		pass

	def _num_tokens_in_answer(self, row):
	    """Count number of tokens in answer
	    Args:
	        row(pandas.dataframe): input pandas dataframe
	    Return:
	        row(pandas.dataframe): return number of tokens in answer(gap)
	    """
	    answer = row.Answer
	    try:
	    	row['Num_Tokens_In_Answer'] = len(answer.split())
	    	return row
	    except:
	        row['Num_Tokens_In_Answer'] = 0
	    	return row

	def _num_token_in_sentence(self, row):
		"""Count number of features in sentence
		Args:
		    row(pandas.dataframe): input pandas dataframe
		Returns:
		    row(pandas.dataframe): number of tokens in sentence (question)
		"""
		question = row.Question
	    try:
	        row['Num_Tokens_In_Sentence'] = len(question.split())
	        return row
	    except:
	        row['Num_Tokens_In_Sentence'] = 0
	    	return row

	def _num_row_tokens_matching_in_out(self, row):
		"""Number of tokens in the answer that match tokens outside of the answer
	    Args:
	        df(pandas.dataframe): input pandas dataframe
	    Returns:
	        df(pandas.dataframe): result a pandas dataframe with new feature
	    """
	    try:
		    answer = row.Answer
		    question = row.Question
		    intersection = [i for i in answer_tokens if i in question]
		    row['Num_Token_Match_Question'] = len(intersection)
		    return row
		except:
			row['Num_Token_Match_Question'] = 0
			return row

	def _percentage_token_in_answer(self, row):
		"""Percent of the sentence tokens that are in the answer (exclude answer length)
		Args:
		    row(pandas.dataframe): input pandas dataframe
		Returns:
		    row(pandas.dataframe): result a pandas dataframe with new feature
		"""
	    answer_len = row.Num_Tokens_In_Answer
	    sentence_len = row.Num_Tokens_In_Sentence - answer_len
	    try:
	        row['Percentage_Token_In_Answer'] = float(answer_len)/sentence_len
	        return row
	    except:
	        row['Percentage_Token_In_Answer'] = 0
	    	return row

