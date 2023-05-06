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

        self.setWindowTitle("Anschiessen 2023 - Rönneburg")

        path = 'data/OUT-JSONInterface.log'
        self.ui.PfadEdit.setText(path)

        # clicks
        self.ui.onlinemode.clicked.connect(self.set_onlinepath)
        self.ui.localmode.clicked.connect(self.set_localpath)
        self.ui.debugmode.clicked.connect(self.enable_pfad_edit)
        self.ui.Act.clicked.connect(self.act_click)
        

    def set_onlinepath(self):
        self.ui.PfadEdit.setText('//DESKTOP-6RH80LH/Jsonlive/OUT-JSONInterface.log')

    def set_localpath(self):
        self.ui.PfadEdit.setText('data/OUT-JSONInterface.log')


    def enable_pfad_edit(self):
        self.ui.PfadEdit.setEnabled(True)

    def herren_click(self):
        path = self.ui.PfadEdit.text()
        data = bf.read_logfile2(path)
        lastUpdate = data['ShotDateTime'].max()
        self.ui.time.setText(lastUpdate)
        os.makedirs('backup', exist_ok=True)  
        data.to_csv('backup/full.csv')
        DataRes = pd.read_csv('backup/full.csv', index_col=0)   

        WettbewerbVogel = "KKA Vogelteil KKA"
        discVogel = "KKA"

        self.ui..setRowCount(0)
        resHaspa = bf.Best_Shot(DataRes,WettbewerbVogel,discVogel)
        resHaspa.to_csv('backup/haspa.csv', header=False)
        with open('backup/haspa.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                row = self.ui.VogelteilHTable.rowCount()
                self.ui.VogelteilHTable.insertRow(row)

                self.ui.VogelteilHTable.setItem(row,0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.VogelteilHTable.setItem(row,1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.VogelteilHTable.setItem(row,2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.VogelteilHTable.setItem(row,3, QtWidgets.QTableWidgetItem(line[3]))
                self.ui.VogelteilHTable.setItem(row,4, QtWidgets.QTableWidgetItem(line[4]))     


    def act_click(self):
        path = self.ui.PfadEdit.text()
        data = bf.read_logfile2(path)
        lastUpdate = data['ShotDateTime'].max()
        self.ui.time.setText(lastUpdate)
        os.makedirs('backup', exist_ok=True)  
        data.to_csv('backup/full.csv')
        DataRes = pd.read_csv('backup/full.csv', index_col=0)
        

        # Wettbewerb 1 Pokal (beste 10 Schuss)
        WettbewerbVogel = "KKA Pokal KKA"
        discVogel = "KKA"

        self.ui.P.setRowCount(0)
        res = bf.BestTenSeries(DataRes,WettbewerbVogel,discVogel)
        res.to_csv('backup/pokal.csv', header=False)
        with open('backup/pokal.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                row = self.ui.EhrenScheibeTable.rowCount()
                self.ui.EhrenScheibeTable.insertRow(row)

                self.ui.EhrenScheibeTable.setItem(row,0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.EhrenScheibeTable.setItem(row,1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.EhrenScheibeTable.setItem(row,2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.EhrenScheibeTable.setItem(row,3, QtWidgets.QTableWidgetItem(line[3]))
                self.ui.EhrenScheibeTable.setItem(row,4, QtWidgets.QTableWidgetItem(line[4]))
        # Wettbewerb 2 Ehrenpreise (beste 10en in Serie)
        self.ui.EhrenPreisTable.setRowCount(0)
        res = bf.BestTenSeries(DataRes,WettbewerbVogel,discVogel)
        res.to_csv('backup/ehrenpreis.csv', header=False)
        with open('backup/ehrenpreis.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                row = self.ui.EhrenPreisTable.rowCount()
                self.ui.EhrenPreisTable.insertRow(row)

                self.ui.EhrenPreisTable.setItem(row,0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.EhrenPreisTable.setItem(row,1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.EhrenPreisTable.setItem(row,2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.EhrenPreisTable.setItem(row,3, QtWidgets.QTableWidgetItem(line[3]))
                self.ui.EhrenPreisTable.setItem(row,4, QtWidgets.QTableWidgetItem(line[4]))

        # Wettbewerb 3 Haspa Orden
        WettbewerbHaspa = "KKA Haspa Offenne Klasse KKA"
        discHaspa = "KKA"
        zielteilerHaspa = 380

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

        # Wettbewerb 4 KK-Auflage
        WettbewerbKK = "KKA KK Preisschieen KKA"
        discKK = "KKA"
        anzKK = 2

        self.ui.KKAuflageTable.setRowCount(0)
        resKK = bf.best_tens(DataRes,WettbewerbKK,discKK,anzKK)
        resKK.to_csv('backup/kkauflage.csv', header=False)
        with open('backup/kkauflage.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                row = self.ui.KKAuflageTable.rowCount()
                self.ui.KKAuflageTable.insertRow(row)

                self.ui.KKAuflageTable.setItem(row,0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.KKAuflageTable.setItem(row,1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.KKAuflageTable.setItem(row,2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.KKAuflageTable.setItem(row,3, QtWidgets.QTableWidgetItem(line[3]))
                self.ui.KKAuflageTable.setItem(row,4, QtWidgets.QTableWidgetItem(line[4]))


        # Wettbewerb 5 LG - Auflage
        WettbewerbLG = "LGA LG Preisschieen LGA"
        discLG = "LGA"
        anzLG = 3

        self.ui.LGAuflageTable.setRowCount(0)
        resLGA = bf.BestXShots(DataRes,WettbewerbLG,discLG,anzLG)
        resLGA.to_csv('backup/LGAuflage.csv', header=False)
        with open('backup/LGAuflage.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                row = self.ui.LGAuflageTable.rowCount()
                self.ui.LGAuflageTable.insertRow(row)

                self.ui.LGAuflageTable.setItem(row,0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.LGAuflageTable.setItem(row,1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.LGAuflageTable.setItem(row,2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.LGAuflageTable.setItem(row,3, QtWidgets.QTableWidgetItem(line[3]))
                self.ui.LGAuflageTable.setItem(row,4, QtWidgets.QTableWidgetItem(line[4]))


    def damen_click(self):
        path = self.ui.PfadEdit.text()
        data = bf.read_logfile2(path)
        lastUpdate = data['ShotDateTime'].max()
        self.ui.time.setText(lastUpdate)
        os.makedirs('backup', exist_ok=True)  
        data.to_csv('backup/full.csv')
        DataRes = pd.read_csv('backup/full.csv', index_col=0)

        #Wettbewerb 1
        #Table : DamenvizeTable
        WettbewerbDamenVize = 'LGA Damenvizeorden LGA'
        discDamenVize = 'LGA'
        zielteilerDamenVize = 1107
        self.ui.DamenvizeTable.setRowCount(0)
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

sys.exit(app.exec_())