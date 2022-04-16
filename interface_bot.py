from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import PySimpleGUI as sg

def janela():
    sg.theme("Reddit")

    layout_center = [
        [sg.Text('Contato ou grupo', size=(15, 0)), sg.Input(size=(20, 0), key='cont')],
        [sg.Text('Mensagem que deseja enviar', size=(30, 0), justification='center')],
        [sg.Input(size=(30, 3), key='mensa')],
        [sg.Button('Enviar', size=(20, 0))],
        [sg.Button('Sair', size=(20, 0))]
    ]

    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Column(layout_center, element_justification='c'), sg.Push()],
        [sg.VPush()]
    ]

    return sg.Window('Whatsapp bot', layout, finalize=True, size=(300, 200))

janela1 = janela()

while True:
    janelas, eventos, valores = sg.read_all_windows()
    if janelas == janela1 and eventos == 'Sair' or eventos == sg.WINDOW_CLOSED:
        break





driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
time.sleep(30)

contatos = ['ANT']
mensagem = 'apenas teste'

def buscar_contato(contatos):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contatos)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
# copyable-text selectable-text
