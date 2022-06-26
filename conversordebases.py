import PySimpleGUI as pg
import pyperclip as clip
from con_bases import *

def convert(nbr = "", base_a = 0, base_b = 0):
    value = todec(nbr, base_a)
    print(value)
    if base_b == 2:
        new_value = tobin(int(value))
        print(new_value )
        return (new_value)
    elif base_b == 8:
        new_value = tooct(int(value))
        print(new_value )
        return (new_value)
    elif base_b == 16:
        new_value = tohex(int(value))
        print(new_value )
        return (new_value)

#layout
pg.theme('Reddit')

inputsize = (10,1)
bases = ['Decimal', 'Binary', 'Octal', 'Hexadecimal']

col01 = [
    [pg.Combo([bases[0], bases[1], bases[2], bases[3]], bases[0], key = 'selbase', readonly=True, auto_size_text = True), pg.Input(key='nbr', size = inputsize)],
    [pg.Button('convert', size = (15, 1))]
]
cl01 = [
    [pg.Text(key = 'text_result01', text = bases[1], background_color='#0079d3', text_color = '#fff', size = (12, 0), justification='center')],
    [pg.Text(key = 'text_result02', text = bases[2], background_color='#0079d3', text_color = '#fff', size = (12, 0), justification='center')],
    [pg.Text(key = 'text_result03', text = bases[3], background_color='#0079d3', text_color = '#fff', size = (12, 0), justification='center')]
]
cl02 = [
    [pg.Input(key='b01', size = inputsize, readonly=True)],
    [pg.Input(key='b02', size = inputsize, readonly=True)],
    [pg.Input(key='b03', size = inputsize, readonly=True)]
]
col02 = [
    [pg.Column(cl01, element_justification='r'), pg.Column(cl02, element_justification='l')]
]
layout = [
    [pg.Column(col01, element_justification='c'), pg.Column(col02)]
]
#window
win = pg.Window('Number Converter', layout)

#events
while True:
    event, value = win.read()

    if event == pg.WINDOW_CLOSED:
        break

    if event == 'convert':
        if value['nbr'] == '':    #checking null entry
            for i in range(3):
                win[f'b0{i+1}'].update('Null')

        elif value['selbase'] == bases[0]:
            win['text_result01'].update(bases[1])
            win['text_result02'].update(bases[2])
            win['text_result03'].update(bases[3])
            win['b01'].update(tobin(int(value['nbr'])))    # Binary
            win['b02'].update(tooct(int(value['nbr'])))    # Octal
            win['b03'].update(tohex(int(value['nbr'])))    # Hexadecimal
        elif value['selbase'] == bases[1]:
            win['text_result01'].update(bases[0])
            win['text_result02'].update(bases[2])
            win['text_result03'].update(bases[3])
            win['b01'].update(todec(value['nbr'], 2))    # Decimal
            win['b02'].update(convert(value['nbr'], 2, 8)) # Octal
            win['b03'].update(convert(value['nbr'], 2, 16)) # Hexadecimal
        elif value['selbase'] == bases[2]:
            win['text_result01'].update(bases[0])
            win['text_result02'].update(bases[1])
            win['text_result03'].update(bases[3])
            win['b01'].update(todec(value['nbr'], 8))    # Decimal
            win['b02'].update(convert(value['nbr'], 8, 2))    # Binary
            win['b03'].update(convert(value['nbr'], 8, 16))    # Hexadecimal
        elif value['selbase'] == bases[3]:
            win['text_result01'].update(bases[0])
            win['text_result02'].update(bases[1])
            win['text_result03'].update(bases[2])
            win['b01'].update(todec(value['nbr'], 16))    # Decimal
            win['b02'].update(convert(value['nbr'], 16, 2))    # Binary
            win['b03'].update(convert(value['nbr'], 16, 8))    # Octal

    if event == 'copy01':
        clip.copy(value['b01'])
    if event == 'copy02':
        clip.copy(value['b02'])
    if event == 'copy03':
        clip.copy(value['b03'])

win.close()
