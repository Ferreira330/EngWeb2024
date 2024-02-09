import xml.etree.ElementTree as xml

def trataImagens(file):
    HTML = ""
    etree = xml.parse(file).getroot()
    #root = etree.getroot()
    corpo = etree.find('corpo')
    for figura in corpo.findall('figura'):
        id = figura.get('id')
        path = figura.find('imagem').get('path')
        legenda = figura.find('legenda').text
        HTML += f"<img id = {id} src='{path}' alt='{legenda}' width = 100%>"

    #for para in corpo.findall('para'):
        #HTML += f"<p>{para.text}</p>"
    return HTML


def trataCasas(file):
#lista_listas = etree.xpath('//lista-casas')
    HTML = ""
    etree = xml.parse(file)
    root = etree.getroot()
    if root.find('corpo').find('lista-casas') is not None:
        lista_casas = root.find('corpo').find('lista-casas')
        HTML += "<ul>" #abrir o itemize
        for casa in lista_casas.findall('casa'):
            HTML += "<li>" #abrir o item

            numero = casa.find('número').text
            HTML += f"<h2>Número: {numero}</h2>"

            enfiteuta = casa.find('enfiteuta')
            HTML += f"<p>Enfiteuta: {enfiteuta}</p>"
            
            foro = casa.find('foro')
            if foro is not None:
                HTML += f"<p>Foro: {foro.text}</p>"

            descricao = casa.find('desc')
            if descricao is not None:
                HTML += "Descrição: "
                for child in descricao:
                    if child.tag in ['para']:
                        HTML += f"<p>{child.text}</p>"
                        if child.tail:
                            HTML += f"{child.tail}"
                    if child.tag in ['lugar','entidade','data']:
                        HTML += f"<b>{child.text}</b>"
                        print("entrou aqui")
                        if child.tail:
                            HTML += f"{child.tail}"
                    if child.tail:
                        HTML += f"{child.tail}"
        HTML += "</ul>" #fechar o itemize
    return HTML


def trataPara(file):
    HTML = ""
    etree = xml.parse(file)
    root = etree.getroot()
    lista_paras = root.find('corpo')
    for para in lista_paras.findall('para'):
        HTML += f"<p>"
        HTML += f"{para.text}"
        for child in para:
            if child.tag in ['lugar','data']:
                HTML += f"<b>{child.text}</b>"
            if child.tail:
                HTML += f"{child.tail}"
        HTML += "</p>"

    return HTML


def getNome(file):
    etree = xml.parse(file)
    root = etree.getroot()
    return root.find('meta').find('nome').text

