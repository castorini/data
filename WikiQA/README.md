WikiQA
------

### References

1. Yang, Yi, Wen-tau Yih, and Christopher Meek. "WikiQA: A Challenge Dataset for Open-Domain Question Answering." EMNLP. 2015.
2. https://www.microsoft.com/en-us/research/publication/wikiqa-a-challenge-dataset-for-open-domain-question-answering/


### Getting the data
You can download the dataset from [here](https://www.microsoft.com/en-us/download/confirmation.aspx?id=52419) or [here](http://aka.ms/WikiQA)


### (Pre-) Processing

```
unzip WikiQACorpus.zip
```
Remember to read ``WikiQACorpus/README.txt`` for a detailed description of the dataset.
Note that the qrels are ``WikiQACorpus/*ref`` for the train, dev, and test sets.


To convert data to *standard* format, run

```
python create-train-dev-test-data.py 
```

This generates the ``train``, ``dev`` and ``test`` directories, each containing the following layout:

```
dev
├── a.toks
├── b.toks
├── id.txt
└── sim.txt
```

Each line in ``a.toks`` contains one question (the same question repeats in subsequent lines for as many times as the number of candidate answers).

Each line in ``b.toks`` contains one candidate answer.

Each line in ``sim.txt`` contains the label (0 or 1) for the question-answer pair in the corresponding line of ``a.toks`` and ``b.toks`` respectively.

Each line in ``id.txt`` contains the question-id for question at the corresponding line in ``a.toks``

