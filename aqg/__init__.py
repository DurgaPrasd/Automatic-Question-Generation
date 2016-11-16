import re
import os
import json
import math
import string
import operator

import nltk
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.externals import joblib
from practnlptools.tools import Annotator

import utils.linguistic as ling

from collections import defaultdict
from collections import OrderedDict

from utils.file_reader import File_Reader
from utils.file_writer import File_Writer
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
