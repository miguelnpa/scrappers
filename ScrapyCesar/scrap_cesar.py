# Acessar o link: https://cesar.breezy.hr/
# Verificar, dentro da classe div.class = "positions-container" ir até a classe li.class = "position transition" 
# Pegar o a.href e o a.h2 = "Senior Data Scientista [manaus]"
# Se o a.h2 que existirem na página forem diferentes dos a.h2 que existem no documento de texto, abrir um novo arquivo TXT 
# Escrito "NOVOS PROCESSOS DISPONÍVEIS NO CESAR, CONFERIR!!"

#### PRIMEIRA FUNÇÃO - Abrir o arquivo Validação.txt, ler o texto dentro e retornar um lista com strings dos nomes em validacao.txt

from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

validacaoAdress = 'C:/Projetos/ScrapyCesar/validacao/validacao.txt'
link = 'https://cesar.breezy.hr/'
aviso = 'vaga.txt'

def read_file(fileLocation):
    trueJobList = []
    with open(fileLocation, 'r',encoding='utf-8') as f:
        jobList = f.read().split(',')
        for i in jobList:
            trueJobList.append(i.strip('\n'))
        return trueJobList


#### SEGUNDA FUNÇÃO - Acessar o link https://cesar.breezy.hr/ e retornar um objeto bs

def access_link(link):
    html = urlopen(link)
    bs = BeautifulSoup(html.read(), 'html.parser')
    return bs




# TERCEIRA FUNÇÃO - RETORNAR A LISTA COM OS H2 DENTRO DO LINK

def h2_list_return(bs):
    h2List = []
    find_class = bs.find_all('li', class_ = 'position transition')
    for li_tag in find_class:
        a_tag = li_tag.find('a')
        if a_tag:
            h2_tag = a_tag.find('h2')
            if h2_tag:
                h2List.append(h2_tag.text)
    return h2List

# QUARTA FUNÇÃO - COMPARAR A LISTA ENCONTRADA DOS H2 COM A LISTA PRÉVIA SALVA NO COMPUTADOR

def list_comparison(h2_list,file_list):
    if h2_list == file_list:
        return True
    else:
        return False

# QUINTA FUNÇÃO - ABRIR UM DOCUMENTO TXT ESCRITO "NOVOS PROCESSOS DISPONÍVEIS NO CESAR, CONFERIR!!"

def open_warning(aviso):
    return os.system(aviso)

# SEXTA FUNÇÃO - CASO A LISTA SEJA DIFERENTE

def validation_warning(list_comparison,warning):
    if list_comparison == True:
        return
    elif list_comparison == False:
        return open_warning(warning)
    

file_list = read_file(validacaoAdress)
bs = access_link(link)  
h2_list = h2_list_return(bs)
comparison = list_comparison(h2_list,file_list)
validation_comparison = validation_warning(comparison,aviso)