import pyshark
import threading

scanfinished = False

def sniff(object):
    object.sniff(timeout=0)

capture = pyshark.LiveCapture(interface="Wi-Fi", bpf_filter='tcp[tcpflags] == tcp-syn|tcp-ack', output_file='./nomduprojet/capture.pcap')
threading.Thread(target=sniff,args=[capture]).start()
while scanfinished: # Quand scanfinished = True, stopper la capture
    capture.close()
