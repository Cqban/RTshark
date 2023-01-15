output_file_test = input("Nom du fichier html à générer: ")

html_test = """
    <!DOCTYPE html>
    <html lang="en">
    <style>
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
                <td>"Fake port list : [1, 2, 3, 4...]"</td>
            </tr>
        </table>
        <img src="https://i.postimg.cc/sxLyrXQs/rtshark.png" id="logo" alt="RTshark Logo"/>
    </body>
    </html>"""

def write_page(html_test, output_file_test):
    with open(output_file_test, 'w') as f:
        f.write(html_test)

write_page(html_test, output_file_test)