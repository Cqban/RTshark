import pyshark
import argparse
import webbrowser
from write_page import write_page
from extract_ports import extract_ports
from generate_webpage import generate_webpage

# Main function which handles arguments and the processing of the other functions.
def main():
    parser = argparse.ArgumentParser()                                               
    parser.add_argument('--input-file', help="PCAP file to analyze", required=True)
    parser.add_argument('--output-file', help="Output file to write the HTML code", required=True)
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    #Ouverture du fichier pcap avec pyshark en appliquant un filtre pour les segments TCP ayant les flag SYN et ACK
    capture_file = pyshark.FileCapture(input_file)
    port_list = extract_ports(capture_file)
    html = generate_webpage(port_list)
    write_page(html, output_file)
    webbrowser.open_new_tab(output_file)

if __name__ == "__main__":
    main()