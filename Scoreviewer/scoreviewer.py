import pandas as pd
import PySimpleGUI as sg
import time 
import backend as bd

path = 'OUT-JSONInterface.log'

## Setting initialisation values
event_name = 'Damen Vogelschießen 2023'
comp1 = 'Königinnen Orden'
comp2 = 'Damen Jubiläums Orden'
comp3 = 'Damen Vogelteil'
comp4 = 'KK Auflage'
comp5 = 'Bundesorden'
comp6 = 'Haspa-Orden'
comp7 = 'Zapf-Orden'
comp8 = 'Vogelteil'
comp9 = 'LG Auflage'
comp10 = 'Halsband Orden'
comp11 = 'Ehrenpreis'
comp12 = 'Mafia Pokal'

#Creating the Dataframes
placeholder_df = pd.DataFrame({'Platz': [1,2,3,4,5,6,7,8,9,10],
                               'Name': ['Alisa Aachen','Berndt Berlin','Christiane Crailsheim','Dieter Dingolfing','Erika Erfurt','Ferdinand Frankfurt','Gerlinde Göttingen','Harald Hamburg','Inga Ingolstadt','Jannik Jork'],
                               'Score': [100,95,85,80,70,65,60,55,50,49]
                               })

placeholder_df2 = pd.DataFrame({'Platz': [1,2,3,4,5,6,7,8,9,10],
                               'Name': ['Zacharias Zeppelin','Yvonne Ypern','Xander Xanten','Wilma Würzburg','Viktor Venlo','Ferdinand Frankfurt','Gerlinde Göttingen','Harald Hamburg','Inga Ingolstadt','Jannik Jork'],
                               'Punkte': [100,95,85,80,70,65,60,55,50,49]
                               })

df1 = placeholder_df 
df2 = placeholder_df
df3 = placeholder_df
df4 = placeholder_df
df5 = placeholder_df
df6 = placeholder_df
df7 = placeholder_df2 
df8 = placeholder_df2
df9 = placeholder_df2
df10 = placeholder_df2
df11 = placeholder_df2
df12 = placeholder_df2

## Setting the layout
layout = [
    [sg.Text('Willkommen zum '+ event_name, font='Calibri 28', expand_x=True, justification='center', pad=((10,10),(10,30)))],
    [sg.Button('Seite 1',key='-SEITE 1-',pad=((10,10),(10,30))),sg.Button('Seite 2',key='-SEITE 2-',pad=((10,10),(10,30)))],
    [sg.Text(comp1,key='-COMP 1 TEXT-', font='Calibri 20', expand_x=True, justification='center'),sg.Text(comp2,key='-COMP 2 TEXT-', font='Calibri 20', expand_x=True, justification='center'),sg.Text(comp3,key='-COMP 3 TEXT-', font='Calibri 20', expand_x=True, justification='center')],
    [sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=10,
                     key= '-TABLE 1-',
                     font='Calibri 12',
                     pad=((20,25),(10,30))),
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=10,
                     key= '-TABLE 2-' ,
                     font='Calibri 12',
                     pad=((25,25),(10,30))),
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=10,
                     key= '-TABLE 3-' ,
                     font='Calibri 12',
                     pad=((25,20),(10,30)))],
    [sg.Text(comp4,key='-COMP 4 TEXT-', font='Calibri 20', expand_x=True, justification='center'),sg.Text(comp5,key='-COMP 5 TEXT-', font='Calibri 20', expand_x=True, justification='center'),sg.Text(comp6,key='-COMP 6 TEXT-', font='Calibri 20', expand_x=True, justification='center')],
    [sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=10,
                     key= '-TABLE 4-' ,
                     font='Calibri 12',
                     pad=((20,25),(10,30))),
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=10,
                     key= '-TABLE 5-' ,
                     font='Calibri 12',
                     pad=((25,25),(10,30))),
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=10,
                     key= '-TABLE 6-' ,
                     font='Calibri 12',
                     pad=((25,20),(10,30)))],
    [sg.Text('Letzte Aktualisierung:'),sg.Text('--:--', key='-TIME-'),sg.Text('Nächste Aktualisierung (dauert ca. 1min)->'),sg.Button('Jetzt', key='-REFRESH-'),sg.Push(),sg.Button('Exit',key='-EXIT-')]
]
# TODO : Set Theme

