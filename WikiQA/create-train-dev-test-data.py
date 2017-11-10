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

    qids = []
    questions = []
    answers = []
    labels = []

    tokenizer = TreebankWordTokenizer()

    qid_count = 0
    qid_old = None
    qid_labels = []
    qid_questions = []
    qid_answers = []
    qid_qids = []
    with open(infile, encoding='utf-8') as inf:
        inf.readline() # header
        for line in inf:
            fields = line.lower().strip().split('\t')
            qid = fields[0]
            question = ' '.join(tokenizer.tokenize(fields[1]))
            sentence = ' '.join(tokenizer.tokenize(fields[5])[:40])
            label = fields[6]
            if qid != qid_old:
                qid_old = qid
                qid_count += 1
                if "1" in qid_labels: # and "0" in qid_labels:
                    qids.extend(qid_qids)
                    questions.extend(qid_questions)
                    answers.extend(qid_answers)
                    labels.extend(qid_labels)
                qid_labels = []
                qid_questions = []
                qid_answers = []
                qid_qids = []
            qid_qids.append(str(qid_count))
            qid_questions.append(question)
            qid_answers.append(sentence)
            qid_labels.append(label)

    dump(questions, os.path.join(out_folder, 'a.toks'))
    dump(answers, os.path.join(out_folder, 'b.toks'))
    dump(labels, os.path.join(out_folder, 'sim.txt'))
    dump(qids, os.path.join(out_folder, 'id.txt'))

    if out_folder == 'train':
        with open(os.path.join('WikiQACorpus', 'WikiQA-{}.ref'.format(out_folder)), encoding='utf-8') as inqrel:
            with open('{}.qrel'.format(out_folder), 'w', encoding='utf-8') as outqrel:
                outqids = set(qids)
                for line in inqrel:
                    qid, zero, docid, label = line.strip().split()
                    if qid in outqids:
                        print(line.strip(), file=outqrel)
    else:
        copyfile(os.path.join('WikiQACorpus', 'WikiQA-{}-filtered.ref'.format(out_folder)), 
                 '{}.qrel'.format(out_folder))



if __name__ == "__main__":

    write_out(os.path.join('WikiQACorpus', 'WikiQA-train.tsv'), 'train')
    write_out(os.path.join('WikiQACorpus', 'WikiQA-dev.tsv'), 'dev')
    write_out(os.path.join('WikiQACorpus', 'WikiQA-test.tsv'), 'test')

    build_vocab(
        glob.glob(os.path.join('.', '*/*.toks')),
        os.path.join('.', 'vocab.txt'), False)

