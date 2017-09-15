#!/usr/bin/env python

import os
import sys
import zipfile

from tqdm import tqdm
from urllib.request import urlretrieve

from utils import md5, reporthook

TXT_FILE = 'paragram_vectors.txt'
MD5 = 'b6b66e1e16bf6e08f228f3b6c2147900'
URL = 'http://ttic.uchicago.edu/~wieting/paragram_vectors.txt'


if __name__ == '__main__':
    if os.path.isfile(TXT_FILE) and md5(TXT_FILE) == MD5:
        print('{} already exists. Skipping download.'.format(TXT_FILE))
        sys.exit(0)

    print('Downloading paragram embedding')
    with tqdm(unit='B', unit_scale=True, miniters=1, desc=TXT_FILE) as t:
        fname, _ = urlretrieve(URL, TXT_FILE, reporthook=reporthook(t))
