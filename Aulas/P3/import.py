import csv
import json

def read_csv(file):
    bd = []
    try:
        with open(file, 'r') as f:
            csv_reader = csv.DictReader(f, delimiter=';')
            
            for row in csv_reader:
                bd.append(row)
    except FileNotFoundError:
        print(f'O ficheiro {file} não foi encontrado')
    except Exception as e:
        print(f'Erro: {e}')
    return bd

def pertence(lista, valor):
    encontrado = False
    i = 0
    while i < len(lista) and not encontrado:
        if lista[i]['designacao'] == valor:
            encontrado = True
        i += 1
    return encontrado

def calc_animais(bd):
    animais = []
    contador = 1
    for reg in bd:
        if not pertence(animais, reg['SpeciesIDDesc']):
            animais.append({
                "id": f"a{contador}",
                "designacao": reg["SpeciesIDDesc"],
            })
            contador += 1
    return animais

def calc_especies(bd):
    especies = []
    contador = 1
    for reg in bd:
        if not pertence(especies, reg['BreedIDDesc']) :
            especies.append({
                "id": f"e{contador}",
                "designacao": reg["BreedIDDesc"],
        })
            contador += 1
    return especies



file_path = 'Health_AnimalBites.csv'
myBD = read_csv(file_path)
especies = calc_especies(myBD)
animais = calc_animais(myBD)

nova_BD = {
    "ocorrencias": myBD,
    "especies" : especies,
    "animais" : animais,
}

f = open("mordidas.json", "w")
json.dump(nova_BD, f, indent=4)
f.close()
