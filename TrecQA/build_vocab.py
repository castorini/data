import os
import glob
import argparse

def build_vocab(filepaths, dst_path, lowercase=True):
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

if __name__ == "__main__":
    # ap = argparse.ArgumentParser(description='builds vocabulary for TrecQA')
    # ap.add_argument('data_dir', help='the training data folder')
    # args = ap.parse_args()

    print('builds vocabulary for TrecQA')
    build_vocab(
        glob.glob(os.path.join('.', '*/*.toks')),
        os.path.join('.', 'vocab.txt'), False)
