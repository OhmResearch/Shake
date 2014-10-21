import sys
import os
from PyQt4 import QtGui, uic

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('shake.ui', self)
        self.show()
###########
	
	self.treeWidget.expandAll()
	
	
        self.tableWidget.setRowCount(5)
	self.tableWidget.horizontalHeader().setMovable(True)
	self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

	self.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem('New home for AT lorem ipsum contra hoover'))
	self.tableWidget.setItem(1, 0, QtGui.QTableWidgetItem('New home for JL'))
	self.tableWidget.setItem(2, 0, QtGui.QTableWidgetItem('New home for AT'))

	self.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem('Cindy Chiudioni'))
	self.tableWidget.setItem(1, 1, QtGui.QTableWidgetItem('Jessica Luczywo'))
	self.tableWidget.setItem(2, 1, QtGui.QTableWidgetItem('Cindy Chiudioni'))

	self.tableWidget.setItem(0, 2, QtGui.QTableWidgetItem('9/14/14, 6:05 PM'))
	self.tableWidget.setItem(1, 2, QtGui.QTableWidgetItem('9/12/14, 6:05 PM'))
	self.tableWidget.setItem(2, 2, QtGui.QTableWidgetItem('10/14/13, 6:05 PM'))

	self.tableWidget.clicked.connect(self.getRowID)
	self.label_5.setText("Total: 5")
	self.label_6.setText("Unread: 5")
	self.label_7.setText("Space Used: "+self.getFolderSize("."))
	
	

    def getRowID(self):
	row = self.tableWidget.currentItem().row()
	col = self.tableWidget.currentItem().column()

	message = self.tableWidget.item(row,col).text()
	
	self.plainTextEdit_3.clear()
	self.plainTextEdit_3.insertPlainText(message)

    def getFolderSize(self, folder):
	total_size = os.path.getsize(folder)
	for item in os.listdir(folder):
		itempath = os.path.join(folder, item)
		if os.path.isfile(itempath):
		    total_size += os.path.getsize(itempath)
		elif os.path.isdir(itempath):
		    total_size += getFolderSize(itempath)
	return str(total_size)


    def loadMessages(self):
	with open('lorem.txt', 'r') as content_file:
    		content = content_file.read()

###########


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
