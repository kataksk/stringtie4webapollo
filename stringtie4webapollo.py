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
            if line[2] == 'transcript':
                # line[2] = 'mRNA'
                # print(line)
                # output = '\t'.join(line[0:8]) + '\t' + feature_converter(line[8], line[2])
                output = '\t'.join(line[0:2]) + '\t' + 'mRNA' + '\t' +'\t'.join(line[3:8])+ '\t' + feature_converter(line[8], line[2])
                # output = str(line[0]) + '\t' + str(line[1]) + '\t' + str(line[2]) + '\t' + str(line[3]) + '\t' + str(line[4]) + '\t' + str(line[5]) + '\t' + str(line[6]) + '\t' + str(line[7]) + '\t' + feature_converter(line[8], line[2])
                print(output)
            elif line[2] == 'exon':
                # line[2] = 'CDS'
                # print(line)
                # output = '\t'.join(line[0:8]) + '\t' + feature_converter(line[8], line[2])
                output = '\t'.join(line[0:2]) + '\t' + 'CDS' + '\t' +'\t'.join(line[3:8])+ '\t' + feature_converter(line[8], line[2])
                # output = str(line[0]) + '\t' + str(line[1]) + '\t' + str(line[2]) + '\t' + str(line[3]) + '\t' + str(line[4]) + '\t' + str(line[5]) + '\t' + str(line[6]) + '\t' + str(line[7]) + '\t' + feature_converter(line[8], line[2])
                print(output)
