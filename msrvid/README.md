:::::::::::: MSRVID (Microsoft Research Video Caption) data set ::::::::::::


The MSRVID data set consists of 900 English sentence pairs, was usd in SemEval 2012 STS competition.

We preprocessed the original dataset and generated files in two directories, each directory containing the following layout:

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

