"""
.. module:: write_webpage
   :platform: Unix, windows
   :synopsis: Writing HTML file function

.. moduleauthor:: Lechevrel Malko Fournier Vincent <malko.lechevrel@etu.univ-poitiers.fr>

"""

def write_page(html, output_file):
    """
    This function write the content of the generate_webpage function inside of a HTML file.

    :param args: Output file
    :type args: str
    :raises: TypeErrorWrite
    :example: 

    index.html
    
    """

    with open(output_file, 'w') as f:
        f.write(html)