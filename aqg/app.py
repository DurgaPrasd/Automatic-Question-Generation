import re
import os
import sys
import json
import math
import string
import operator
from collections import defaultdict
from collections import OrderedDict

import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")

import argparse
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.externals import joblib

import utils.linguistic as ling
from utils.file_reader import File_Reader
from utils.file_writer import File_Writer
from utils.gap_selection import GapSelection
from utils.sentence_selection import SentenceSelection
from utils.feature_construction import FeatureConstruction

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def pipeline(document):
    """Pipeline of Automatic Question Generation 
    - Args:
        document(str): path of input document
    - Returns:
        question_answers(pandas.dataframe): Q/A/Prediction
    """
    # init classes
    ss = SentenceSelection()
    gs = GapSelection()
    # build candidate questions, extract features
    sentences = ss.prepare_sentences(document)
    candidates = gs.get_candidates(sentences)
    fc = FeatureConstruction()
    candidates_with_features = fc.extract_feature(candidates)
    question_answers = _classify(candidates_with_features)
    return question_answers


def _classify(df):
    """Classification
    - Args:
        df(pandas.dataframe): candidate qa pairs with extracted features 
    - Returns:
        question_answers(pandas.dataframe): Question, Answer, Prediction (label)
    """
    clf = joblib.load(os.path.dirname(__file__) + "/models/clf.pkl")
    question_answers = df[['Question', 'Answer']]
    X = df.drop(['Answer', 'Question', 'Sentence'], axis=1).as_matrix()
    y = clf.predict(X)
    question_answers['Prediction'] = y
    return question_answers


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--input", help="input document")
    args = parser.parse_args()
    print pipeline(args.input)
