import sys

stringtie_gtf_input = sys.argv[1]

def feature_converter(feature, type):
    if type == 'transcript':
        feature_split = feature.split('"; ')
        id_start = feature_split[1].find('"')
        output = 'ID=' + feature_split[1][id_start+1:]
        return output
    elif type == 'exon':
        feature_split = feature.split('"; ')
        id_start = feature_split[1].find('"')
        output = 'ID=' + feature_split[1][id_start+1:] + '.exon;Parent=' + feature_split[1][id_start+1:]
        return output

with open(stringtie_gtf_input, 'r') as f:
    for line in f:
        if line[0] == '#':
            continue
        else:
            line = line.rstrip('\n').split('\t')
            output = '\t'.join(line[0:8]) + '\t' + feature_converter(line[8], line[2])
            print(output)
