from lxml import etree as xml

def get_text_and_tail(element):
    text = element.text if element.text else ""
    for child in element:
        text += get_text_and_tail(child)
        text += child.tail if child.tail else ""
    return text


def trataPara(file):
    HTML = """<!DOCTYPE html>\n
    <html>\n
    """
    try:
        etree = xml.parse(file)
    except:
        return HTML
    #etree = xml.parse(file)
    root = etree.getroot()
    head = root.find('meta').find('nome').text
    HTML += f"<head><title>{head}</title><meta charset='UTF-8'></head>\n"
    body = root.find('corpo')
    HTML += "<body>\n"
    HTML += f"<h1> <a href= ./index.html>Voltar</a> </h1>\n"
    for para in body.findall('para'):
        HTML += f"<p>"
        HTML += f"{para.text}"
        for child in para:
            if child.tag in ['lugar','data']:
                HTML += f"<b>{child.text}</b>"
            if child.tail:
                HTML += f"{child.tail}"
        HTML += "</p>\n"
    for figura in body.findall('figura'):
        HTML += f"<img src='{figura.find('imagem').get('path')}' alt='{figura.find('legenda').text}' width=100%>\n"
    
    for l in body.findall('lista-casas'):
        HTML += "<ul>\n"
        for casa in l.findall('casa'):
            HTML += "<li>\n"
            HTML += f"<h2>Casa número: {casa.find('número').text}</h2>\n"
            if casa.find('enfiteuta') is not None:
                HTML += f"<p>Enfiteuta: {casa.find('enfiteuta').text}</p>\n"
            if casa.find('foro') is not None:
                HTML += f"<p>Foro: {casa.find('foro').text}</p>\n"
            HTML += "<p>Descrição: </p>\n"
            desc = casa.find('desc')
            HTML += "<p>"
            if desc is not None:
                HTML += get_text_and_tail(desc)
            HTML += "</p>"
        HTML += "</ul>\n"
    HTML += "</body>\n"
    HTML += "</html>"
    return HTML