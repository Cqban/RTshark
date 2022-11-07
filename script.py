import pyshark

filename = input("Ecris le nom du fichier de capture dont tu veux extraire les ports source ouverts : ")
capturefile = pyshark.FileCapture(filename)

liste = []
for p in capturefile:
    if hasattr(p, 'tcp'):
        liste.append(p.tcp.srcport)
    if hasattr(p, 'udp'):
        liste.append(p.udp.srcport)

with open('textfile.txt', 'w') as input:
    for listitem in sorted(set(liste)):
        input.write(f'{listitem}\n')



