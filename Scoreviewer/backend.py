import json
import pandas as pd
from operator import index
from posixpath import split

def read_logfile(path):
    shots = pd.DataFrame()
    with open(path, 'r', encoding='utf8', errors='ignore') as log:
        for line in log:
            element = pd.json_normalize(json.loads(line), record_path=['Objects'])
            #if len(element.columns) > 32:
            #    element.drop(element.columns[[1,2,3,4,7,8,9,14,15,16,18,19,20,21,22,26,30,32,33]], axis=1, inplace=True)
            shots = pd.concat([shots, element], axis=0, ignore_index=True)
    
    shots = shots[shots['IsHot'] == True]

    shots.rename(columns= {'Shooter.Firstname' : 'Vorname',
                           'Shooter.Lastname' : 'Nachname',
                           'Distance' : 'Teiler',
                           'Shooter.Identification' : 'Startnummer',
                           'MenuItem.MenuPointName' : 'Wettbewerb'
    },inplace=True)
    shots['Name'] = shots['Vorname']+ ' ' + shots['Nachname'].str.split(' ', 1).str[1]
    shots = shots[['ShotDateTime','Name','Startnummer','Range','Wettbewerb','Count','FullValue','DecValue','Teiler','DiscType']]
    shots.reset_index(inplace=True, drop=True)
    shots.index += 1
    return shots

## bester Schuss
def Best_Shot(data, wettbewerb, disc):
    comp = data[data['Wettbewerb'] == wettbewerb]
    comp = comp[comp['DiscType'] == disc]
    shooters = comp['Startnummer'].unique()

    if comp.shape[0] == 0:
        return pd.DataFrame(columns=['Platz', 'Name', 'Ringzahl', 'Teiler' ])

    res = pd.DataFrame()
    for shooter in shooters:
        df = comp[comp['Startnummer'] == shooter]
        best = df.loc[df['Teiler'].idxmin()]

        res = pd.concat([res, best.to_frame().transpose()], axis=0, ignore_index=True)

    res = res[['Name', 'Teiler']]
    res.sort_values(['Teiler'] , ascending=True, inplace=True)
    res.reset_index(inplace=True, drop=True)
    res.index += 1
    res['Platz'] = res.index
    res = res[['Platz','Name', 'Teiler']]

    return res

## beste Schüsse
def Best_Shots(data, wettbewerb, disc, anzahl):
    comp = data[data['Wettbewerb'] == wettbewerb]
    comp = comp[comp['DiscType'] == disc]
    shooters = comp['Startnummer'].unique()

    if comp.shape[0] == 0:
        return pd.DataFrame(columns=['Platz','Name', 'Teiler'])
    
    res = pd.DataFrame()

    for shooter in shooters:
        df = comp[comp['Startnummer'] == shooter]

        if df.shape[0] >= anzahl:
            best = df.loc[df['Teiler'].idxmin()]
            best['Teiler'] = round(df['Teiler'].nsmallest(anzahl, keep='all').sum(), 1)
            res = pd.concat([res, best.to_frame().transpose()], axis=0, ignore_index=True)
        
    res = res[['Name', 'Teiler']]

    res.sort_values(['Teiler'] , ascending=True, inplace=True)
    res.reset_index(inplace=True, drop=True)
    res.index += 1
    res['Platz'] = res.index
    res = res[['Platz','Name', 'Teiler']]

    return res

## Vorgabe
def Vorgabe(data,name,disctype,zielteiler):
    comp = data[data['Wettbewerb'] == name]
    comp = comp[comp['DiscType'] == disctype]
    shooters = comp['Startnummer'].unique()

    if comp.shape[0] == 0:
        return pd.DataFrame(columns=['Position', 'Name', 'Ringzahl', 'Teiler' ])

    res = pd.DataFrame()

    for shooter in shooters:
        df = comp[comp['Startnummer'] == shooter]
        df['Abstand'] = round( abs(df['Teiler'] - zielteiler), 1)
        best = df.loc[df['Abstand'].idxmin()]

        res = pd.concat([res, best.to_frame().transpose()], axis=0, ignore_index=True)

    res = res[['Name', 'Abstand']]
    res.sort_values(['Abstand'] , ascending=True, inplace=True)
    res.reset_index(inplace=True, drop=True)
    res.index += 1
    res['Platz'] = res.index
    res = res[['Platz','Name', 'Abstand']]
    if name == 'LGA Mafia Pokal LGA' and res.shape[0] >= 3:
        res.loc[res['Platz'] <= 3, 'Name'] = '???'

    return res

## Beste Serie
    #TODO

## Ehrenpreise
    # TODO