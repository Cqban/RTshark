import pyshark

input_file_test = input("Choisis le fichier pcap dont tu veux extraire les ports: ")
capture_file_test = pyshark.FileCapture(input_file_test)

def extract_ports(capture_file_test):
    port_list_test = []
    for packet_test in capture_file_test:
        if hasattr(packet_test, 'tcp'):
            if "0x012" in str(packet_test):
                port_list_test.append(int(packet_test.tcp.srcport))
    print(sorted(set(port_list_test)))

extract_ports(capture_file_test)