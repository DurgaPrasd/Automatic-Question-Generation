# Automatic Gap-Filling Question Generator

[![Requirements Status](https://requires.io/github/bwanglzu/QA-Crawler/requirements.svg?branch=master)](https://requires.io/github/bwanglzu/QA-Crawler/requirements/?branch=master)

Learning to generate Gap-Filling questions from teaching material.

## Build

### Build Project

- `git clone https://github.com/bwanglzu/Automatic_Question_Generation.git`
- `cd Automatic_Question_Generation`
- `pip install -r requirements.txt`

### Build Stanford Parser & NER

- Create a folder to host all the stanford models, e.g. `mkdir /your-path-to-stanford-models/stanford-models`.
+ Download Stanford Parser at [here](https://nlp.stanford.edu/software/lex-parser.shtml), unzip, and:
  - Move `stanford-parser.jar` to stanford models folder, e.g. `/your-path-to-stanford-models/stanford-models/stanford-parser.jar`
  - Move `stanford-parser-x-x-x-models.jar` to stanford models folder.
  - Unzip `stanford-parser-x-x-x-models.jar`, move `/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz` to `stanford-models/`
+ Download Stanford NER at [here](https://nlp.stanford.edu/software/CRF-NER.shtml), unzip, and:
  - Move `stanford-ner.jar` to stanford models folder.
  - Move `stanford-ner-x-x-x.jar` to stanford models folder (e.g. 3.7.0).
  - Move `/classifiers/english.all.3class.distsim.crf.ser.gz` to stanford models folder.

The stanford models folder should looks like this:

```
- stanford-models/
    | - stanford-parser.jar
    | - stanford-parser-x-x-x-models.jar
    | - englishPCFG.ser.gz
    | - stanford-ner.jar
    | - stanford-ner-x-x-x.jar
    | - english.all.3class.distsim.crf.ser.gz
```

### Environment Variables

Create environment variable file with: `touch .env` for configuration (in project root).

```python
SENTENCE_RATIO = 0.05 #The threshold of important sentences

STANFORD_JARS=/path-to-your-stanford-models/stanford-models/
STANFORD_PARSER_CLASSPATH=/path-to-your-stanford-models/stanford-models/stanford-parser-x.x.x-models.jar

STANFORD_NER_CLASSPATH=/path-to-your-stanford-models/stanford-models/stanford-ner.jar
```

## Run

- `cd aqg`
- `python app.py -f name-of-the-document.txt`

## Test

- `nosetests --with-coverage`

## Strategy

- Sentence Selection: select topically important sentences from text document.
- Gap Selection: Exmploy standford parser extract NP (noun phrase) and ADJP from important sentences as candidate gaps
- Question Classification: Classify question quality based on pre-trained SVM classifier

## Performance:

- Achieved 77% accuracy on training set.
- Achieved 66% accuracy on 10-fold CV.

## Classifier Info:

- SVM trained with [Scikit Learn](https://github.com/scikit-learn/scikit-learn), C = 300, gamma = 0.001, rbf kernel.



