#from selenium import webdriver
#import tkinter
#import time
import pandas as pd

def load_contatos():
    planilha = pd.read_excel('C:\whatsponto\contatos.xlsx')
    contatos = str(planilha)
    contatos = contatos.split('\n')
    del contatos[0]
    listados = len(contatos)
    list_contatos = []
    lista_erros = ''
    for word in contatos:     
        if len(word.split()) == 4:
            list_contatos += [word.split()]
        else:
            lista_erros += 'Erro com ' + word + '\n'

    if lista_erros == '':
        lista_erros += '0'

    return(list_contatos,listados,lista_erros)

       
       
(contatos,listados, erro) = load_contatos()


