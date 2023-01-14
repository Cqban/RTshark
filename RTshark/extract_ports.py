"""
.. module:: extract_ports
   :platform: Unix, windows
   :synopsis: Port extraction function

.. moduleauthor:: Lechevrel Malko Fournier Vincent <malko.lechevrel@etu.univ-poitiers.fr>

"""

def extract_ports(capture_file):
    """
    This function allows you to extract open ports from a PCAP file.

    :param args: PCAP file
    :type args: str
    :returns: Returns the open ports as a list.
    :rtype: int
    :raises: TypeError
    :example: 

    [80, 443, 25565]
    """
    port_list = []
    for packet in capture_file:
        print(packet)
        if "ACK" in str(packet):
            print("a")
            port_list.append(int(packet.tcp.srcport))
    return sorted(set(port_list))