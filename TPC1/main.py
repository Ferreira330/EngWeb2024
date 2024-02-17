import os
import parser

pasta_texto = "./texto"
os.makedirs("HTML", exist_ok=True)
HTML_INDEX = """<!DOCTYPE html>
<html>
<head>
    <title>
    EW TPC1 - Index
    </title>
    <meta charset="UTF-8">
</head>
<body>
<h1>Index</h1>
<ul>
"""
for file in os.listdir(pasta_texto):
    if file.endswith(".xml"):
        HTML = parser.trataPara(f"./texto/{file}")
        open(f"./HTML/{file}.html", "w", encoding="utf-8").write(HTML)
        HTML_INDEX += f"<li><a href='{file}.html'>{file}</a></li>\n"

HTML_INDEX += "</ul>\n"
HTML_INDEX += "</body>\n"
HTML_INDEX += "</html>"
mapa = open(f"./HTML/index.html", "w", encoding="utf-8")
mapa.write(HTML_INDEX)
mapa.close()

        