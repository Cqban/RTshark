import pyshark
import sys
import argparse

parser = argparse.ArgumentParser()                                               
parser.add_argument( "input-file", type=str )
parser.add_argument( "output-file", type=str )
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file


# Traitement du fichier pcap
capturefile = pyshark.FileCapture(input_file)

liste = []
for p in capturefile:
    if hasattr(p, 'tcp'):
        liste.append(p.tcp.srcport)

with open(output_file, 'w') as input:
    for listitem in sorted(set(liste)):
        input.write(f'{listitem}\n')