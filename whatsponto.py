#from selenium import webdriver
#import tkinter
#import time
import pandas as pd


planilha = pd.read_excel('C:\whatsponto\contatos.xlsx')
contatos = str(planilha)
contatos = contatos.split('\n')
print(contatos)
del contatos[0]
list_contatos = []
for word in contatos:
    list_contatos += [word.split()]

