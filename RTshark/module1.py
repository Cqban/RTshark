"""
.. module:: generate_webpage
   :platform: Unix, windows
   :synopsis: module1 du projet

.. moduleauthor:: Lechevrel Malko Fournier Vincent <malko.lechevrel@etu.univ-poitiers.fr>

"""

# Function to generate an HTML page displaying the given list of ports
def generate_webpage(port_list):
    ''' Cette fonction fait un truc
	
    :param port_list: variable mes couilles
	

    '''
    # Code CSS
    codecss = """
body {
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
        font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
        font-size: 2rem;
    }
        .rslt td {
        font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
        font-size: medium;
        text-shadow: 3px white;
        font-style: bold;
        border:1px white;
        color: white;
        background: black;
        text-align: center;
    }

        #logo {
            width: 25%;
            margin-top: 10%;
            margin-left: 38%;    
    }
    """
    
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
        </table>
        <img src="https://i.postimg.cc/sxLyrXQs/rtshark.png" id="logo" alt="RTshark Logo"/>
    </body>
    </html>""" 

    return codehtml

   
