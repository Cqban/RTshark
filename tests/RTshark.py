import pyshark
import nmap
import threading

scanner = nmap.PortScanner()
ip_addr = input("Adresse IP à scanner : ")
scanfinished = False

def sniff(object):
    object.sniff(timeout=0)

#Capture wireshark avec filtre ciblant les segment ayant pour flag SYN et ACK (réponses signifiant qu'un port est ouvert suite au scan nmap)
def capturewireshark():
    capture = pyshark.LiveCapture(interface="Wi-Fi", bpf_filter='tcp[tcpflags] == tcp-syn|tcp-ack', output_file='./nomduprojet/capture.pcap')
    threading.Thread(target=sniff,args=[capture]).start()
    while scanfinished: # Quand scanfinished = True, stopper la capture
        capture.close()

# balayage des ports 1 à 1024 en mode TCP Scan de l'@ IP choisie
def scannmap():
    scanner.scan(ip_addr,'1-1024', '-v -sT') # équivalent de "nmap [ip] -p 1-1024 -v -sT"
    print(scanner.scaninfo())
    scanfinished = True

threading.Thread(target=capturewireshark).start()
threading.Thread(target=scannmap).start()

# Traitement du fichier pcap
capturefile = pyshark.FileCapture("capture.pcap")

liste = []
for p in capturefile:
    if hasattr(p, 'tcp'):
        liste.append(p.tcp.srcport)

with open('textfile.txt', 'w') as input:
    for listitem in sorted(set(liste)):
        input.write(f'{listitem}\n')
