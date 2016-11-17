from __init__ import *
from nltk.corpus import stopwords

class FeatureConstruction:
	def __init__(self):
		self.classifier = os.environ.get('CLASSIFIER_PATH')

	def _num_token_in_answer(self, row):
		"""Get number of tokens in answer 
		Args:
		    row(pandas.datafrane): current row vector
		Return:
		    row(pandas.datafrane): row vector with new feature 
		"""
		answer = row.Answer
		try:
			row['Num_Tokens_In_Answer'] = len(answer.split())
			return row
		except:
			row['Num_Tokens_In_Answer'] = 0
			return row

	def _num_token_in_sentence(self, row):
		"""Get number of tokens in question
		Args:
		    row(pandas.dataframe): current row vector
		Return:
		    row(pandas.dataframe): row vector with new feature 
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
		    row(pandas.dataframe): input pandas dataframe
		Return:
		    row(pandas.dataframe): result a pandas dataframe with new feature
		"""
		answer = row.Answer 
		question = row.Question 
		try:
			interaction = [i for i in answer_tokens if i in question]
			row['Num_Token_Match_Question'] = len(interaction)
			return row
		except:
			row['Num_Token_Match_Question'] = 0
			return row

	def _percentage_token_in_answer(self, row):
		"""Percent of the sentence tokens that are in the answer
		Args:
		    row(pandas.dataframe): input pandas dataframe
		Return:
		    row(pandas.dataframe): result a pandas dataframe with new feature
		"""
		answer_len = row.Num_Tokens_In_Answer
		sentence_len = row.Num_Tokens_In_Sentence + answer_len
		try:
			row['Percentage_Token_In_Answer'] = float(answer_len)/sentence_len
			return row
		except:
			row['float(answer_len)/sentence_len'] = 0
			return row

	def _percentage_token_in_out_answer(self, row):
		"""Percent of the sentence tokens that are in the answer (exclude answer length)
		Args:
		    row(pandas.datafrane): input row vector 
		Return:
		    row(pandas.dataframe): output row vector with new feature 
		"""
		answer_len = row.Num_Tokens_In_Answer
		sentence_len = row.Num_Tokens_In_Sentence
		try:
			row['Percentage_Token_In_Out_Answer'] = float(answer_len)/sentence_len
			return row 
		except:
			row['float(answer_len)/sentence_len'] = 0
			return row 

	def _answer_capitalized_word_density(self, row):
		"""Percentage of tokens in the answer that are all caps
		Args:
		    row(pandas.dataframe): input row vector
		Return:
		    row(pandas.dataframe): ouput row vector with new features
		"""
		answer = row.Answer
		try:
			tokens = answer.split()
			num_tokens = len(tokens)
			cap_tokens = [i for i in tokens if i.isupper()==True]
			num_cap_tokens = len(cap_tokens)
			row['Answer_Capitalized_Word_Density'] = float(num_cap_tokens)/num_tokens
			return row 
		except:
			row['float(num_cap_tokens)/num_tokens'] = 0
			return row

	def _answer_pronun_density(self, row):
		"""Percentage of tokens in the answer that are pronouns
		Args:
		    row(pandas.dataframe): input row vector
		Return:
		    row(pandas.dataframe): result a row dataframe with new feature
		"""
		answer = row.Answer
		try:
			row['ANSWER_PRONOMINAL_DENSITY'] = self._identify_pronoun(answer)
			return row
		except:
			row['ANSWER_PRONOMINAL_DENSITY'] = 0
			return row

	def _identify_pronoun(self, answer):
		"""Calculate percentage of pronouns within answer
		Args:
		    answer(str): answer text
		Return:
		    percentage(float): ratio of pronouns in answer
		"""
		text = nltk.word_tokenize(answer)
		post = nltk.pos_tag(text)
		pronoun_list = ['PRP', 'PRP$', 'WP', 'WP$']
		#init variables
		num_pronouns = 0
		num_terms = len(post)
		percentage = 0
		for k, v in post:
			if v in pronoun_list:
				num_pronouns += 1
		try:
			percentage = float(num_pronouns)/num_terms
		except:
			percentage = 0
		return percentage

	def _answer_stop_word_density(self, row):
		"""Percentage of tokens in the answer are stopwords
		Args:
		    row(pandas.dataframe): input row vector
		Return:
		    row(pandas.dataframe): ouput vector with new feature 
		"""
		stop = stopwords.words('english')
		answer = row.Answer 
		try:
			tokens = answer.split()
			num_tokens = len(tokens)
			stop_word_in_answer = [i for i in tokens if i in stop]
			num_stop_word_in_answer = len(stop_word_in_answer)
			row['ANSWER_STOPWORD_DENSITY'] = float(num_stop_in_answer)/num_tokens
			return row 
		except:
			row['ANSWER_STOPWORD_DENSITY'] = 0
			return row

	def _answer_end_with_quantifier(self, row):
		"""Answer ends with a quantifier word (many, few, etc, 1 true, 0 false
		Args:
		    row(pandas.dataframe): input row vector 
		Return:
		    row(pandas.dataframe): output vector with new feature
		"""
		answer = row.Answer
		try:
			tokens = answer.split()
			answer_end_token = tokens[-1]
			if answer_end_token in ling.QUANTIFIER_WORDS:
				row['ANSWER_ENDS_WITH_QUANTIFIER'] = 1
				return row
			else:
				row['ANSWER_ENDS_WITH_QUANTIFIER'] = 0
				return row
		except:
			row['ANSWER_ENDS_WITH_QUANTIFIER'] = 0
			return row

	def _answer_start_with_quantifier(self, row):
		"""Answer start with a quantifier word (many, few etc) 1 true, 0 false
		Args:
		    row(pandas.dataframe): input row vector 
		Return:
		    row(pandas.dataframe): output vector with new feature
		"""
		answer = row.Answer
		try:
			tokens = answer.split()
			answer_start_token = tokens[0]
			if answer_start_token in ling.QUANTIFIER_WORDS:
				row['ANSWER_STARTS_WITH_QUANTIFIER'] = 1
				return row 
			else:
				row['ANSWER_STARTS_WITH_QUANTIFIER'] = 0
				return row
		except:
			row['ANSWER_STARTS_WITH_QUANTIFIER'] = 0
			return row

	def _answer_quantifier_density(self, row):
		"""Percentage of tokens in the answer that are quantifier words
		Args:
		    row(pandas.dataframe): input pandas dataframe
		Return:
		    row(pandas.dataframe): result a pandas dataframe with new feature
		"""
		answer = row.Answer 
		try:
			tokens = answer.split()
			answer_len = len(tokens)
			quantifier_tokens = [i for i in tokens if i in ling.QUANTIFIER_WORDS]
			quantifier_tokens_len = len(quantifier_tokens)
			row['ANSWER_QUANTIFIER_DENSITY'] = float(quantifier_tokens_len)/answer_len
			return row 
		except:
			row['ANSWER_QUANTIFIER_DENSITY'] = 0
			return row

	def _percentage_capitalized_word_in_answer(self, row):
		"""Percentage of capitalized words in the sentence that are in the answer
		Args:
		    row(pandas.dataframe): input pandas dataframe
		Return:
		    row(pandas.dataframe): result a pandas dataframe with new feature
		"""
		answer = row.Answer
		sentence = row.Sentence 
		try:
			tokens = sentence.split()
			num_tokens = len(tokens)
			cap_tokens = [i for i in tokens if i.isupper()==True]
			cap_tokens_in_answer = [i for i in cap_tokens if i in answer]
			row['PERCENT_CAPITALIZED_WORDS_IN_ANSWER'] = float(len(cap_tokens_in_answer))/num_tokens
			return row 
		except:
			row['PERCENT_CAPITALIZED_WORDS_IN_ANSWER'] = 0
			return row

	def _percentage_pronoun_in_answer(self, row):
		"""Percentage of pronouns in the sentence that are in the answer
		Args:
		    row(pandas.dataframe): input pandas dataframe
		Return:
		    row(pandas.dataframe): result a pandas dataframe with new feature
		"""
		answer = row.Answer
		sentence = row.Sentence
		try:
			pronoun_in_sentence, sentence_len = self._identify_pronoun2(sentence)
			pronoun_in_sentence_in_answer = [i for i in pronoun_in_sentence if i in answer]
			num_pronoun_in_sentence_in_answer = len(pronoun_in_sentence_in_answer)
			row['PERCENT_PRONOMINALS_IN_ANSWER'] = float(num_pronoun_in_sentence_in_answer)/sentence_len
			return row 
		except:
			row['PERCENT_PRONOMINALS_IN_ANSWER'] = 0
			return row

	def _identify_pronoun2(self, sentence):
		"""Calculate percentage of pronouns in the sentence that are in the answer
		Args:
		    sentence(str): question sentence 
		Return:
		    pronoun_in_sentence(list): pronouns in sentence 
		    sentence_len(int): length of current sentence 
		"""
		text = nltk.word_tokenize(sentence)
		post = nltk.pos_tag(text)
		pronoun_list = ['PRP', 'PRP$', 'WP', 'WP$']
		pronoun_in_sentence = []
		sentence_len = len(post)
		for k, v in post:
			if v in pronoun_list:
				pronoun_in_sentence.append(k)
		return pronoun_in_sentence, sentence_len

	def _sentence_start_with_discourse(self, row):
		"""Sentence starts with a discourse connective word, 1 true 0 false
		Args:
		    row(pandas.dataframe): input pandas dataframe
		Return:
		    row(pandas.dataframe): result a pandas dataframe with new feature
		"""
		sentence = row.Sentence 
		try:
			tokens = sentence.split()
			start_tokens = ' '.join(tokens[:3]) # first three terms
			#check discourse marker is in first three tokens
			is_discourse = [i for i in ling.DISCOURSE_MARKERS if i in start_tokens]
			if is_discourse:
				row['SENTENCE_STARTS_WITH_DISCOURSE_CONNECTIVE'] = 1
				return row
			else:
				row['SENTENCE_STARTS_WITH_DISCOURSE_CONNECTIVE'] = 0
				return row
		except:
			row['SENTENCE_STARTS_WITH_DISCOURSE_CONNECTIVE'] = 0
			return row

	def _pos1_gram_after_answer(self, row, flag):
		"""The first POS tag following the answer span is [FLAG]
		Args:
		    row(pandas.dataframe): input pandas dataframe
		    flag(string): symbol to match first tagger
		Return:
		    binary(int): 1 match, 0 not match
		"""
		question = row.Question 
		try:
			first_tagger = self._first_tagger_after_answer_span(question)
			if first_tagger == flag:
				return 1
			else:
				return 0
		except:
			return 0

	def _first_tagger_after_answer_span(self, question):
		"""Get the first tagger after answer span
		Args:
		    question(string): string of current question 
		Return:
		    tagger(string): tagger of first term after span
		"""
		text = nltk.word_tokenize(question)
		post = nltk.pos_tag(text)
		index = next(idx for (idx, t) in enumerate(post) if t[0]=='_____') + 1
		return post[index][1]

	def _pos1_gram_before_answer(self, row, flag):
		"""The first POS tag before the answer span is [FLAG]
		Args:
		    row(pandas.dataframe): input pandas dataframe
		    flag(string): symbol to match first tagger
		Return:
		    binary(int): 1 match, 0 not match
		"""
		question = row.Question
		try:
			first_tagger = self._first_tagger_before_answer_span(question)
			if first_tagger == flag:
				return 1
			else:
				return 0
		except:
			return 0

	def _first_tagger_before_answer_span(self, question):
		"""Get the first tagger before answer span
		Args:
		    question(string): string of current question 
		Return:
		    tagger(string): tagger of first term before span
		"""
		text = nltk.word_tokenize(question)
		post = nltk.pos_tag(text)
		index = next(idx for (idx, t) in enumerate(post) if t[0]=='_____') - 1
		return post[index][1]


	def _pos_gram_count_answer(self, row, flag):
		"""Count pos tagger within answer that match [FLAG]
		Args:
		    row(pandas.dataframe): dataframe of current row
		    flag(string): [FLAG] to match answer
		Return:
		    count(int): number of match
		"""
		answer = row.Answer 
		try:
			tag_count = self._count_token_with_match(answer, flag)
			return tag_count
		except:
			return 0

	def _count_token_with_match(self, answer, match):
		"""Count answer match FLAG 
		"""
		text = nltk.word_tokenize(answer)
		post = nltk.pos_tag(text)
		count = 0
		for k, v in post:
			if v == match:
				count +=1
		return count 









	def extract_feature(self, candidates):
		"""Build feature dataframe
		Args:
		    candidates(list): candidate question answer pairs
		Return:
		    df(pandas.dataframe): dataframe of question, answer, sentence and features
		"""
		df = pd.DataFrame(candidates)
		for idx, row in df.iterrows():
			row = self._num_token_in_answer(row)
			row = self._num_token_in_sentence(row)
			row = self._num_row_tokens_matching_in_out(row)
			row = self._percentage_token_in_answer(row)
			row = self._percentage_token_in_out_answer(row)
			row = self._answer_capitalized_word_density(row)
			row = self._answer_stop_word_density(row)
			row = self._answer_end_with_quantifier(row)
			row = self._answer_start_with_quantifier(row)
			row = self._answer_quantifier_density(row)
			row = self._percentage_capitalized_word_in_answer(row)
			row = self._percentage_pronoun_in_answer(row)
			row = self._sentence_start_with_discourse(row)
			row['GRAM_AFTER_ANSWER_quoation'] = self._pos1_gram_after_answer(row, "'")
			row['GRAM_AFTER_ANSWER_comma'] = self._pos1_gram_after_answer(row, ",")
			row['GRAM_AFTER_ANSWER_LRB'] = self._pos1_gram_after_answer(row, "LRB")
			row['GRAM_AFTER_ANSWER_RRB'] = self._pos1_gram_after_answer(row, "RRB")
			row['GRAM_AFTER_ANSWER_Stop'] = self._pos1_gram_after_answer(row, ".")
			row['GRAM_AFTER_ANSWER_Colon'] = self._pos1_gram_after_answer(row, ":")
			row['GRAM_AFTER_ANSWER_CC'] = self._pos1_gram_after_answer(row, "CC")
			row['GRAM_AFTER_ANSWER_CD'] = self._pos1_gram_after_answer(row, "CD")
			row['GRAM_AFTER_ANSWER_DT'] = self._pos1_gram_after_answer(row, "DT")
			row['GRAM_AFTER_ANSWER_EX'] = self._pos1_gram_after_answer(row, "EX")
			row['GRAM_AFTER_ANSWER_IN'] = self._pos1_gram_after_answer(row, "IN")
			row['GRAM_AFTER_ANSWER_JJ'] = self._pos1_gram_after_answer(row, "JJ")
			row['GRAM_AFTER_ANSWER_JJR'] = self._pos1_gram_after_answer(row, "JJR")
			row['GRAM_AFTER_ANSWER_JJS'] = self._pos1_gram_after_answer(row, "JJS")
			row['GRAM_AFTER_ANSWER_MD'] = self._pos1_gram_after_answer(row, "MD")
			row['GRAM_AFTER_ANSWER_NN'] = self._pos1_gram_after_answer(row, "NN")
			row['GRAM_AFTER_ANSWER_NNP'] = self._pos1_gram_after_answer(row, "NNP")
			row['GRAM_AFTER_ANSWER_NNPS'] = self._pos1_gram_after_answer(row, "NNPS")
			row['GRAM_AFTER_ANSWER_NNS'] = self._pos1_gram_after_answer(row, "NNS")
			row['GRAM_AFTER_ANSWER_POS'] = self._pos1_gram_after_answer(row, "POS")
			row['GRAM_AFTER_ANSWER_PRP'] = self._pos1_gram_after_answer(row, "PRP")
			row['GRAM_AFTER_ANSWER_RB'] = self._pos1_gram_after_answer(row, "RB")
			row['GRAM_AFTER_ANSWER_RBR'] = self._pos1_gram_after_answer(row, "RBR")
			row['GRAM_AFTER_ANSWER_RBS'] = self._pos1_gram_after_answer(row, "RBS")
			row['GRAM_AFTER_ANSWER_RP'] = self._pos1_gram_after_answer(row, "RP")
			row['GRAM_AFTER_ANSWER_TO'] = self._pos1_gram_after_answer(row, "TO")
			row['GRAM_AFTER_ANSWER_VB'] = self._pos1_gram_after_answer(row, "VB")
			row['GRAM_AFTER_ANSWER_VBD'] = self._pos1_gram_after_answer(row, "VBD")
			row['GRAM_AFTER_ANSWER_VBG'] = self._pos1_gram_after_answer(row, "VBG")
			row['GRAM_AFTER_ANSWER_VBN'] = self._pos1_gram_after_answer(row, "VBN")
			row['GRAM_AFTER_ANSWER_VBP'] = self._pos1_gram_after_answer(row, "VBP")
			row['GRAM_AFTER_ANSWER_VBZ'] = self._pos1_gram_after_answer(row, "VBZ")
			row['GRAM_AFTER_ANSWER_WDT'] = self._pos1_gram_after_answer(row, "WDT")
			row['GRAM_AFTER_ANSWER_WP'] = self._pos1_gram_after_answer(row, "WP")
			row['GRAM_AFTER_ANSWER_WRB'] = self._pos1_gram_after_answer(row, "WRB")
			row['GRAM_BEFORE_ANSWER_Comma'] = self._pos1_gram_before_answer(row, ",")
			row['GRAM_BEFORE_ANSWER_LRB'] = self._pos1_gram_before_answer(row, "LRB")
			row['GRAM_BEFORE_ANSWER_RRB'] = self._pos1_gram_before_answer(row, "RRB")
			row['GRAM_BEFORE_ANSWER_Colon'] = self._pos1_gram_before_answer(row, ":")
			row['GRAM_BEFORE_ANSWER_CC'] = self._pos1_gram_after_answer(row, "CC")
			row['GRAM_BEFORE_ANSWER_CD'] = self._pos1_gram_before_answer(row, "CD")
			row['GRAM_BEFORE_ANSWER_DT'] = self._pos1_gram_before_answer(row, "DT")
			row['GRAM_BEFORE_ANSWER_EX'] = self._pos1_gram_before_answer(row, "EX")
			row['GRAM_BEFORE_ANSWER_IN'] = self._pos1_gram_before_answer(row, "IN")
			row['GRAM_BEFORE_ANSWER_JJ'] = self._pos1_gram_before_answer(row, "JJ")
			row['GRAM_BEFORE_ANSWER_MD'] = self._pos1_gram_before_answer(row, "MD")
			row['GRAM_BEFORE_ANSWER_NN'] = self._pos1_gram_before_answer(row, "NN")
			row['GRAM_BEFORE_ANSWER_NNP'] = self._pos1_gram_before_answer(row, "NNP")
			row['GRAM_BEFORE_ANSWER_NNPS'] = self._pos1_gram_before_answer(row, "NNPS")
			row['GRAM_BEFORE_ANSWER_NNS'] = self._pos1_gram_before_answer(row, "NNS")
			row['GRAM_BEFORE_ANSWER_POS'] = self._pos1_gram_before_answer(row, "POS")
			row['GRAM_BEFORE_ANSWER_PRP$'] = self._pos1_gram_before_answer(row, "PRP$")
			row['GRAM_BEFORE_ANSWER_RB'] = self._pos1_gram_before_answer(row, "RB")
			row['GRAM_BEFORE_ANSWER_RBS'] = self._pos1_gram_before_answer(row, "RBS")
			row['GRAM_BEFORE_ANSWER_RP'] = self._pos1_gram_before_answer(row, "RP")
			row['GRAM_BEFORE_ANSWER_TO'] = self._pos1_gram_before_answer(row, "TO")
			row['GRAM_BEFORE_ANSWER_VB'] = self._pos1_gram_before_answer(row, "VB")
			row['GRAM_BEFORE_ANSWER_VBD'] = self._pos1_gram_before_answer(row, "VBD")
			row['GRAM_BEFORE_ANSWER_VBG'] = self._pos1_gram_before_answer(row, "VBG")
			row['GRAM_BEFORE_ANSWER_VBN'] = self._pos1_gram_before_answer(row, "VBN")
			row['GRAM_BEFORE_ANSWER_VBP'] = self._pos1_gram_before_answer(row, "VBP")
			row['GRAM_BEFORE_ANSWER_VBZ'] = self._pos1_gram_before_answer(row, "VBZ")
			row['GRAM_BEFORE_ANSWER_WDT'] = self._pos1_gram_before_answer(row, "WDT")
			row['GRAM_BEFORE_ANSWER_WP'] = self._pos1_gram_before_answer(row, "WP")
			row['GRAM_BEFORE_ANSWER_WRB'] = self._pos1_gram_before_answer(row, "WRB")
			row['GRAM_IN_ANSWER_COUNT_Quotation'] = self._pos_gram_count_answer(row, "'")
			row['GRAM_IN_ANSWER_COUNT_Comma'] = self._pos_gram_count_answer(row, ",")
			row['GRAM_IN_ANSWER_COUNT_LRB'] = self._pos_gram_count_answer(row, "LRB")
			row['GRAM_IN_ANSWER_COUNT_RRB'] = self._pos_gram_count_answer(row, "RRB")
			row['GRAM_IN_ANSWER_COUNT_Colon'] = self._pos_gram_count_answer(row, ":")
			row['GRAM_IN_ANSWER_COUNT_CC'] = self._pos_gram_count_answer(row, "CC")
			row['GRAM_IN_ANSWER_COUNT_CD'] = self._pos_gram_count_answer(row, "CD")
			row['GRAM_IN_ANSWER_COUNT_DT'] = self._pos_gram_count_answer(row, "DT")
			row['GRAM_IN_ANSWER_COUNT_EX'] = self._pos_gram_count_answer(row, "EX")
			row['GRAM_IN_ANSWER_COUNT_IN'] = self._pos_gram_count_answer(row, "IN")
			row['GRAM_IN_ANSWER_COUNT_JJ'] = self._pos_gram_count_answer(row, "JJ")
			row['GRAM_IN_ANSWER_COUNT_JJR'] = self._pos_gram_count_answer(row, "JJR")
			row['GRAM_IN_ANSWER_COUNT_JJS'] = self._pos_gram_count_answer(row, "JJS")
			row['GRAM_IN_ANSWER_COUNT_MD'] = self._pos_gram_count_answer(row, "MD")
			row['GRAM_IN_ANSWER_COUNT_NN'] = self._pos_gram_count_answer(row, "NN")
			row['GRAM_IN_ANSWER_COUNT_NNP'] = self._pos_gram_count_answer(row, "NNP")
			row['GRAM_IN_ANSWER_COUNT_NNPS'] = self._pos_gram_count_answer(row, "NNPS")
			row['GRAM_IN_ANSWER_COUNT_NNS'] = self._pos_gram_count_answer(row, "NNS")
			row['GRAM_IN_ANSWER_COUNT_POS'] = self._pos_gram_count_answer(row, "POS")
			row['GRAM_IN_ANSWER_COUNT_PRP'] = self._pos_gram_count_answer(row, "PRP")
			row['GRAM_IN_ANSWER_COUNT_PRP$'] = self._pos_gram_count_answer(row, "PRP$")
			row['GRAM_IN_ANSWER_COUNT_RB'] = self._pos_gram_count_answer(row, "RB")
			row['GRAM_IN_ANSWER_COUNT_RBR'] = self._pos_gram_count_answer(row, "RBR")
			row['GRAM_IN_ANSWER_COUNT_RBS'] = self._pos_gram_count_answer(row, "RBS")
			row['GRAM_IN_ANSWER_COUNT_RP'] = self._pos_gram_count_answer(row, "RP")
			row['GRAM_IN_ANSWER_COUNT_TO'] = self._pos_gram_count_answer(row, "TO")
			row['GRAM_IN_ANSWER_COUNT_VB'] = self._pos_gram_count_answer(row, "VB")
			row['GRAM_IN_ANSWER_COUNT_VBD'] = self._pos_gram_count_answer(row, "VBD")
			row['GRAM_IN_ANSWER_COUNT_VBG'] = self._pos_gram_count_answer(row, "VBG")
			row['GRAM_IN_ANSWER_COUNT_VBN'] = self._pos_gram_count_answer(row, "VBN")
			row['GRAM_IN_ANSWER_COUNT_VBP'] = self._pos_gram_count_answer(row, "VBP")
			row['GRAM_IN_ANSWER_COUNT_VBZ'] = self._pos_gram_count_answer(row, "VBZ")
			row['GRAM_IN_ANSWER_COUNT_WDT'] = self._pos_gram_count_answer(row, "WDT")
			row['GRAM_IN_ANSWER_COUNT_WP'] = self._pos_gram_count_answer(row, "WP")
			row['GRAM_IN_ANSWER_COUNT_WP$'] = self._pos_gram_count_answer(row, "WP$")
			row['GRAM_IN_ANSWER_COUNT_WRB'] = self._pos_gram_count_answer(row, "WRB")
			print row


















