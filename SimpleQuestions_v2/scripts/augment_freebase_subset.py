#!/usr/bin/python

import argparse
import gzip

class RDFTriple(object):
    def __init__(self, sub, pred, obj):
        self.subject = sub
        self.predicate = pred
        self.object = obj

    def __str__(self):
        return '%s\t%s\t%s\t.' % (self.subject, self.predicate, self.object)

    def __lt__(self, other):
        return not other.subject < self.subject

def is_url(field):
    if field.startswith("<http"):
        return True
    return False

def extract_predicate(cand_pred):
    preds_suffix_to_be_extracted = [
        "ns/type.object.name>",
        "ns/common.topic.alias>",
        "key/wikipedia.en_title>",
        "2000/01/rdf-schema#label>"
    ]
    for pred in preds_suffix_to_be_extracted:
        if cand_pred.endswith(pred):
            return True
    return False

def augment(freebase_fn, fbsubset_fn, out_fn):
    rdf_triples = []
    fbsubset_entities = set()

    # get entities from freebase-subset
    with open(fbsubset_fn, 'r') as f:
        for linenum, line in enumerate(f):
            sub, pred, obj, _ = line.strip().split('\t')
            fbsubset_entities.add(sub)
            if is_url(obj):  # skip if it is literal
                fbsubset_entities.add(obj)

            rdf_triple = RDFTriple(sub, pred, obj)
            rdf_triples.append(rdf_triple)

            if (linenum % 1000000 == 0):
                print("file: {}, line number: {}".format("freebase-subset", linenum))

    # extract predicates for those entities from entire freebase
    with gzip.open(freebase_fn, 'rb') as f:
        for linenum, line in enumerate(f):
            sub, pred, obj, _ = line.decode().strip().split('\t')
            # extract relevant predicate and make sure object is literal, not another entity
            if sub in fbsubset_entities and extract_predicate(pred) and not is_url(obj):
                # print(line.decode().strip())
                rdf_triple = RDFTriple(sub, pred, obj)
                rdf_triples.append(rdf_triple)

            if (linenum % 1000000 == 0):
                print("file: {}, line number: {}".format("freebase", linenum))

    # sort and write to outfile
    rdf_triples.sort()
    with open(out_fn, 'w') as fo:
        for rdf_triple in rdf_triples:
            # print('%s' % (str(rdf_triple)))
            fo.write('%s\n' % (str(rdf_triple)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Augment Freebase subset to include additional fields')
    parser.add_argument('-f', '--freebase', dest='freebase', action='store', required = True,
                        help='path to entire freebase dump - GZIP file')
    parser.add_argument('-s', '--fbsubset', dest='fbsubset', action='store', required=True,
                        help='path to freebase subset file')
    parser.add_argument('-o', '--output', dest='output', action='store', required=True,
                        help='output file')

    args = parser.parse_args()
    print("Input - freebase: {}".format(args.freebase))
    print("Input - fbsubset: {}".format(args.fbsubset))
    print("Output: {}".format(args.output))
    augment(args.freebase, args.fbsubset, args.output)
    print("Augmented freebase-subset with extracted predicates for entities.")
