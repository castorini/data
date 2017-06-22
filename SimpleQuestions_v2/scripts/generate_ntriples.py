
def www2fb(in_str):
    out_str = 'http://rdf.freebase.com/ns/%s' % (in_str.split('www.freebase.com/')[-1].replace('/', '.'))
    return out_str

def convert(infilename, outfilename):
    triple_dict = {}
    with open(infilename, 'r') as fi:
        for line in fi:
            fields = line.strip().split('\t')
            sub = www2fb(fields[0])
            rel = www2fb(fields[1])
            objs = fields[2].split()
            for obj in objs:
                obj = www2fb(obj)
                triple_dict[(sub, rel, obj)] = 1

    with open(outfilename, 'w') as fo:
        for (sub, rel, obj) in triple_dict.keys():
            # print( '<%s>\t<%s>\t<%s>\t.\n' % (sub, rel, obj) )
            fo.write( '<%s>\t<%s>\t<%s>\t.\n' % (sub, rel, obj) )
    print(len(triple_dict))

if __name__ == '__main__':
    try:
        in_fn = sys.argv[1]
        out_fn = sys.argv[2]
        print("Input: {}".format(in_fn))
        print("Output: {}".format(out_fn))
    except:
        print("ERROR: Wrong format.")
        print("USAGE: python generate_ntriples.py [freebase_subset_file] [output_filename]")

    convert(in_fn, out_fn)
    print("Converted freebase-subset to NTriples format.")
