import pandas as pd
import PySimpleGUI as sg

## Setting initialisation values
event_name = 'Damen Vogelschießen 2023'
comp1 = 'Königinnen Orden'
comp2 = 'Damen Jubiläums Orden'
comp3 = 'Damen Vogelteil'
comp4 = 'KK Auflage'
comp5 = 'Bundesorden'
comp6 = 'Haspa-Orden'

placeholder_df = pd.DataFrame({'Platz': [1,2,3,4,5,6,7,8,9,10],
                               'Name': ['Alisa Aachen','Berndt Berlin','Christiane Crailsheim','Dieter Dingolfing','Erika Erfurt','Ferdinand Frankfurt','Gerlinde Göttingen','Harald Hamburg','Inga Ingolstadt','Jannik Jork'],
                               'Score': [100,95,85,80,70,65,60,55,50,49]
                               })

## Setting the layout
layout = [
    [sg.Text('Willkommen zum '+ event_name, font='Calibri 28', expand_x=True, justification='center', pad=((10,10),(10,30)))],
    [sg.Button('Seite 1',key='-SEITE1',pad=((10,10),(10,30))),sg.Button('Seite 2',key='-SEITE2',pad=((10,10),(10,30)))],
    [sg.Text(comp1,key='-COMP 1 TEXT-', font='Calibri 20', expand_x=True, justification='center'),sg.Text(comp2,key='-COMP 2 TEXT-', font='Calibri 20', expand_x=True, justification='center'),sg.Text(comp3,key='-COMP 3 TEXT-', font='Calibri 20', expand_x=True, justification='center')],
    [sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=max(10, len(placeholder_df)),
                     key= '-TABLE 1-',
                     font='Calibri 12',
                     pad=((20,25),(10,30))),
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=max(10, len(placeholder_df)),
                     key= '-TABLE 2-' ,
                     font='Calibri 12',
                     pad=((25,25),(10,30))),
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=max(10, len(placeholder_df)),
                     key= '-TABLE 3-' ,
                     font='Calibri 12',
                     pad=((25,20),(10,30)))],
    [sg.Text(comp4,key='-COMP 4 TEXT-', font='Calibri 20', expand_x=True, justification='center'),sg.Text(comp5,key='-COMP 5 TEXT-', font='Calibri 20', expand_x=True, justification='center'),sg.Text(comp6,key='-COMP 6 TEXT-', font='Calibri 20', expand_x=True, justification='center')],
    [sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=max(10, len(placeholder_df)),
                     key= '-TABLE 4-' ,
                     font='Calibri 12',
                     pad=((20,25),(10,30))),
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=max(10, len(placeholder_df)),
                     key= '-TABLE 5-' ,
                     font='Calibri 12',
                     pad=((25,25),(10,30))),
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=max(10, len(placeholder_df)),
                     key= '-TABLE 6-' ,
                     font='Calibri 12',
                     pad=((25,20),(10,30)))],
    [sg.Text('Letzte Aktualisierung:'),sg.Text('Nächste Aktualisierung in...'),sg.Push(),sg.Button('Exit',key='-EXIT-')]
]
# TODO : Set Theme

window = sg.Window('Scoreviewer Beta',layout)

## Event Loop
while True:
    event, values = window.read()

    if event in ('-EXIT-',sg.WIN_CLOSED):
        break

window.close()