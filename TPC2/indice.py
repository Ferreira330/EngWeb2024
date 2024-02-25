import os, json
port = 8080
file = open("mapa-virtual.json", "r", encoding="utf-8")
db = json.load(file)


HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Mapa</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>Mapa</h1>
    <div id="map" style="width: 100%; height: 500px;">
    <ul>
'''

for cidade in db["cidades"]:
    id = cidade["id"]
    nome = cidade["nome"]
    if id[0] == "c":
        HTML += f'''
            <li><a href="http://localhost:{port}/{id}">{nome}</a></li>
        '''

HTML += '''
    </ul>
    </div>
</body>
</html>
'''
ind = os.makedirs("HTML", exist_ok=True)
ind = open("HTML/indice.html", "w", encoding="utf-8")
ind.write(HTML)
ind.close()