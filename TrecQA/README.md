TrecQA
------

The TrecQA dataset is commonly used for evaluating answer selection in question answering. It was first released and then organized by the following papers:

+ Wang et al. [What is the Jeopardy Model? A Quasi-Synchronous Grammar for QA.](http://www.aclweb.org/anthology/D07-1003) *EMNLP-CoNLL 2007*.
+ Heilman and Smith. [Tree Edit Models for Recognizing Textual Entailments, Paraphrases,
and Answers to Questions.](http://www.aclweb.org/anthology/N10-1145) *NAACL 2010*.
+ Yao et al. [Answer Extraction as Sequence Tagging with Tree Edit Distance.](http://www.aclweb.org/anthology/N13-1106) *NAACL-HLT 2013*.

Specifically, we use the data prepared by Yao et al., downloaded from `http://cs.jhu.edu/~xuchen/packages/jacana-qa-naacl2013-data-results.tar.bz2`.

The raw data source, `jacana-qa-naacl2013-data-results.tar.bz2` with an MD5 checksum of `11f0275e95691594cd74825e0c341b7a`, is stored in this repository.

For convenience, the `data/` directory contains the following splits in a pseudo-XML format:

+ `TRAIN.xml`
+ `TRAIN-ALL.xml`
+ `DEV.xml`
+ `TEST.xml`

Per the README file in `jacana-qa-naacl2013-data-results.tar.bz2`, the source of the above files are as follows:

```
train-less-than-40.manual-edit.xml: TRAIN in paper
train2393.cleanup.xml.gz:           TRAIN-ALL in paper
dev-less-than-40.manual-edit.xml:   DEV in paper
test-less-than-40.manual-edit.xml:  TEST in paper
```

# DEPENDENCIES

- python 3.6
- [pytorch](http://pytorch.org/)
- numpy
- sklearn
- nltk
- scipy


# EMBEDDINGS

The pre-initialized word2vec embeddings have to be downloaded from [here](https://drive.google.com/folderview?id=0B-yipfgecoSBfkZlY2FFWEpDR3M4Qkw5U055MWJrenE5MTBFVXlpRnd0QjZaMDQxejh1cWs&usp=sharing).



# BUILD TrecQA Dataset

```
python3 parse.py

python3 overlap_features.py

python3 build_vocab.py

python3 build_qrels.py
```

The above command will parse the XML file into <question, answer> pairs into different folder:

+ `TRAIN.xml: train/`
+ `TRAIN-ALL.xml: train-all/`
+ `DEV.xml: raw-dev/`
+ `TEST.xml:raw-test/`

We also calulate the 4 overlapping features between each question and answer pair and save them into different folder.

build_vocab.py will save all the tokens appear in the question and answer pairs for loading corresponding word embeddings. 