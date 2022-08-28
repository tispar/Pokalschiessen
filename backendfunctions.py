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
    with open(path, 'r', encoding='utf8', errors='ignore') as log:
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
    best.sort_values(['DecValue', 'Distance'], ascending=[False,True], inplace=True)
    oldies.sort_values(['TotalDistance'], ascending=True, inplace=True)
    u65.sort_values(['TotalDistance'], ascending=True, inplace=True)

    #resetting indexes
    best.reset_index(inplace=True)
    oldies.reset_index(inplace=True)
    u65.reset_index(inplace=True)

    return best, oldies, u65


