import pandas as pd
import PySimpleGUI as sg
import time 
import backend as bd
import datetime as dt

path = 'OUT-JSONInterface.log' ##offline
#path = '//DESKTOP-6RH80LH/Jsonlive/OUT-JSONInterface.log' ##online

###################################
## Setting initialisation values ##
###################################

event_name = 'Schützenfest 2023'
now = dt.datetime.now()
nowstring = now.strftime("%H:%M")
updatetime = 5 #in minutes
updateMiliSec = 3000
update= now + dt.timedelta(minutes=1)
updatestring = update.strftime("%H:%M")

## Seite 1
comp1 = 'Ehrenscheibe'
comp2 = 'Ehrenpreisscheibe'
comp3 = 'KK-Auflage'
comp4 = 'Zapfenstreichausmarschorden'
comp5 = 'Dieter Reincke - Orden'
comp6 = 'Bundesorden'
comp7 = 'LG-Auflage'
comp8 = 'Mafia-Pokal'
## Seite 2
comp9 = 'Bestmann Schützen'
comp10 = 'Bestmann Oldies'
comp11 = 'Bestmann Frauen'
comp12 = 'Bestmann Spielmannszug'
comp13 = 'Haspa-Orden D/H'
comp14 = 'Damen Jubiläums Orden'
comp15 = 'Königinnen Orden'
comp16 = 'Vogelteil Herren'
## Seite 3
comp17= 'Vogelteil Damen'
comp18 = 'Vogelteil Jugend'
comp19 = 'LG-Auflage Jugend'
comp20 = 'LG-Freihand Jugend'
comp21 = 'Ehrenscheibe'
comp22 = 'Celebration-Pokal'
comp23 = 'Jugend-Standarte-Pokal'
comp24 = 'Jugend Ausmarsch-Orden'
## Seite 4
comp25 = 'Krystian-Dechsheimer-Orden'
comp26 = 'Licht-Glücksziel'
comp27 = 'Licht-Auflage'
comp28 = 'Bianca-Dechsheimer-Nadel'
comp29 = 'Haspa-Orden Lichtpunkt'
comp30 = 'Haspa-Orden Luftgewehr'
comp31 = 'Beste(r) Jungschütze/-in'
comp32 = 'Bester(r) Lichtpunktschütze/-in'

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
df13 = placeholder_df
df14 = placeholder_df
df15 = placeholder_df
df16 = placeholder_df
df17 = placeholder_df
df18 = placeholder_df
df19 = placeholder_df
df20 = placeholder_df
df21 = placeholder_df
df22 = placeholder_df
df23 = placeholder_df
df24 = placeholder_df
df25 = placeholder_df
df26 = placeholder_df
df27 = placeholder_df
df28 = placeholder_df
df29 = placeholder_df
df30 = placeholder_df
df31 = placeholder_df
df32 = placeholder_df

########################
## Setting the layout ##
########################
layout = [
    [sg.Text('Willkommen zum '+ event_name, font='Calibri 28', expand_x=True, justification='center', pad=((10,10),(10,30)))],
    [sg.Button('Seite 1',key='-SEITE 1-',pad=((10,10),(10,30)), font='Calibri 16')
     ,sg.Button('Seite 2',key='-SEITE 2-',pad=((10,10),(10,30)), font='Calibri 16')
     ,sg.Button('Seite 3',key='-SEITE 3-',pad=((10,10),(10,30)), font='Calibri 16')
     ,sg.Button('Seite 4',key='-SEITE 4-',pad=((10,10),(10,30)), font='Calibri 16')],
    [sg.Text(comp1,key='-COMP 1 TEXT-', size=(25, 1), font='Calibri 20', expand_x=True, justification='center')
     ,sg.Text(comp2,key='-COMP 2 TEXT-',size=(25, 1), font='Calibri 20', expand_x=True, justification='center')
     ,sg.Text(comp3,key='-COMP 3 TEXT-', size=(25, 1), font='Calibri 20', expand_x=True, justification='center')
     ,sg.Text(comp4,key='-COMP 4 TEXT-', size=(25, 1), font='Calibri 20', expand_x=True, justification='center')],
    [sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=15,
                     key= '-TABLE 1-',
                     font='Calibri 12',
                     pad=((20,25),(10,30))),
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=15,
                     key= '-TABLE 2-' ,
                     font='Calibri 12',
                     pad=((25,25),(10,30))),
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=15,
                     key= '-TABLE 3-' ,
                     font='Calibri 12',
                     pad=((25,25),(10,30))),
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=15,
                     key= '-TABLE 4-' ,
                     font='Calibri 12',
                     pad=((25,20),(10,30)))],
    [sg.Text(comp5,key='-COMP 5 TEXT-', size=(25, 1), font='Calibri 20', expand_x=True, justification='center')
     ,sg.Text(comp6,key='-COMP 6 TEXT-', size=(25, 1), font='Calibri 20', expand_x=True, justification='center')
     ,sg.Text(comp7,key='-COMP 7 TEXT-', size=(25, 1), font='Calibri 20', expand_x=True, justification='center')
     ,sg.Text(comp8,key='-COMP 8 TEXT-', size=(25, 1), font='Calibri 20', expand_x=True, justification='center')],
    [sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=15,
                     key= '-TABLE 5-' ,
                     font='Calibri 12',
                     pad=((20,25),(10,30))),
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=15,
                     key= '-TABLE 6-' ,
                     font='Calibri 12',
                     pad=((25,25),(10,30))),
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=15,
                     key= '-TABLE 7-' ,
                     font='Calibri 12',
                     pad=((25,25),(10,30))),                 
    sg.Table(values=placeholder_df.values.tolist(),
                     headings=placeholder_df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=15,
                     key= '-TABLE 8-' ,
                     font='Calibri 12',
                     pad=((25,20),(10,30)))],
    [sg.Text('Letzte Aktualisierung: ',size=(16,1)),sg.Text('--:--', key='-TIME-',size=(10,1)),sg.Text('Nächste Aktualisierung um: ',size=(20,1)),sg.Text('--:--', key='-TIME 2-'),sg.Button('Jetzt', key='-REFRESH-', disabled=True,visible=False),sg.Push(),sg.Button('Exit',key='-EXIT-', font='Calibri 16')]
]
# TODO : Set Theme

