import os
import glob
from shutil import copyfile

from nltk.tokenize import TreebankWordTokenizer


def build_vocab(filepaths, dst_path, lowercase=True):
    """
    Builds a vocabulary list for the dataset
    """
    vocab = set()
    for filepath in filepaths:
        with open(filepath, encoding='utf-8') as f:
            for line in f:
                if lowercase:
                    line = line.lower()
                vocab |= set(line.split())
    with open(dst_path, 'w', encoding='utf-8') as f:
        for w in sorted(vocab):
            f.write(w + '\n')


def dump(data, outfile):
    with open(outfile, 'w', encoding='utf-8') as outf:
        outf.write('\n'.join(data) + '\n')


def write_out(infile, out_folder):
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)

    qfile = open(os.path.join(out_folder, 'a.toks'), 'w', encoding='utf-8')
    afile = open(os.path.join(out_folder, 'b.toks'), 'w', encoding='utf-8')
    lfile = open(os.path.join(out_folder, 'sim.txt'), 'w', encoding='utf-8')

    ids = []
    questions = []
    answers = []
    labels = []

    tokenizer = TreebankWordTokenizer()

    qid_count = 0
    with open(infile, encoding='utf-8') as inf:
        inf.readline() # header
        for i, line in enumerate(inf):
            fields = line.lower().strip().split('\t')
            question = ' '.join(tokenizer.tokenize(fields[3]))
            sentence = ' '.join(tokenizer.tokenize(fields[4]))
            label = fields[0]

            ids.append(str(i+1))
            questions.append(question)
            answers.append(sentence)
            labels.append(label)

    dump(questions, os.path.join(out_folder, 'a.toks'))
    dump(answers, os.path.join(out_folder, 'b.toks'))
    dump(labels, os.path.join(out_folder, 'sim.txt'))
    dump(ids, os.path.join(out_folder, 'id.txt'))


if __name__ == "__main__":
    write_out('msr_paraphrase_train.txt', 'train')
    write_out('msr_paraphrase_test.txt', 'test')

    build_vocab(
        glob.glob(os.path.join('.', '*/*.toks')),
        os.path.join('.', 'vocab.txt'), False
    )

