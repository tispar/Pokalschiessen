import json
import pandas as pd

def read_logfile(path):
    shots = pd.DataFrame()
    with open(path, 'r', encoding='utf8', errors='ignore') as log:
        for line in log:
            element = pd.json_normalize(json.loads(line), record_path=['Objects'])
            if len(element.columns) > 32:
                element.drop(element.columns[[1,2,3,4,7,8,9,14,15,16,18,19,20,21,22,26,30,32,33]], axis=1, inplace=True)
                shots = pd.concat([shots, element], axis=0, ignore_index=True)
    
    return shots[shots['IsHot'] == True]

def read_logfile2(path):
    shots = pd.DataFrame()
    with open(path, 'r', encoding='utf-8', errors='ignore') as log:
        lines = log.readlines()
        for line in reversed(lines):
            element = pd.json_normalize(json.loads(line), record_path=['Objects'])
            if len(element.columns) > 32:
                element.drop(element.columns[[1,2,3,4,7,8,9,14,15,16,18,19,20,21,22,26,30,32,33]], axis=1, inplace=True)
                shots = pd.concat([shots, element], axis=0, ignore_index=True)

    shots.sort_values(['ShotDateTime'], ascending=[True], inplace=True)

    return shots[shots['IsHot'] == True].reset_index(drop=True)




def oldiepokal(data):
    comp = data[data['MenuItem.MenuPointName'] == 'KKA OldiPokal KKA']
    comp = comp[comp['DiscType'] == 'KKA']
    shooters = comp['Shooter.Identification'].unique()
    best = pd.DataFrame()
    oldies = pd.DataFrame()
    u65 = pd.DataFrame()

    if comp.shape[0] == 0:
        return pd.DataFrame(columns=['Position', 'Vorname', 'Nachname', 'Id', 'Scheibenanzahl', 'Teiler' ])

    for shooter in shooters:
        df = comp[comp['Shooter.Identification'] == shooter]
        max = df.loc[df['DecValue'].idxmax()]
        best = pd.concat([best, max.to_frame().transpose()], axis=0, ignore_index=True)

        teiler = df['Distance'].sum() -2022
        max['TotalDistance'] = teiler
        if 2022 - max['Shooter.Birthyear'] > 65:
            oldies = pd.concat([oldies, max.to_frame().transpose()], axis=0, ignore_index=True)
        else:
            u65 = pd.concat([u65, max.to_frame().transpose()], axis=0, ignore_index=True)

    #sorting
    if len(best.index >0):
        best.sort_values(['DecValue', 'Distance'], ascending=[False,True], inplace=True)
    if len(oldies.index >0):
        oldies.sort_values(['TotalDistance'], ascending=True, inplace=True)
    if len(u65.index >0):
        u65.sort_values(['TotalDistance'], ascending=True, inplace=True)

    #resetting indexes
    best.reset_index(inplace=True)
    oldies.reset_index(inplace=True)
    u65.reset_index(inplace=True)

    #formatting for display
    #best: Position, Full Name, id, Full Value , Teiler
    best.drop(best.columns[[0,1,2,3,5,7,8,11,15]], axis=1, inplace=True)
    best = best[['Shooter.Firstname', 'Shooter.Lastname', 'Shooter.Identification', 'FullValue', 'Distance']]
    best.index += 1
    best.rename(columns={'Shooter.Firstname' : 'Vorname', 'Shooter.Lastname' : 'Nachname', 'Shooter.Identification' : 'id' , 'FullValue' : 'Scheiben' , 'Distance' : 'Teiler'  }, inplace=True)

    return best, oldies, u65




