import os

for set in ['train-all', 'raw-test', 'raw-dev']:

    with open(set + '.qrel', 'w') as qrelf:
        labels = [y.strip() for y in open(os.path.join(set+'/sim.txt')).readlines()]
        qids = [id.strip() for id in open(os.path.join(set+'/id.txt')).readlines()]

        for i in range(len(labels)):
            qid = qids[i]
            lbl = labels[i]
            print('{} {} {} {}'.format(qid, '0', i, lbl), file=qrelf)

    