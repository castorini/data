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

