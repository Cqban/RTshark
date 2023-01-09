import pyshark
import argparse
import webbrowser
from module1 import generate_webpage

# Function to extract a list of unique port numbers from a pcap file
def extract_ports(capture_file):
    port_list = []
    for packet in capture_file:
        if hasattr(packet, 'tcp'):
            port_list.append(int(packet.tcp.srcport))
    return sorted(set(port_list))

# Function to write the given HTML code to the specified file
def write_page(html, output_file):
    with open(output_file, 'w') as f:
        f.write(html)

# Main function which handles arguments and the processing of the other functions.
def main():
    parser = argparse.ArgumentParser()                                               
    parser.add_argument('--input-file', help="PCAP file to analyze", required=True)
    parser.add_argument('--output-file', help="Output file to write the HTML code", required=True)
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    capture_file = pyshark.FileCapture(input_file)
    port_list = extract_ports(capture_file)
    html = generate_webpage(port_list)
    write_page(html, output_file)
    webbrowser.open_new_tab(output_file)

if __name__ == "__main__":
    main()
