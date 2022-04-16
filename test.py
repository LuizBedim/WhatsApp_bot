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

