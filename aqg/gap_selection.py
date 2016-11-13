"""Question Generation, use pre-trained support vector machine identify question quality
Note: SVM Accuracy on Training Set 75%
	  SVM Accuracy on 10-fold CV: 66%
	  Parameter: rbf kernel, c=300, gamma=0.001
Code:
"""
from __init__ import *

from sum_basic import SumBasic

class Gap_Selection:
	def __init__(self):
		self.classifier = config.CLASSIFIER_PATH
		self.sb = SumBasic()
		self.fw = File_Writer()