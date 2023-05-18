import json
import pandas as pd
from operator import index
from posixpath import split
import warnings
warnings.filterwarnings("ignore")

def read_logfile(path):
    shots = pd.DataFrame()
    with open(path, 'r', encoding='utf8', errors='ignore') as log:
        for line in log:
            element = pd.json_normalize(json.loads(line), record_path=['Objects'])
            shots = pd.concat([shots, element], axis=0, ignore_index=True)
    
    shots = shots[shots['IsHot'] == True]

    shots.rename(columns= {'Shooter.Firstname' : 'Vorname',
                           'Shooter.Lastname' : 'Nachname',
                           'Distance' : 'Teiler',
                           'Shooter.Identification' : 'Startnummer',
                           'Shooter.Birthyear' : 'Geburtsjahr',
                           'MenuItem.MenuPointName' : 'Wettbewerb'
    },inplace=True)
    shots['Name'] = shots['Vorname']+ ' ' + shots['Nachname'].str.split(' ', 1).str[1]
    shots = shots[['ShotDateTime','Name','Geburtsjahr','Startnummer','Range','Wettbewerb','Run','Count','FullValue','DecValue','Teiler','DiscType']]
    shots.reset_index(inplace=True, drop=True)
    shots.index += 1
    # Schüsse auf falscher Range herausfiltern
    shots = shots[((shots['Range'] <= 6) & (shots['DiscType'] == 'KKA')) | ((shots['Range'] > 6) & (shots['DiscType'] != 'KKA'))]
    return shots

###################
## bester Schuss ##
###################
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

###################
## beste Schüsse ##
###################
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

#######################
## Vorgabe (1 Schuss ##
#######################
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
    #if name == 'LGA Mafia Pokal LGA' and res.shape[0] >= 3:
    #    res.loc[res['Platz'] <= 3, 'Name'] = '???'

    return res
#################
## Beste Serie ##
#################
def best_Ten_Series(data,wettbewerb):
    comp = data[data['Wettbewerb'] == wettbewerb]
    shooters = comp['Startnummer'].unique()
    if comp.shape[0] == 0:
        return pd.DataFrame(columns=['Platz','Name', 'Teiler'])
    
    res = pd.DataFrame()
    for shooter in shooters:
        df = comp[comp['Startnummer'] == shooter]
        bestRinge = 0
        bestTeiler = 20000
        reihen = len(df) // 2
        df.reset_index(inplace=True, drop=True)
  
        for i in range(0,reihen):
            #print('This '+str(i*2) +'  next: '+str(i*2 +1))
            d1 = df[df.index == (i*2)]
            v1 = int(d1['FullValue'])
            teiler1 = int(d1['Teiler'])
            d2 = df[df.index == (i*2 +1)]
            v2 = int(d2['FullValue'])
            teiler2= int(d2['Teiler'])
            #print('comparing index '+(str(i*2)+' and '+(str(i*2+1))))
            #print(' values: '+str(v1)+' and '+str(v2))
            if v1 >= 10 and v2 >= 10:
                Teiler = teiler1 + teiler2
                if Teiler < bestTeiler:
                    bestTeiler = Teiler
               
            
        if bestTeiler != 20000:
            best = df.loc[df['Teiler'].idxmin()]
            best['Teiler'] = bestTeiler
            res = pd.concat([res, best.to_frame().transpose()], axis=0, ignore_index=True)
    
    res.sort_values(['Teiler'] , ascending=True, inplace=True)
    res.reset_index(inplace=True, drop=True)
    res.index += 1
    res['Platz'] = res.index
    res = res[['Platz','Name', 'Teiler']]        

    return res



###############
## Best Tens ##
###############
def Best_Tens(data, wettbewerb, disc, anzahl):
    comp = data[data['Wettbewerb'] == wettbewerb]
    comp = comp[comp['DiscType'] == disc]
    comp = comp[comp['DecValue'] >= 10.0]
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


##################
## Ehrenscheibe ##
##################
def Ehrenscheibe(data, wettbewerb, pflicht):
    comp = data[data['Wettbewerb'] == pflicht]
    shooters = comp['Startnummer'].unique()
    comp = data[data['Wettbewerb'] == wettbewerb]
    comp = comp[comp['DecValue'] >= 10.0]

    if comp.shape[0] == 0:
        return pd.DataFrame(columns=['Platz', 'Name', 'Ringzahl', 'Teiler' ])

    res = pd.DataFrame()
    for shooter in shooters:
        df = comp[comp['Startnummer'] == shooter]
        if df.shape[0] > 0:
            best = df.loc[df['Teiler'].idxmin()]

            res = pd.concat([res, best.to_frame().transpose()], axis=0, ignore_index=True)

    res = res[['Name', 'Teiler']]
    res.sort_values(['Teiler'] , ascending=True, inplace=True)
    res.reset_index(inplace=True, drop=True)
    res.index += 1
    res['Platz'] = res.index
    res = res[['Platz','Name', 'Teiler']]

    return res

###################
## beste Schüsse ##
###################
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

######################################
## Beste Ringzahl (nach x Schüssen) ##
######################################
def best_Rings(data, wettbewerb, disc, anzahl):
    comp = data[data['Wettbewerb'] == wettbewerb]
    comp = comp[comp['DiscType'] == disc]
    shooters = comp['Startnummer'].unique()

    if comp.shape[0] == 0:
        return pd.DataFrame(columns=['Platz','Name', 'Teiler'])
    
    res = pd.DataFrame()

    for shooter in shooters:
        df = comp[comp['Startnummer'] == shooter]
        #print(df)
        if df.shape[0] >= anzahl:
            best = df.iloc[-1]
            best['DecValue'] = round(df['DecValue'].nlargest(anzahl, keep='all').sum(), 1)
            res = pd.concat([res, best.to_frame().transpose()], axis=0, ignore_index=True)
    
    res = res[['Name','DecValue' ,'Teiler']]

    res.sort_values(['DecValue','Teiler'] , ascending=[False,True], inplace=True)
    res.reset_index(inplace=True, drop=True)
    res.index += 1
    res['Platz'] = res.index
    res = res[['Platz','Name', 'DecValue']]

    return res

##############
## Bestmann ##
##############
def bestmann(data:pd.DataFrame , wettbewerbe: list , pflicht: str, min_age = 0, max_age = 120):
    shooterslist = data[data['Wettbewerb'] == pflicht]
    shooterslist = shooterslist[((shooterslist['Geburtsjahr']-2023)*(-1) >= min_age) & ((shooterslist['Geburtsjahr']-2023)*(-1) <= max_age)]
    shooters = shooterslist['Startnummer'].unique()
    res = pd.DataFrame()
    for shooter in shooters:
        teiler = 0
        s = data[data['Startnummer'] == shooter]
        s.reset_index(inplace=True, drop=True)
        for wettbewerb in wettbewerbe:
            df = s[(s['Wettbewerb'] == wettbewerb)]
            if df.shape[0] == 0:
                teiler = teiler+ 10000
            else:
                best = round(df['Teiler'].nsmallest(1, keep='all').sum(), 1)
                teiler = teiler + best
        teiler = round(teiler,1)
        row = s[s.index == 0]
        row['Teiler'] = teiler

        res = pd.concat([res, row], axis=0, ignore_index=True)
    
    res = res[['Name' ,'Teiler']]

    res.sort_values(['Teiler'] , ascending=[True], inplace=True)
    res.reset_index(inplace=True, drop=True)
    res.index += 1
    res['Platz'] = res.index
    res = res[['Platz','Name', 'Teiler']]   

    return res     
