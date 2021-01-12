#from selenium import webdriver
#import tkinter
#import time
import pandas as pd

def gerar_contatos():
    planilha = pd.read_excel('C:\whatsponto\contatos.xlsx')
    contatos = str(planilha)
    contatos = contatos.split('\n')
    del contatos[0]
    listados = len(contatos)
    print(listados)
    list_contatos = []
    count_list = 0
    lista_erros = ''
    for word in contatos:     
        if len(word.split()) == 4:
            list_contatos += [word.split()]
        else:
            lista_erros += 'Erro com ' + word + '\n'

    print(list_contatos) 
    print(lista_erros)       
       
gerar_contatos()