def bestmann(data):

    #Herren
    hcomp = data[data['MenuItem.MenuPointName'] == 'Jubilumspokal']
    hcomp = hcomp[hcomp['DiscType'] == 'KKA'] 
    hshooters = hcomp['Shooter.Identification'].unique()

    if hcomp.shape[0] != 0:
        hbest = pd.DataFrame()
        for shooter in hshooters:
            df = hcomp[hcomp['Shooter.Identification'] == shooter]
            max = df.loc[df['DecValue'].idxmax()]
            hbest = pd.concat([hbest, max.to_frame().transpose()], axis=0, ignore_index=True)

        hbest.sort_values(['DecValue', 'Distance'], ascending=[False,True], inplace=True)

        hbest.drop(hbest.columns[[0,1,2,3,5,7,8,11,15]], axis=1, inplace=True)
        hbest = hbest[['Shooter.Firstname', 'Shooter.Lastname', 'Shooter.Identification', 'FullValue', 'Distance']]
        hbest.index += 1
        hbest.rename(columns={'Shooter.Firstname' : 'Vorname', 'Shooter.Lastname' : 'Nachname', 'Shooter.Identification' : 'id' , 'FullValue' : 'Scheiben' , 'Distance' : 'Teiler'  }, inplace=True)
    else:
        hbest = pd.DataFrame(columns=['Position', 'Vorname', 'Nachname', 'Id', 'Scheibenanzahl', 'Teiler' ])

    #Damen
    dcomp = data[data['MenuItem.MenuPointName'] == 'Damenjubilumspokal']
    dcomp = dcomp[dcomp['DiscType'] == 'KKA'] 
    dshooters = dcomp['Shooter.Identification'].unique()

    if dcomp.shape[0] != 0:
        dbest = pd.DataFrame()
        for shooter in hshooters:
            df = dcomp[dcomp['Shooter.Identification'] == shooter]
            max = df.loc[df['DecValue'].idxmax()]
            dbest = pd.concat([dbest, max.to_frame().transpose()], axis=0, ignore_index=True)

        dbest.sort_values(['DecValue', 'Distance'], ascending=[False,True], inplace=True)

        dbest.drop(dbest.columns[[0,1,2,3,5,7,8,11,15]], axis=1, inplace=True)
        dbest = dbest[['Shooter.Firstname', 'Shooter.Lastname', 'Shooter.Identification', 'FullValue', 'Distance']]
        dbest.index += 1
        dbest.rename(columns={'Shooter.Firstname' : 'Vorname', 'Shooter.Lastname' : 'Nachname', 'Shooter.Identification' : 'id' , 'FullValue' : 'Scheiben' , 'Distance' : 'Teiler'  }, inplace=True)
    else:
        dbest = pd.DataFrame(columns=['Position', 'Vorname', 'Nachname', 'Id', 'Scheibenanzahl', 'Teiler' ])

    #Jugend
    jcomp = data[data['MenuItem.MenuPointName'] == 'Jugen Jubilumspokal']
    jcomp = jcomp[jcomp['DiscType'] == 'LGA'] 
    jshooters = jcomp['Shooter.Identification'].unique()

    if jcomp.shape[0] !=0 :
        jbest = pd.DataFrame()
        for shooter in hshooters:
            df = jcomp[jcomp['Shooter.Identification'] == shooter]
            max = df.loc[df['DecValue'].idxmax()]
            jbest = pd.concat([jbest, max.to_frame().transpose()], axis=0, ignore_index=True)

        jbest.sort_values(['DecValue', 'Distance'], ascending=[False,True], inplace=True)

        jbest.drop(dbest.columns[[0,1,2,3,5,7,8,11,15]], axis=1, inplace=True)
        jbest = jbest[['Shooter.Firstname', 'Shooter.Lastname', 'Shooter.Identification', 'FullValue', 'Distance']]
        jbest.index += 1
        jbest.rename(columns={'Shooter.Firstname' : 'Vorname', 'Shooter.Lastname' : 'Nachname', 'Shooter.Identification' : 'id' , 'FullValue' : 'Scheiben' , 'Distance' : 'Teiler'  }, inplace=True)
    else:
        jbest = pd.DataFrame(columns=['Position', 'Vorname', 'Nachname', 'Id', 'Scheibenanzahl', 'Teiler' ])

    return hbest, dbest, jbest


def preisschiessen(data):
    comp = data[data['MenuItem.MenuPointName'] == 'Preisschiessen']
    comp = comp[comp['DiscType'] == 'KKA']
    shooters = comp['Shooter.Identification'].unique()
    if comp.shape[0] == 0:
        return pd.DataFrame(columns=['Position', 'Vorname', 'Nachname', 'Id', 'Scheibenanzahl', 'Teiler' ])

    price = pd.DataFrame()
    for shooter in shooters:
        df = comp[comp['Shooter.Identification'] == shooter]
        max = df.loc[df['Distance'].idxmax()]
        max['DecValue'] = df['DecValue'].nlargest(2).sum()
        max['Distance'] = df['Distance'].nsmallest(2).sum()
        price = pd.concat([price, max.to_frame().transpose()], axis=0, ignore_index=True)
    
    price.sort_values(['DecValue', 'Distance'], ascending=[False,True], inplace=True)

    price.drop(price.columns[[0,1,2,3,5,7,8,11,15]], axis=1, inplace=True)
    price = price[['Shooter.Firstname', 'Shooter.Lastname', 'Shooter.Identification', 'FullValue', 'Distance']]
    price.index += 1
    price.rename(columns={'Shooter.Firstname' : 'Vorname', 'Shooter.Lastname' : 'Nachname', 'Shooter.Identification' : 'id' , 'FullValue' : 'Scheiben' , 'Distance' : 'Teiler'  }, inplace=True)

    return price
