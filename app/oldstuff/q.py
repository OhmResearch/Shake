import sys
from PyQt4 import QtGui


lista = ['aa', 'ab', 'ac']
listb = ['ba', 'bb', 'bc']
listc = ['ca', 'cb', 'cc']
mystruct = {'A':lista, 'B':listb, 'C':listc}

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.table = QtGui.QTableWidget(5,5)
        self.table.setHorizontalHeaderLabels([u"\u2605", u"\U0001F4CE", 'Subject', 'From', 'Date'])
        self.table.setVerticalHeaderLabels(['', '', '', '', ''])
	self.table.setSortingEnabled(True)
        self.table.horizontalHeader().sectionDoubleClicked.connect(self.changeHorizontalHeader)


        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)
	self.initUI()

    def initUI(self):
    	self.setGeometry(300,300,300,300)
      	self.setWindowTitle('Notepad')
     	self.show() 

    def changeHorizontalHeader(self, index):
        oldHeader = self.table.horizontalHeaderItem(index).text()
        newHeader, ok = QtGui.QInputDialog.getText(self,
                                                      'Change header label for column %d' % index,
                                                      'Header:',
                                                       QtGui.QLineEdit.Normal,
                                                       oldHeader)
        if ok:
            self.table.horizontalHeaderItem(index).setText(newHeader)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = MyWindow()
	
    main.show()

    sys.exit(app.exec_())
