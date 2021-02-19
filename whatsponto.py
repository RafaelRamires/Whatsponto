import time
import pandas as pd
from selenium import webdriver
import pyautogui


def load_contatos():
    planilha = pd.read_excel('C:\whatsponto\contatos.xlsx')
    contatos = str(planilha)
    contatos = contatos.split('\n')
    del contatos[0]
    listados = len(contatos)
    list_contatos = []
    lista_erros = ''
    for word in contatos:     
        if len(word.split()) == 3:
            list_contatos += [word.split()]
        else:
            lista_erros += 'Erro com ' + word + '\n'

    if lista_erros == '':
        lista_erros += '0'

    return(list_contatos,listados,lista_erros)

            
(contatos,listados, erro) = load_contatos()
print(listados)
print(erro)


class whatsponto:
    def __init__(self):
        self.mensagem = "Por favor confira seu ponto"
        self.pessoas = contatos
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
   
    def buscar_enviar(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(10)

        for pessoa in self.pessoas: 
            matricula = pessoa[1]
            nome= pessoa[2]
            try: 
                pessoa = self.driver.find_element_by_xpath(f'//span[@title="{nome}"]')
                time.sleep(2)
                pessoa.click()
            except:
                print('erro com ' + nome )
            else:    
                chat_box = self.driver.find_element_by_class_name('DuUXI')
                chat_box.click()
                chat_box.send_keys(self.mensagem)
                time.sleep(2)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                botao_enviar.click()
                time.sleep(2)
                botao_clip = self.driver.find_element_by_xpath("//span[@data-icon='clip']")
                botao_clip.click()
                time.sleep(2)
                botao_documento = self.driver.find_element_by_xpath("//span[@data-icon='attach-document']")
                botao_documento.click()
                time.sleep(2)
                pyautogui.typewrite(f"C:\Whatsponto\Pontos\{matricula}.pdf")
                pyautogui.press("enter")
                time.sleep(2)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                botao_enviar.click()
                time.sleep(2)
                
           
bot = whatsponto() 
bot.buscar_enviar()       