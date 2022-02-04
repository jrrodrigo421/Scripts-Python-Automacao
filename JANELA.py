from PySimpleGUI import PySimpleGUI as sg
import time
import webbrowser

sg.theme('Dark Red2')
layout = [
    [sg.Text('PREPARATION     '), sg.Input(key='PREPARATION')],
    [sg.Text('IMPLEMENTATION'), sg.Input(key='IMPLEMENTATION')],
    [sg.Text('VERIFICATION      '), sg.Input(key='VERIFICATION')],
    [sg.Text('MONITORING        '), sg.Input(key='MONITORING')],
    [sg.Text('COMPLETE          '), sg.Input(key='COMPLETE')],
    [sg.Text('LINK                     '), sg.Input(key='LINK    ')],
    [sg.Checkbox('Salvar Dados?')],
    [sg.Button('ENTRAR')]
]

janela = sg.Window('WFM', layout)


Actual_Time = time.strftime("%I:%M:%S")



while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'ENTRAR':
        
            print('DEU BOA')
