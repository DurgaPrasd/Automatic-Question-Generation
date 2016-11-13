# Automatic Gap-Filling Question Generator

[![CircleCI](https://circleci.com/gh/bwanglzu/QA-Crawler/tree/master.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/bwanglzu/QA-Crawler/tree/master)
[![Requirements Status](https://requires.io/github/bwanglzu/QA-Crawler/requirements.svg?branch=master)](https://requires.io/github/bwanglzu/QA-Crawler/requirements/?branch=master)

Learning to generate Gap-Filling questions from teaching material.

## Still Unfinished

## Build

- git clone ``
- Modify configuration files in ``

## Run

- `cd aqg`

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



