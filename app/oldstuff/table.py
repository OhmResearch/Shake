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

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    t = Table()
    t.show()
    sys.exit(app.exec_())
