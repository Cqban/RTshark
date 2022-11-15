import pyshark
import nmap

# scanner = nmap.PortScanner()
# ip_addr = input("Adresse IP à scanner : ")

capture = pyshark.LiveCapture(interface='Wi-Fi', display_filter='tcp.flags.syn==1 and tcp.flags.ack==1', output_file='prout.pcap')
capture.sniff(timeout=20000)
print(capture)

# scanner.scan(ip_addr,'1-65535', '-v -sS')
# print(scanner.scaninfo())
# print("Etat de l'adresse IP: ", scanner[ip_addr].state())
# print("Ports Ouverts: ", scanner[ip_addr]['tcp'].keys())


# capturefile = pyshark.FileCapture("capture.pcap")

# liste = []
# for p in capturefile:
#     if hasattr(p, 'tcp'):
#         liste.append(p.tcp.srcport)

# with open('textfile.txt', 'w') as input:
#     for listitem in sorted(set(liste)):
#         input.write(f'{listitem}\n')



