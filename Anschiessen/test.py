import pandas as pd
import PySimpleGUI as sg

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                   'Age': [25, 32, 18, 47],
                   'Gender': ['F', 'M', 'M', 'M']})

layout = [[sg.Table(values=df.values.tolist(),
                     headings=df.columns.tolist(),
                     max_col_width=25,
                     auto_size_columns=True,
                     justification='center',
                     num_rows=min(25, len(df)))],
          [sg.Button('Exit')]]

window = sg.Window('Dataframe Viewer', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()