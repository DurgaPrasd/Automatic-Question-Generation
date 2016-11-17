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
- `pip install -r requirements.txt`
- Modify configuration files in `.env`

### Build Stanford Parser & NER

- Java 1.8 required

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



