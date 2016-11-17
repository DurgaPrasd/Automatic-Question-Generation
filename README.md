# Automatic Gap-Filling Question Generator

[![CircleCI](https://circleci.com/gh/bwanglzu/Automatic_Question_Generation/tree/master.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/bwanglzu/QA-Crawler/tree/master)
[![Requirements Status](https://requires.io/github/bwanglzu/QA-Crawler/requirements.svg?branch=master)](https://requires.io/github/bwanglzu/QA-Crawler/requirements/?branch=master)

Learning to generate Gap-Filling questions from teaching material.

## Unfinished Yet

- SOLVE BUG MAX() FUNCTION EMPTY SEQUENCE **SLOVED**
- PRINT ALL EXCEPTIONS **SOLVED**
- RE-TRAIN SVM AFTER SOLVE BUG. **WORKING**
- CIRCLECI PROBLEM, NEED TO DOWNLOAD NLTK DATA OTHERWISE WILL ALWAYS FAIL TO DEPLOY
- ADD STANFORD PARSER + NLTK INSTALL PROCESS IN README

## Build

### Build Project

- `git clone https://github.com/bwanglzu/Automatic_Question_Generation.git`
- `cd Automatic_Question_Generation`
- `pip install -r requirements.txt`
- `touch .env` for configuration (in project root)

### .env

```python
SENTENCE_RATIO = 0.05 #The threshold of important sentences

#Stanford Jars, your folder of STANFORD PARSER
STANFORD_JARS="/Users/path-to-stanford-parser/stanford_parser-yyyy-mm-dd/"
#Stanford Name Entity Recognition folder, 
STANFORD_NERS = "/Users/path-to-stanford-ner/stanford-ner-yyyy-mm-dd/"
#TEMP PATH FOR STORE QUESTION/ANSWER CANDIDATES
CANDIDATE_PATH = "/Users/wbcha/Desktop/project/Mind_The_Gap/candidates/"
#Support Vector Machine Path (in project folder/model, clf.pkl)
CLASSIFIER_PATH = "/Users/path-to-project/model/clf.pkl"
```

### Build Stanford Parser & NER

- Check this page `https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software`
- Folder structure of Stanford Parser should looks like:

```python
- stanford-parser-yyyy-mm-dd
    | - stanford-parser-3.5.2-models.jar
    | - stanford-parser.jar
    | - englishPCFG.ser.gz
    | - ..... (rest stuff)
```

- Folder structure of Stanford NER:

```python
- stanford-ner-yyyy-mm-dd
    | - stanford-ner-3.6.0.jar
    | - stanford-ner.jar
    | - english.all.3class.distsim.crf.ser.gz
    | - ..... (rest stuff)
```

- It shuold be noted that `englishPCFG.ser.gz` and `english.all.3class.distsim.crf.ser.gz` originally in a subfolder named `classifiers`

## Run

- `cd aqg`
- `python app.py document.txt`

## Test

- `nosetests`

## Strategy

- Sentence Selection: select topically important sentences from text document.
- Gap Selection: Exmploy standford parser extract NP (noun phrase) and ADJP from important sentences as candidate gaps
- Question Classification: Classify question quality based on SVM classifier

## Performance:

- Achieved 77% accuracy on training set.
- Achieved 66% accuracy on 10-fold CV.

## Classifier Info:

- SVM trained with [Scikit Learn](https://github.com/scikit-learn/scikit-learn), C = 300, gamma = 0.001, rbf kernel.



