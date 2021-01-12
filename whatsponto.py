#from selenium import webdriver
#import tkinter
#import time
import pandas as pd

def gerar_contatos():
    planilha = pd.read_excel('C:\whatsponto\contatos.xlsx')
    contatos = str(planilha)
    contatos = contatos.split('\n')
    listados = len(contatos)
    print(contatos)
    del contatos[0]
    list_contatos = []
    count_list = 0
    for word in contatos:
        list_contatos += [word.split()]
        return(list_contatos, )
