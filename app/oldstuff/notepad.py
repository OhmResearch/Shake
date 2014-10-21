#! /usr/bin/python

import sys
import os
from PyQt4 import QtGui

class Table(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        layout = QtGui.QGridLayout() 
        self.led = QtGui.QLineEdit("Sample")
        self.table = QtGui.QTableWidget()
	self.table.setRowCount(5)
	self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([u"\u2605", u"\U0001F4CE", 'Subject', 'From', 'Date'])
        self.table.setVerticalHeaderLabels(['', '', '', '', ''])
	self.table.setSortingEnabled(True)
	layout.addWidget(self.led, 0, 0)
	layout.addWidget(self.table, 1, 0)
	self.table.setItem(0, 3, QtGui.QTableWidgetItem('Cindy Chiudioni'))
	self.table.setItem(1, 3, QtGui.QTableWidgetItem('Jessica Luczywo'))
	self.table.setItem(2, 3, QtGui.QTableWidgetItem('Jessica Luczywo'))
	self.table.setItem(3, 3, QtGui.QTableWidgetItem('Cindy Chiudioni'))
	self.table.setItem(4, 3, QtGui.QTableWidgetItem('Jessica Luczywo'))
        self.setLayout(layout)
    	self.setGeometry(30,30,800,500)

class Notepad(QtGui.QMainWindow):

    def __init__(self):
        super(Notepad, self).__init__()
        self.initUI()
        
    def initUI(self):
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
        
        self.text = QtGui.QTextEdit(self)
        
        self.setCentralWidget(self.text)
        self.setGeometry(300,300,700,300)
        self.setWindowTitle('Notepad')
        
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
    notepad = Notepad()
    notepad.show()
    t = Table()
    t.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()


