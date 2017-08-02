#!/usr/bin/env python

import os
import sys
import zipfile

from tqdm import tqdm
from urllib.request import urlretrieve

from utils import md5, reporthook

TXT_FILE = 'glove.840B.300d.txt'
ZIP_FILE = 'glove.840B.300d.zip'
GLOVE_TXT_MD5 = 'eec7d467bccfa914726b51aac484d43a'
GLOVE_ZIP_MD5 = '2ffafcc9f9ae46fc8c95f32372976137'
URL = 'http://nlp.stanford.edu/data/glove.840B.300d.zip'


if __name__ == '__main__':
    if os.path.isfile(TXT_FILE) and md5(TXT_FILE) == GLOVE_TXT_MD5:
        print('{} already exists. Skipping download.'.format(TXT_FILE))
        sys.exit(0)

    if os.path.isfile(ZIP_FILE) and md5(ZIP_FILE) == GLOVE_ZIP_MD5:
        print('{} already exists. Skipping download. Unzip it to extract the embeddings.'.format(ZIP_FILE))
        sys.exit(0)

    print('Downloading GloVe Common Crawl (840B tokens, 2.2M vocab, cased, 300d vectors, 2.03 GB download)')
    with tqdm(unit='B', unit_scale=True, miniters=1, desc=ZIP_FILE) as t:
        fname, _ = urlretrieve(URL, ZIP_FILE, reporthook=reporthook(t))
        with zipfile.ZipFile(fname, "r") as zf:
            zf.extractall('.')