window = sg.Window('Scoreviewer Beta',layout)

page = 1

## Event Loop
while True:
    event, values = window.read()

    if event in ('-EXIT-',sg.WIN_CLOSED):
        break

    if event == '-REFRESH-':
        window['-COMP 1 TEXT-'].update('Update läuft')
        window['-COMP 2 TEXT-'].update('Update läuft')
        window['-COMP 3 TEXT-'].update('Update läuft')
        window['-COMP 4 TEXT-'].update('Update läuft')
        window['-COMP 5 TEXT-'].update('Update läuft')
        window['-COMP 6 TEXT-'].update('Update läuft')
        window['-TIME-'].update('in progress')
        window.refresh()
        data = bd.read_logfile(path)
        df1 = bd.Vorgabe(data,'KKA KK-DamenKniginnen Orden KKA','KKA',1999.0)
        df2 = bd.Vorgabe(data,'KKA KK-Damen Jubi Orden KKA','KKA',2023.0)
        df3 =  bd.Best_Shot(data,'KKA Damen Vogelteil KKA','KKA')
        df5 = bd.Best_Shot(data,'KKA KK-Bundesorden KKA','KKA')
        df6 = bd.Vorgabe(data,'KKA Damen Vogelteil KKA','KKA',380.0)
        if page == 1:
            window['-COMP 1 TEXT-'].update(comp1)
            window['-TABLE 1-'].update(values=df1.values.tolist())
            window['-COMP 2 TEXT-'].update(comp2)
            window['-TABLE 2-'].update(values=df2.values.tolist())
            window['-COMP 3 TEXT-'].update(comp3)
            window['-TABLE 3-'].update(values=df3.values.tolist())
            window['-COMP 4 TEXT-'].update(comp4)
            window['-COMP 5 TEXT-'].update(comp5)
            window['-TABLE 5-'].update(values=df5.values.tolist())
            window['-COMP 6 TEXT-'].update(comp6)
            window['-TABLE 6-'].update(values=df6.values.tolist())
        else:
            window['-COMP 1 TEXT-'].update(comp7)
            window['-COMP 2 TEXT-'].update(comp8)
            window['-COMP 3 TEXT-'].update(comp9)
            window['-COMP 4 TEXT-'].update(comp10)
            window['-COMP 5 TEXT-'].update(comp11)
            window['-COMP 6 TEXT-'].update(comp12)
        zeit = time.gmtime()
        window['-TIME-'].update(str((zeit.tm_hour+2)) +':'+str(zeit.tm_min))
        window.refresh()

    if event == '-SEITE 2-' and page == 1:
        window['-COMP 1 TEXT-'].update(comp7)
        window['-TABLE 1-'].update(values= placeholder_df2.values.tolist())
        window['-COMP 2 TEXT-'].update(comp8)
        window['-TABLE 2-'].update(values= placeholder_df2.values.tolist())
        window['-COMP 3 TEXT-'].update(comp9)
        window['-TABLE 3-'].update(values= placeholder_df2.values.tolist())
        window['-COMP 4 TEXT-'].update(comp10)
        window['-TABLE 4-'].update(values= placeholder_df2.values.tolist())
        window['-COMP 5 TEXT-'].update(comp11)
        window['-TABLE 5-'].update(values= placeholder_df2.values.tolist())
        window['-COMP 6 TEXT-'].update(comp12)
        window['-TABLE 6-'].update(values= placeholder_df2.values.tolist())
        window.refresh()
        page = 2

    if event == '-SEITE 1-' and page == 2:
        window['-COMP 1 TEXT-'].update(comp1)
        window['-TABLE 1-'].update(values=df1.values.tolist())
        window['-COMP 2 TEXT-'].update(comp2)
        window['-TABLE 2-'].update(values=df2.values.tolist())
        window['-COMP 3 TEXT-'].update(comp3)
        window['-TABLE 3-'].update(values=df3.values.tolist())
        window['-COMP 4 TEXT-'].update(comp4)
        window['-COMP 5 TEXT-'].update(comp5)
        window['-TABLE 5-'].update(values=df5.values.tolist())
        window['-COMP 6 TEXT-'].update(comp6)
        window['-TABLE 6-'].update(values=df6.values.tolist())
        window.refresh()
        page = 1

## END
window.close()