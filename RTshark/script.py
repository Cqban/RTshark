import pyshark
import sys
import argparse

parser = argparse.ArgumentParser()                                               
parser.add_argument('--input-file', help="PCAP file to analyze", required=True)
parser.add_argument('--output-file', help="Output file to write the HTML code", required=True)
args = parser.parse_args()

input_file = (args.input_file)
output_file = (args.output_file)


# Traitement du fichier pcap
capturefile = pyshark.FileCapture(input_file)

liste = []
for p in capturefile:
    if hasattr(p, 'tcp'):
        liste.append(int(p.tcp.srcport))

listev2 = sorted(set(liste))

css = """body {
        background-color: red;
    }"""

codehtml = f"""
<?xml version=\"1.0\" encoding=\"UTF-8\" ?>
<!DOCTYPE html>
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"fr\" lang=\"fr\" dir=\"ltr\">
<style>
    {css}
</style>
<head>
<title> Mon titre </title>
</head>
<body>
    Liste des ports ouverts : {listev2}
</body>
</html>"""

with open(output_file, 'w') as writinghtml:
    writinghtml.write(codehtml)
