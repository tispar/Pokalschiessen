import sys 
import os  
import pandas as pd
import csv
from qtpy import QtWidgets
import backendfunctions as bf
from ui.mainwindow import Ui_MainWindow
# Bootup Routines
app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Pokalschießen 2022 - Rönneburg -- stable beta-Version")

        #check if backupfolder exists
        #check if backupfile exists
        #get maxdate from backupfile

        path = 'data/OUT-JSONInterface.log'
        self.ui.PfadEdit.setText(path)
        # data = bf.read_logfile2(path)
        # lastUpdate = data['ShotDateTime'].max()
        # print(lastUpdate)
        # os.makedirs('backup', exist_ok=True)  
        # data.to_csv('backup/full.csv')  

        # clicks
        self.ui.DemoButton.clicked.connect(self.demo_click)
        self.ui.PreisButton.clicked.connect(self.preis_click)
        self.ui.BestmannButton.clicked.connect(self.bestmann_click)
    
    def demo_click(self):
        print("Click")
        path = self.ui.PfadEdit.text()
        data = bf.read_logfile2(path)
        lastUpdate = data['ShotDateTime'].max()
        self.ui.time.setText(lastUpdate)
        os.makedirs('backup', exist_ok=True)  

        data.to_csv('backup/full.csv')  
        self.ui.oldiepokaltable.setRowCount(0)
        data = pd.read_csv('backup/full.csv', index_col=0)
        print("Datei wurde geladen")
        df1, df2, df3 = bf.oldiepokal(data)
        df1.to_csv('backup/oldies.csv', header=False)
        print("Datei wurde geschrieben")
        with open('backup/oldies.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                row = self.ui.oldiepokaltable.rowCount()
                self.ui.oldiepokaltable.insertRow(row)

                self.ui.oldiepokaltable.setItem(row,0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.oldiepokaltable.setItem(row,1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.oldiepokaltable.setItem(row,2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.oldiepokaltable.setItem(row,3, QtWidgets.QTableWidgetItem(line[3]))
                self.ui.oldiepokaltable.setItem(row,4, QtWidgets.QTableWidgetItem(line[4]))
                self.ui.oldiepokaltable.setItem(row,5, QtWidgets.QTableWidgetItem(line[5]))

    def preis_click(self):
        print("preis_click() called")
        path = self.ui.PfadEdit.text()
        data = bf.read_logfile2(path)
        lastUpdate = data['ShotDateTime'].max()
        self.ui.time.setText(lastUpdate)
        os.makedirs('backup', exist_ok=True)  

        data.to_csv('backup/full.csv')  
        self.ui.PreisTable.setRowCount(0)
        data = pd.read_csv('backup/full.csv', index_col=0)
        
        df = bf.preisschiessen(data)
        df.to_csv('backup/preis.csv', header=False)

        with open('backup/preis.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                row = self.ui.PreisTable.rowCount()
                self.ui.PreisTable.insertRow(row)

                self.ui.PreisTable.setItem(row,0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.PreisTable.setItem(row,1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.PreisTable.setItem(row,2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.PreisTable.setItem(row,3, QtWidgets.QTableWidgetItem(line[3]))
                self.ui.PreisTable.setItem(row,4, QtWidgets.QTableWidgetItem(line[4]))
                self.ui.PreisTable.setItem(row,5, QtWidgets.QTableWidgetItem(line[5]))


    def bestmann_click(self):
        print("bestmann_click() called")
        print("preis_click() called")
        path = self.ui.PfadEdit.text()
        data = bf.read_logfile2(path)
        os.makedirs('backup', exist_ok=True)  
        lastUpdate = data['ShotDateTime'].max()
        self.ui.time.setText(lastUpdate)

        data.to_csv('backup/full.csv')  
        self.ui.HerrenBestmann.setRowCount(0)
        self.ui.DamenBestmann.setRowCount(0)
        self.ui.JugendBestmann.setRowCount(0)

        data = pd.read_csv('backup/full.csv', index_col=0)

        her, dam, jug = bf.bestmann(data)
        her.to_csv('backup/herbest.csv', header=False)
        dam.to_csv('backup/dambest.csv', header=False)
        jug.to_csv('backup/jugbest.csv', header=False)

        with open('backup/herbest.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                row = self.ui.HerrenBestmann.rowCount()
                self.ui.HerrenBestmann.insertRow(row)

                self.ui.HerrenBestmann.setItem(row,0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.HerrenBestmann.setItem(row,1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.HerrenBestmann.setItem(row,2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.HerrenBestmann.setItem(row,3, QtWidgets.QTableWidgetItem(line[3]))
                self.ui.HerrenBestmann.setItem(row,4, QtWidgets.QTableWidgetItem(line[4]))
                self.ui.HerrenBestmann.setItem(row,5, QtWidgets.QTableWidgetItem(line[5]))
        
        with open('backup/dambest.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                row = self.ui.DamenBestmann.rowCount()
                self.ui.DamenBestmann.insertRow(row)

                self.ui.DamenBestmann.setItem(row,0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.DamenBestmann.setItem(row,1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.DamenBestmann.setItem(row,2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.DamenBestmann.setItem(row,3, QtWidgets.QTableWidgetItem(line[3]))
                self.ui.DamenBestmann.setItem(row,4, QtWidgets.QTableWidgetItem(line[4]))
                self.ui.DamenBestmann.setItem(row,5, QtWidgets.QTableWidgetItem(line[5]))

        with open('backup/jugbest.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                row = self.ui.JugendBestmann.rowCount()
                self.ui.JugendBestmann.insertRow(row)

                self.ui.JugendBestmann.setItem(row,0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.JugendBestmann.setItem(row,1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.JugendBestmann.setItem(row,2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.JugendBestmann.setItem(row,3, QtWidgets.QTableWidgetItem(line[3]))
                self.ui.JugendBestmann.setItem(row,4, QtWidgets.QTableWidgetItem(line[4]))
                self.ui.JugendBestmann.setItem(row,5, QtWidgets.QTableWidgetItem(line[5]))

window = MainWindow()

window.show()

sys.exit(app.exec_())