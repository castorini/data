import re
import os
import numpy as np
# import cPickle
import subprocess
from collections import defaultdict
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem.porter import *

UNKNOWN_WORD_IDX = 0


def load_data(fname):
  lines = open(fname, encoding='utf-8').readlines()
  qids, questions, answers, labels = [], [], [], []
  num_skipped = 0
  prev = ''
  qid2num_answers = {}
  for i, line in enumerate(lines):
    line = line.strip()

    qid_match = re.match('<QApairs id=\'(.*)\'>', line)

    if qid_match:
      qid = qid_match.group(1)
      qid2num_answers[qid] = 0

    if prev and prev.startswith('<question>'):
      question = line.lower().split('\t')

    label = re.match('^<(positive|negative)>', prev)
    if label:
      label = label.group(1)
      label = 1 if label == 'positive' else 0
      answer = line.lower().split('\t')
      labels.append(label)
      answers.append(answer)
      questions.append(question)
      qids.append(qid)
      qid2num_answers[qid] += 1
    prev = line

  return qids, questions, answers, labels



def add_to_vocab(data, alphabet):
  for sentence in data:
    for token in sentence:
      alphabet.add(token)



def write_to_file(xmlF,outdir):
  
  if not os.path.exists(outdir):
    os.makedirs(outdir)

  
  qids, questions, answers, labels = load_data(xmlF)
  
  qid_file = open(outdir+'/id.txt','w', encoding='utf-8')
  for qid in qids:
    qid_file.write(qid+'\n')
  qid_file.close()


  questions_file = open(outdir+'/a.toks','w', encoding='utf-8')
  for q in questions:
    # q_toks = TreebankWordTokenizer().tokenize(' '.join(q))
    q_str = ' '.join(q).lower()
    questions_file.write(q_str+'\n')
  questions_file.close()


  answers_file = open(outdir+'/b.toks','w', encoding='utf-8')
  for a in answers:
    # a_toks = TreebankWordTokenizer().tokenize(' '.join(a))
    a_str = ' '.join(a).lower()
    answers_file.write(a_str+'\n')
  answers_file.close()


  sim_file = open(outdir+'/sim.txt','w', encoding='utf-8')
  for label in labels:
    sim_file.write(str(label)+'\n')
  sim_file.close()

  print(outdir+' dataset done!')



if __name__ == '__main__':

  stoplist = None


  train = 'data/TRAIN.xml'
  write_to_file(train,'train')
  train_all = 'data/TRAIN-ALL.xml'
  write_to_file(train_all,'train-all')  

  dev = 'data/DEV.xml'
  write_to_file(dev,"raw-dev")
  test = 'data/TEST.xml'
  write_to_file(test,"raw-test")

    
