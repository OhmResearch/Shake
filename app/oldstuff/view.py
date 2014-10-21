#! /usr/bin/python

import sys
import os
from PyQt4 import QtGui


class Shake(QtGui.QMainWindow):

    def __init__(self):
        super(Shake, self).__init__()
        self.initUI()
        
    def initUI(self):
        layout = QtGui.QGridLayout() 

        newAction = QtGui.QAction('New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Create new file')
        newAction.triggered.connect(self.newFile)
        
        saveAction = QtGui.QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save current file')
        saveAction.triggered.connect(self.saveFile)
        
        openAction = QtGui.QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a file')
        openAction.triggered.connect(self.openFile)
        
        closeAction = QtGui.QAction('Close', self)
        closeAction.setShortcut('Ctrl+Q')
        closeAction.setStatusTip('Close Notepad')
        closeAction.triggered.connect(self.close)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(closeAction)
        
        self.led = QtGui.QLineEdit("Sample")
        self.text = QtGui.QTextEdit()
        self.table = QtGui.QTableWidget()
	self.table.setRowCount(5)
	self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([u"\u2605", u"\U0001F4CE", 'Subject', 'From', 'Date'])
        self.table.setVerticalHeaderLabels(['', '', '', '', ''])
	self.table.setSortingEnabled(True)

	layout.addWidget(self.led, 0, 0)
	layout.addWidget(self.table, 1, 0)
	layout.addWidget(self.text, 2, 0)

	self.table.setItem(0, 3, QtGui.QTableWidgetItem('Cindy Chiudioni'))
	self.table.setItem(1, 3, QtGui.QTableWidgetItem('Jessica Luczywo'))
	self.table.setItem(2, 3, QtGui.QTableWidgetItem('Jessica Luczywo'))
	self.table.setItem(3, 3, QtGui.QTableWidgetItem('Cindy Chiudioni'))
	self.table.setItem(4, 3, QtGui.QTableWidgetItem('Jessica Luczywo'))
        
        #self.setCentralWidget(self.text)
        self.led.setGeometry(30,30,700,300)
        self.table.setGeometry(100,50,700,300)
        self.text.setGeometry(300,80,700,300)
        self.setWindowTitle('Notepad')
	self.led.show()
	self.table.show()
	self.text.show()
	
        
    def newFile(self):
        self.text.clear()
        
    def saveFile(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        f = open(filename, 'w')
        filedata = self.text.toPlainText()
        f.write(filedata)
        f.close()
        
        
    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        f = open(filename, 'r')
        filedata = f.read()
        self.text.setText(filedata)
        f.close()
        
def main():
    app = QtGui.QApplication(sys.argv)
    shake = Shake()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
