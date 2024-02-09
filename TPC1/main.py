import os
import parser

pasta_texto = "./texto"
os.makedirs("HTML", exist_ok=True)

template = '''
<!DOCTYPE html>
<html>
<head>
    <title>
    EW TPC1
    </title>
    <meta charset="UTF-8">
</head>
<body>
'''

files= "./texto/MRB-52-RuaEmFrenteDeNossaSenhoraDeGuadalupe.xml"
for file in os.listdir(pasta_texto):
    HTML = template
    if file.endswith(".xml"):
        HTML += parser.trataImagens(f"./texto/{file}")
        HTML += parser.trataPara(f"./texto/{file}")
        HTML += parser.trataCasas(f"./texto/{file}")
        HTML += "</body>"
        HTML += "</html>"
        mapa = open(f"./HTML/{parser.getNome(f"./texto/{file}")}.html", "w", encoding="utf-8")
        mapa.write(HTML)
        mapa.close()
        #else:
            #continue

