#!/usr/bin/python

import argparse

def www2fb(in_str):
    out_str = 'http://rdf.freebase.com/ns/%s' % (in_str.split('www.freebase.com/')[-1].replace('/', '.'))
    return out_str

def convert(infilename, outfilename):
    triple_dict = {}
    with open(infilename, 'r') as f:
        for linenum, line in enumerate(f):
            fields = line.strip().split('\t')
            sub = www2fb(fields[0])
            rel = www2fb(fields[1])
            objs = fields[2].split()
            for obj in objs:
                obj = www2fb(obj)
                triple_dict[(sub, rel, obj)] = 1

            if (linenum % 1000000 == 0):
                print("line number: {}".format(linenum))

    with open(outfilename, 'w') as fo:
        for (sub, rel, obj) in triple_dict.keys():
            # print( '<%s>\t<%s>\t<%s>\t.' % (sub, rel, obj) )
            fo.write( '<%s>\t<%s>\t<%s>\t.\n' % (sub, rel, obj) )
    print(len(triple_dict))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Freebase subset URLs to Freebase format')
    parser.add_argument('-i', '--input', dest='input', action='store', required = True,
                        help='freebase subset file')
    parser.add_argument('-o', '--output', dest='output', action='store', required=True,
                        help='output file')

    args = parser.parse_args()
    print("Input: {}".format(args.input))
    print("Output: {}".format(args.output))
    convert(args.input, args.output)
    print("Converted freebase-subset to NTriples format.")