window = sg.Window('Scoreviewer Beta',layout,no_titlebar=False)

page = 1

################
## Event Loop ##
################
while True:
    event, values = window.read(timeout=updateMiliSec)

    if event in ('-EXIT-',sg.WIN_CLOSED):
        break

    if event == '-REFRESH-' or (sg.TIMEOUT_KEY and event not in ('-EXIT-',sg.WIN_CLOSED,'-SEITE 1-','-SEITE 2-','-SEITE 3-','-SEITE 4-')):
        ## informing the user
        window['-COMP 1 TEXT-'].update('Update läuft')
        window['-COMP 2 TEXT-'].update('Update läuft')
        window['-COMP 3 TEXT-'].update('Update läuft')
        window['-COMP 4 TEXT-'].update('Update läuft')
        window['-COMP 5 TEXT-'].update('Update läuft')
        window['-COMP 6 TEXT-'].update('Update läuft')
        window['-COMP 7 TEXT-'].update('Update läuft')
        window['-COMP 8 TEXT-'].update('Update läuft')
        window['-TIME-'].update('in progress')
        window['-SEITE 1-'].update(disabled=True)
        window['-SEITE 2-'].update(disabled=True)
        window['-SEITE 3-'].update(disabled=True)
        window['-SEITE 4-'].update(disabled=True)
        window['-EXIT-'].update(disabled=True)
        window.refresh()

        data = bd.read_logfile(path)

        df1 = bd.Ehrenscheibe(data,'KKA KK-Ehrenpreisscheibe KKA','KKA Vogelteil KKA') #Ehrenscheibe beste 10 Männer
        df2 = bd.Best_Tens(data,'KKA KK-Ehrenpreisscheibe KKA','KKA',2) #TODO beste Serie
        df3 = bd.Best_Tens(data,'KKA KK Auflage KKA','KKA',2) # KK-Auflage beste 2 10en
        df4 = bd.best_Ten_Series(data,'KKA KK-Zapf Orden KKA') 
        df5 = bd.Vorgabe(data,'KKA KK-Halsbandorden Dieter KKA','KKA',509.0) # Vorgabe
        df6 = bd.Best_Tens(data,'KKA KK-Bundesorden KKA','KKA',1) # Beste 10
        df7 = bd.Best_Shots(data,'LGA LG Auflage LGA','LGA',3) # Beste 3 Schüsse
        df8 = bd.Vorgabe(data,'LGA Mafia Pokal LGA','LGA',777.0) # Vorgabe
        df9 = bd.bestmann(data,['KKA KK-Ehrenpreisscheibe KKA','KKA KK Auflage KKA','KKA KK-Zapf Orden KKA','LGA LG Auflage LGA'],'KKA Vogelteil KKA',min_age=0,max_age=50) #TODO Bestmann normal 50 Jahre und Jünger
        df10 = bd.bestmann(data,['KKA KK-Ehrenpreisscheibe KKA','KKA KK Auflage KKA','KKA KK-Zapf Orden KKA','LGA LG Auflage LGA'],'KKA Vogelteil KKA',min_age=51,max_age=120) #TODO Bestmann oldies 51 Jahre und älter 
        df11 = bd.bestmann(data,['KKA KK Auflage KKA','KKA KK-Zapf Orden KKA','LGA LG Auflage LGA'],'KKA Damen Vogelteil KKA') #TODO Bestmann Damen
        df12 = bd.best_Rings(data,'LGA LG-Bestmann Spielmannszug LGA','LGA',5) 
        df13 = bd.Vorgabe(data,'KKA Haspa D/H KKA','KKA',380.0)
        df14 = bd.Vorgabe(data,'KKA KK-Damen Jubi Orden KKA','KKA',2023.0)
        df15 = bd.Vorgabe(data,'KKA KK-DamenKniginnen Orden KKA','KKA',1999.0)
        df16 = bd.Best_Shot(data,'KKA Vogelteil KKA','KKA')
        df17 = bd.Best_Shot(data,'KKA Damen Vogelteil KKA','KKA')
        df18 = bd.Best_Shot(data,'LGA Jugend Vogelteil LGA','LGA') # Vogelteil Jugend Bester Schuss
        df19 = bd.best_Rings(data,'LGA Jugend LG Auflage LGA','LGA',10)  # Jugend LG-Auflage Beste 10 Schuss nach Ringen
        df20 = bd.best_Rings(data,'LG Jugend LG Freihand LG','LG',10) # Jugend LG-Freihand Beste 10en nach Ringen
        df21 = bd.Best_Shot(data,'LGA Jugend Ehrenscheibe LGA','LGA') # Jugend Ehrenscheibe Bester Schuss 'LGA Jugend Ehrenscheibe LGA'
        df22 = bd.Vorgabe(data,'LG Jugend Celebrations - Pokal LG','LG',324.0) # Celebration-Pokal Vorgabe 324,0 'LG Jugend Celebrations - Pokal LG'
        df23 = bd.Best_Shots(data,'LGA Jugend Standarte Pokal LGA','LGA',2) # Jugend-Standarte-Pokal Beste 2 Schüsse
        df24 = bd.Best_Shots(data,'LGA Jugend Zapf LGA','LGA',2) # Zapf-/Ausmarsch-Orden Beste 2 Schüsse 'LGA Jugend Zapf LGA'
        df25 = placeholder_df # Krystian-Dechsheimer-Orden Vorgabe 1995 Lichtpistole
        df26 = placeholder_df # Licht-Glücksziel Vorgabe ???
        df27 = placeholder_df # Licht-Auflage Beste Schüsse? Ringe?
        df28 = placeholder_df # Bianca-Dechsheimer-Nadel Teiler über mehrere Schüsse unbekannter Teiler
        df29 = bd.Vorgabe(data,'LGA Haspa Licht LGA','LGA',380.0) # Haspa Lichtpunkt  
        df30 = bd.Vorgabe(data,'LGA Haspa LG Jugend LGA','LGA',380.0)  # Haspa Luftgewehr 'LGA Haspa LG Jugend LGA'
        df31 = placeholder_df # Bestmann Jugend
        df32 = placeholder_df # Bestmann Licht

        if page == 1:
            window['-COMP 1 TEXT-'].update(comp1)
            window['-TABLE 1-'].update(values=df1.values.tolist())
            window['-COMP 2 TEXT-'].update(comp2)
            window['-TABLE 2-'].update(values=df2.values.tolist())
            window['-COMP 3 TEXT-'].update(comp3)
            window['-TABLE 3-'].update(values=df3.values.tolist())
            window['-COMP 4 TEXT-'].update(comp4)
            window['-TABLE 4-'].update(values=df4.values.tolist())
            window['-COMP 5 TEXT-'].update(comp5)
            window['-TABLE 5-'].update(values=df5.values.tolist())
            window['-COMP 6 TEXT-'].update(comp6)
            window['-TABLE 6-'].update(values=df6.values.tolist())
            window['-COMP 7 TEXT-'].update(comp7)
            window['-TABLE 7-'].update(values=df7.values.tolist())
            window['-COMP 8 TEXT-'].update(comp8)
            window['-TABLE 8-'].update(values=df8.values.tolist())
            window['-SEITE 2-'].update(disabled=False)
            window['-SEITE 3-'].update(disabled=False)
            window['-SEITE 4-'].update(disabled=False)
        elif page == 2:
            window['-COMP 1 TEXT-'].update(comp9)
            window['-TABLE 1-'].update(values=df9.values.tolist())
            window['-COMP 2 TEXT-'].update(comp10)
            window['-TABLE 2-'].update(values=df10.values.tolist())
            window['-COMP 3 TEXT-'].update(comp11)
            window['-TABLE 3-'].update(values=df11.values.tolist())
            window['-COMP 4 TEXT-'].update(comp12)
            window['-TABLE 4-'].update(values=df12.values.tolist())
            window['-COMP 5 TEXT-'].update(comp13)
            window['-TABLE 5-'].update(values=df13.values.tolist())
            window['-COMP 6 TEXT-'].update(comp14)
            window['-TABLE 6-'].update(values=df14.values.tolist())
            window['-COMP 7 TEXT-'].update(comp15)
            window['-TABLE 7-'].update(values=df15.values.tolist())
            window['-COMP 8 TEXT-'].update(comp16)
            window['-TABLE 8-'].update(values=df16.values.tolist())
            window['-SEITE 1-'].update(disabled=False)
            window['-SEITE 3-'].update(disabled=False)
            window['-SEITE 4-'].update(disabled=False)
        elif page == 3:
            window['-COMP 1 TEXT-'].update(comp17)
            window['-TABLE 1-'].update(values=df17.values.tolist())
            window['-COMP 2 TEXT-'].update(comp18)
            window['-TABLE 2-'].update(values=df18.values.tolist())
            window['-COMP 3 TEXT-'].update(comp19)
            window['-TABLE 3-'].update(values=df19.values.tolist())
            window['-COMP 4 TEXT-'].update(comp20)
            window['-TABLE 4-'].update(values=df20.values.tolist())
            window['-COMP 5 TEXT-'].update(comp21)
            window['-TABLE 5-'].update(values=df21.values.tolist())
            window['-COMP 6 TEXT-'].update(comp22)
            window['-TABLE 6-'].update(values=df22.values.tolist())
            window['-COMP 7 TEXT-'].update(comp23)
            window['-TABLE 7-'].update(values=df23.values.tolist())
            window['-COMP 8 TEXT-'].update(comp24)
            window['-TABLE 8-'].update(values=df24.values.tolist())
            window['-SEITE 1-'].update(disabled=False)
            window['-SEITE 2-'].update(disabled=False)
            window['-SEITE 4-'].update(disabled=False)
        else :
            window['-COMP 1 TEXT-'].update(comp25)
            window['-TABLE 1-'].update(values= df25.values.tolist())
            window['-COMP 2 TEXT-'].update(comp26)
            window['-TABLE 2-'].update(values= df26.values.tolist())
            window['-COMP 3 TEXT-'].update(comp27)
            window['-TABLE 3-'].update(values= df27.values.tolist())
            window['-COMP 4 TEXT-'].update(comp28)
            window['-TABLE 4-'].update(values= df28.values.tolist())
            window['-COMP 5 TEXT-'].update(comp29)
            window['-TABLE 5-'].update(values= df29.values.tolist())
            window['-COMP 6 TEXT-'].update(comp30)
            window['-TABLE 6-'].update(values= df30.values.tolist())
            window['-COMP 7 TEXT-'].update(comp31)
            window['-TABLE 7-'].update(values=df31.values.tolist())
            window['-COMP 8 TEXT-'].update(comp32)
            window['-TABLE 8-'].update(values=df32.values.tolist())
            window['-SEITE 1-'].update(disabled=False)
            window['-SEITE 2-'].update(disabled=False)
            window['-SEITE 3-'].update(disabled=False)

        now = dt.datetime.now()
        nowstring = now.strftime("%H:%M")
        window['-TIME-'].update(nowstring)
        update= dt.datetime.now() + dt.timedelta(minutes=5)
        updatestring = update.strftime("%H:%M")
        window['-TIME 2-'].update(updatestring)
        print(updatestring)
        updateMiliSec = 300000
        window['-EXIT-'].update(disabled=False)
        window.refresh()

    if event == '-SEITE 1-' and page != 1:
        window['-COMP 1 TEXT-'].update(comp1)
        window['-TABLE 1-'].update(values=df1.values.tolist())
        window['-COMP 2 TEXT-'].update(comp2)
        window['-TABLE 2-'].update(values=df2.values.tolist())
        window['-COMP 3 TEXT-'].update(comp3)
        window['-TABLE 3-'].update(values=df3.values.tolist())
        window['-COMP 4 TEXT-'].update(comp4)
        window['-TABLE 4-'].update(values=df4.values.tolist())
        window['-COMP 5 TEXT-'].update(comp5)
        window['-TABLE 5-'].update(values=df5.values.tolist())
        window['-COMP 6 TEXT-'].update(comp6)
        window['-TABLE 6-'].update(values=df6.values.tolist())
        window['-COMP 7 TEXT-'].update(comp7)
        window['-TABLE 7-'].update(values=df7.values.tolist())
        window['-COMP 8 TEXT-'].update(comp8)
        window['-TABLE 8-'].update(values=df8.values.tolist())
        window['-SEITE 1-'].update(disabled=True)
        window['-SEITE 2-'].update(disabled=False)
        window['-SEITE 3-'].update(disabled=False)
        window['-SEITE 4-'].update(disabled=False)
        window.refresh()
        page = 1

    if event == '-SEITE 2-' and page != 2:
        window['-COMP 1 TEXT-'].update(comp9)
        window['-TABLE 1-'].update(values=df9.values.tolist())
        window['-COMP 2 TEXT-'].update(comp10)
        window['-TABLE 2-'].update(values=df10.values.tolist())
        window['-COMP 3 TEXT-'].update(comp11)
        window['-TABLE 3-'].update(values=df11.values.tolist())
        window['-COMP 4 TEXT-'].update(comp12)
        window['-TABLE 4-'].update(values=df12.values.tolist())
        window['-COMP 5 TEXT-'].update(comp13)
        window['-TABLE 5-'].update(values=df13.values.tolist())
        window['-COMP 6 TEXT-'].update(comp14)
        window['-TABLE 6-'].update(values=df14.values.tolist())
        window['-COMP 7 TEXT-'].update(comp15)
        window['-TABLE 7-'].update(values=df15.values.tolist())
        window['-COMP 8 TEXT-'].update(comp16)
        window['-TABLE 8-'].update(values=df16.values.tolist())
        window['-SEITE 1-'].update(disabled=False)
        window['-SEITE 2-'].update(disabled=True)
        window['-SEITE 3-'].update(disabled=False)
        window['-SEITE 4-'].update(disabled=False)
        window.refresh()
        page = 2

    if event == '-SEITE 3-' and page != 3:
        window['-COMP 1 TEXT-'].update(comp17)
        window['-TABLE 1-'].update(values=df17.values.tolist())
        window['-COMP 2 TEXT-'].update(comp18)
        window['-TABLE 2-'].update(values=df18.values.tolist())
        window['-COMP 3 TEXT-'].update(comp19)
        window['-TABLE 3-'].update(values=df19.values.tolist())
        window['-COMP 4 TEXT-'].update(comp20)
        window['-TABLE 4-'].update(values=df20.values.tolist())
        window['-COMP 5 TEXT-'].update(comp21)
        window['-TABLE 5-'].update(values=df21.values.tolist())
        window['-COMP 6 TEXT-'].update(comp22)
        window['-TABLE 6-'].update(values=df22.values.tolist())
        window['-COMP 7 TEXT-'].update(comp23)
        window['-TABLE 7-'].update(values=df23.values.tolist())
        window['-COMP 8 TEXT-'].update(comp24)
        window['-TABLE 8-'].update(values=df24.values.tolist())
        window['-SEITE 1-'].update(disabled=False)
        window['-SEITE 2-'].update(disabled=False)
        window['-SEITE 3-'].update(disabled=True)
        window['-SEITE 4-'].update(disabled=False)
        window.refresh()
        page = 3

    if event == '-SEITE 4-' and page != 4:
        window['-COMP 1 TEXT-'].update(comp25)
        window['-TABLE 1-'].update(values= df25.values.tolist())
        window['-COMP 2 TEXT-'].update(comp26)
        window['-TABLE 2-'].update(values= df26.values.tolist())
        window['-COMP 3 TEXT-'].update(comp27)
        window['-TABLE 3-'].update(values= df27.values.tolist())
        window['-COMP 4 TEXT-'].update(comp28)
        window['-TABLE 4-'].update(values= df28.values.tolist())
        window['-COMP 5 TEXT-'].update(comp29)
        window['-TABLE 5-'].update(values= df29.values.tolist())
        window['-COMP 6 TEXT-'].update(comp30)
        window['-TABLE 6-'].update(values= df30.values.tolist())
        window['-COMP 7 TEXT-'].update(comp31)
        window['-TABLE 7-'].update(values=df31.values.tolist())
        window['-COMP 8 TEXT-'].update(comp32)
        window['-TABLE 8-'].update(values=df32.values.tolist())
        window.refresh()
        window['-SEITE 1-'].update(disabled=False)
        window['-SEITE 2-'].update(disabled=False)
        window['-SEITE 3-'].update(disabled=False)
        window['-SEITE 4-'].update(disabled=True)
        page = 4

## END
window.close()