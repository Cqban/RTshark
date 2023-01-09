import pyshark
import argparse
import webbrowser

# Function to extract a list of unique port numbers from a pcap file
def extract_ports(capture_file):
    port_list = []
    for packet in capture_file:
        if hasattr(packet, 'tcp'):
            port_list.append(int(packet.tcp.srcport))
    return sorted(set(port_list))

# Function to generate an HTML page displaying the given list of ports
def generate_webpage(port_list):
    # Code CSS
    codecss = """body{
    background-image: url(https://i.postimg.cc/Nj375g1j/background.jpg);
    }
        .rslt {
            display: flex;
        justify-content: center;
        align-items: center;
        border:1px #C0C0C0;
        border-style: solid;
        border-radius: 5px;
        background: black;
    }
        .rslt th {
        border:1px black;
        background:#F0F0F0;
        border-style: groove;
        border-radius: 10px;
        font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
        font-size: 2rem;
    }
        .rslt td {
        font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
        font-size: medium;
        text-shadow: 3px white;
        font-style: bold;
        border:1px white;
        color: white;
        background: black;
    }"""
    
    # Code HTML
    codehtml = f"""
    <!DOCTYPE html>
    <html lang="en">
    <style>
        {codecss}
    </style>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="/css/style.css">
        
        <title>Open Ports</title>
    </head>
    <body>
        <table class="rslt">
            <tr>
                <th>List of Open Ports</th>
            </tr>
            <tr>
                <td>{port_list}</td>
            </tr>
    <tbody>
        
            </tbody>
        </table>
    </body>
    </html>""" 

    return codehtml

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
