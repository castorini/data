:::::::::::: SICK (Sentences Involving Compositional Knowledge) data set ::::::::::::


The SICK data set consists of 10,000 English sentence pairs, built starting from two existing 
paraphrase sets: the 8K ImageFlickr data set and the SEMEVAL-2012 Semantic Textual Similarity Video Descriptions data set. Each sentence pair is annotated for relatedness in meaning and for the entailment relation between the two elements.

The SICK data set is used in SemEval 2014 - Task 1: Evaluation of compositional distributional 
semantic models on full sentences through semantic relatedness and textual entailment

The current release is a subset of the data set representing Task 1 Test data (4927 sentence pairs)

We preprocessed the original dataset and generated the ``train``, ``dev`` and ``test`` directories, each containing the following layout:

```
dev
├── a.toks
├── a.txt
├── a.parents
├── a.rels
├── b.toks
├── b.txt
├── b.parents
├── b.rels
├── id.txt
└── sim.txt
```

Each line in ``a.toks`` contains one question (the same question repeats in subsequent lines for as many times as the number of candidate answers).

Each line in ``b.toks`` contains one candidate answer.

Each line in ``sim.txt`` contains the label (0 or 1) for the question-answer pair in the corresponding line of ``a.toks`` and ``b.toks`` respectively.

Each line in ``id.txt`` contains the question-id for question at the corresponding line in ``a.toks``

Each line in ``a.parents`` or ``b.parents`` and ``a.rels`` or ``b.rels`` contains the output of Standford dependency parser, for head words and dependency arcs separately.

Each line in ``a.txt`` or ``b.txt`` contains original untokenized texts from the original source.

