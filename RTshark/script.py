import pyshark

# Traitement du fichier pcap
capturefile = pyshark.FileCapture("capture.pcap")

liste = []
for p in capturefile:
    if hasattr(p, 'tcp'):
        liste.append(p.tcp.srcport)

with open('textfile.txt', 'w') as input:
    for listitem in sorted(set(liste)):
        input.write(f'{listitem}\n')