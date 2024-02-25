import json, os
port = 8080
file = open("mapa-virtual.json", "r", encoding="utf-8")
db = json.load(file)

def city_name(id):
    for cidade in db["cidades"]:
        if (cidade["id"] == id):
            return cidade["nome"]


for cidade in db["cidades"]:
    id = cidade["id"]
    nome = cidade["nome"]
    if id[0] == "c":
        HTML = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>{nome}</title>
            <meta charset="utf-8">
        </head>
        <body>
            <h1>{nome}</h1>
            <p><b>Nome:</b> {cidade["nome"]}</p>
            <p><b>ID:</b> {cidade["id"]}</p>
            <p><b>População:</b> {cidade["população"]}</p>
            <p><b>Distrito:</b> {cidade["distrito"]}</p>
            <h3><b>Descrição:</b></h3>
            <p>{cidade["descrição"]}</p>

            <h3><b>Ligações:</b></h3>
            <ul>
        '''
        for ligacao in db["ligacoes"]:
            if(ligacao["origem"] == id):
                HTML += f'''
                <li><a href="http://localhost:{port}/{ligacao["id"]}">{city_name(ligacao["destino"])}</a><b> Distância: {ligacao["distância"]}</li>'''

        HTML += '''
            </ul>
        </body>
        </html>
        '''
        f1 = open(f"HTML/{id}.html", "w", encoding="utf-8")
        f1.write(HTML)
        f1.close()

file.close()

                
        
