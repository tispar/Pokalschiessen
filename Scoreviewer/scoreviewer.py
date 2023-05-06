import pandas as pd
import PySimpleGUI as sg

event_name = 'Damen Vogelschießen 2023'
comp1 = '<Wettbewerb 1>'
comp2 = '<Wettbewerb 2>'
comp3 = '<Wettbewerb 3>'
comp4 = '<Wettbewerb 4>'
comp5 = '<Wettbewerb 5>'
comp6 = '<Wettbewerb 6>'

placeholder_df = pd.DataFrame((
    'Platz':[1,2,3,4,5,6,7,8,9,10],
    'Name':['Alisa Aachen', 'Berndt Berlin', 'Christiane Crailsheim','Dieter Dingolfing', 'Erika Erfurt'
            ,'Ferdinand Frankfurt','Gerlinde Göttingen', 'Harald Hamburg', 'Inga Ingolstadt', 'Jannik Jork'],
    'Score':[100,95,85,80,70,65,60,55,50,49]
))

layout = [
    [sg.Text('Willkommen zum '+ event_name, font='Calibri 24')],
    [sg.Button('Seite 1',key='-SEITE1'),sg.Button('Seite 2',key='-SEITE2')],
    [sg.Text(comp1,key='-COMP 1 TEXT-', font='Calibri 20'),sg.Text(comp2,key='-COMP 2 TEXT-', font='Calibri 20'),sg.Text(comp3,key='-COMP 3 TEXT-', font='Calibri 20')],
    [sg.Text(comp4,key='-COMP 4 TEXT-', font='Calibri 20'),sg.Text(comp5,key='-COMP 5 TEXT-', font='Calibri 20'),sg.Text(comp6,key='-COMP 6 TEXT-', font='Calibri 20')],
    [sg.Push(),sg.Button('Exit',key='-EXIT-')]
]

window = sg.Window('Scoreviewer Beta',layout)

while True:
    event, values = window.read()

    if event in ('-EXIT-',sg.WIN_CLOSED):
        break

window.close()