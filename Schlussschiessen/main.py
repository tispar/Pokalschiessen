import sys 
import os  
import pandas as pd
import csv
from qtpy import QtWidgets
import backendfunctions as bf
from ui.mainwindow import Ui_MainWindow
import warnings
warnings.filterwarnings("ignore")

# Bootup Routines
app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Schlussschiessen 2022 - Rönneburg -- stable beta-Version")

        path = 'data/OUT-JSONInterface.log'
        self.ui.PfadEdit.setText(path)

        # clicks
        self.ui.onlinemode.clicked.connect(self.set_onlinepath)
        self.ui.localmode.clicked.connect(self.set_localpath)
        self.ui.debugmode.clicked.connect(self.enable_pfad_edit)
        self.ui.DamenAct.clicked.connect(self.damen_click)

    def set_onlinepath(self):
        self.ui.PfadEdit.setText('//DESKTOP-6RH80LH/Jsonlive/OUT-JSONInterface.log')

    def set_localpath(self):
        self.ui.PfadEdit.setText('data/OUT-JSONInterface.log')


    def enable_pfad_edit(self):
        self.ui.PfadEdit.setEnabled(True)

    def damen_click(self):
        path = self.ui.PfadEdit.text()
        data = bf.read_logfile2(path)
        lastUpdate = data['ShotDateTime'].max()
        self.ui.time.setText(lastUpdate)
        os.makedirs('backup', exist_ok=True)  
        data.to_csv('backup/full.csv')

        #Wettbewerb 1
        #Table : DamenvizeTable
        WettbewerbDamenVize = 'LGA Damenvizeorden LGA'
        discDamenVize = 'LGA'
        zielteilerDamenVize = 1107
        self.ui.DamenvizeTable.setRowCount(0)
        DataRes = pd.read_csv('backup/full.csv', index_col=0)
        resDamenVize = bf.Teiler_All(DataRes, zielteilerDamenVize, WettbewerbDamenVize, discDamenVize)
        resDamenVize.to_csv('backup/DVize.csv', header=False)
        with open('backup/DVize.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                row = self.ui.DamenvizeTable.rowCount()
                self.ui.DamenvizeTable.insertRow(row)

                self.ui.DamenvizeTable.setItem(row,0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.DamenvizeTable.setItem(row,1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.DamenvizeTable.setItem(row,2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.DamenvizeTable.setItem(row,3, QtWidgets.QTableWidgetItem(line[3]))
                self.ui.DamenvizeTable.setItem(row,4, QtWidgets.QTableWidgetItem(line[4]))


        #Wettbewerb 2
        WettbewerbHaspa = "KKA Haspa Offenne Klasse KKA"
        discHaspa = "KKA"
        zielteilerHaspa = 380
        print('check')
        self.ui.HaspaTable.setRowCount(0)
        resHaspa = bf.Teiler_One(DataRes,zielteilerHaspa,WettbewerbHaspa,discHaspa)
        resHaspa.to_csv('backup/haspa.csv', header=False)
        with open('backup/haspa.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                row = self.ui.HaspaTable.rowCount()
                self.ui.HaspaTable.insertRow(row)

                self.ui.HaspaTable.setItem(row,0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.HaspaTable.setItem(row,1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.HaspaTable.setItem(row,2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.HaspaTable.setItem(row,3, QtWidgets.QTableWidgetItem(line[3]))
                self.ui.HaspaTable.setItem(row,4, QtWidgets.QTableWidgetItem(line[4]))
        #Wettbewerb 3
        WettbewerbVogel = "KKA Damen Vogelteil KKA"
        discVogel = "KKA"

        self.ui.VogelteilDTable.setRowCount(0)
        resHaspa = bf.Best_Shot(DataRes,WettbewerbVogel,discVogel)
        resHaspa.to_csv('backup/haspa.csv', header=False)
        with open('backup/haspa.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                row = self.ui.VogelteilDTable.rowCount()
                self.ui.VogelteilDTable.insertRow(row)

                self.ui.VogelteilDTable.setItem(row,0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.VogelteilDTable.setItem(row,1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.VogelteilDTable.setItem(row,2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.VogelteilDTable.setItem(row,3, QtWidgets.QTableWidgetItem(line[3]))
                self.ui.VogelteilDTable.setItem(row,4, QtWidgets.QTableWidgetItem(line[4]))

window = MainWindow()

window.show()

#print("Loop here ?")

sys.exit(app.exec_())