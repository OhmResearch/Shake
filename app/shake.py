import sys
import os
import time
from PyQt4 import QtGui, uic
from hurry.filesize import size
from PyQt4.QtCore import SIGNAL
from datetime import datetime
from time import gmtime, strftime
import gnupg
import threading
from PyQt4.Qt import *
from pprint import pprint
import json
import shutil

varGpgEncoding = 'utf-8'


class WriteNewMessage(QtGui.QWidget):
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi('shake_write.ui', self)
        self.btnAttach.setIcon(QtGui.QIcon('icon_paperclip.gif'))
        self.loadContacts()
        self.btnSend.clicked.connect(self.sendMessage)

    def sendMessage(self):
		gpg = gnupg.GPG(gnupghome="../config/gpg")
		gpg.encoding = varGpgEncoding
		subject = self.lineSubject.text()
		body = self.txtBody.toPlainText()
		varFrom = str(self.cboFrom.currentText())
		print varFrom
		varFrom = "Linux Trivisonno <3PT37WZ>"
		varTo = str(self.lineTo.text())
		print varTo
		unencrypted_string = unicode(str("From: "+varFrom+"\nTo: "+varTo+"\nSubject: "+subject+"\n\n"+body))
		print unencrypted_string
		nodeTo = 'BBZPN6Q'
		output_file = '../mailbox/to/'+nodeTo+'/-_-'+strftime("%Y-%m-%d-%H%M%S", gmtime())+'.txt.gpg'
		signer = 'BD3950A05D60D683029DF62F6DC351A20643F973'
		signer_pass = 'test'
		varFrom = 'BD3950A05D60D683029DF62F6DC351A20643F973'
		varTo = '4C7E91FBBF2FC5554E217A7B133F8825CB21BAEF'
		encrypted_data = gpg.encrypt(unencrypted_string, [varTo,varFrom],passphrase=signer_pass,sign=varFrom,always_trust=True)
		encrypted_string = str(encrypted_data)
		print 'ok: ', encrypted_data.ok
		print 'status: ', encrypted_data.status
		print 'stderr: ', encrypted_data.stderr
		print 'unencrypted_string: ', unencrypted_string
		print 'encrypted_string: ', encrypted_string
		fo = open(output_file, "wb")
		fo.write(encrypted_string);

		# Close opend file
		fo.close()
		
		ascii_armored_public_keys = gpg.export_keys(varFrom)
		with open('../mailbox/to/'+nodeTo+'/'+varFrom+'.asc', 'w') as f:
			f.write(ascii_armored_public_keys)

		self.close()
		window.loadAllMessages()

    def loadContacts(self):
    	gpg = gnupg.GPG(gnupghome="../config/gpg")
    	gpg.encoding = varGpgEncoding
    	privKeys = gpg.list_keys(True) # same as gpg.list_keys(True)   
    	varFrom =str(privKeys[0]["uids"]).decode('utf-8')
    	#print varFrom
    	print 'PRIVATE KEYS'
    	pprint(privKeys)
    	#self.cboFrom.addItem(varFrom) #have to figure out how to get rid of the brackets and the unicode
    	self.cboFrom.addItem("Linux Trivisonno <3PT37WZ>") #Remove when above problem is solved

    	pubKeys = gpg.list_keys() # same as gpg.list_keys(False)  
    	varTo=str(pubKeys[0]["uids"]).decode('utf-8')
    	print 'PUBLIC KEYS'
    	pprint(pubKeys)
    	
    	self.lineTo.setText("Angelo Trivisonno <BBZPN6Q>")


class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('shake.ui', self)
        self.show()
###########
	
	self.treeWidget.expandAll()

	
	self.tableWidget.setRowCount(1)
	self.tableWidget.horizontalHeader().setMovable(True)
	self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
	self.tableWidget.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
	self.tableWidget.setColumnHidden(4, True)
	#self.tableWidget.setSortingEnabled(0, False)
		
	self.tableWidget.selectionModel().currentChanged.connect(self.loadSingleMessage)
	#self.tableWidget.clicked.connect(self.loadSingleMessage)
	#self.connect(self.btnGetMessages,SIGNAL("clicked()"),lambda folder='from': self.loadAllMessages(folder))
	self.btnGetMessages.clicked.connect(self.loadAllMessages)
	#self.loadAllMessages('from')
	#self.connect(self.treeWidget,SIGNAL("itemSelectionChanged()"),lambda folder='from': self.loadAllMessages(folder))
	self.treeWidget.itemSelectionChanged.connect(self.loadAllMessages)
	self.treeWidget.itemSelectionChanged.connect(self.loadSingleMessage)
	self.treeWidget.clicked.connect(self.loadAllMessages)
	self.treeWidget.clicked.connect(self.loadSingleMessage)
	gpg = gnupg.GPG(gnupghome="../config/gpg")
	gpg.encoding = varGpgEncoding
	#print gpg.list_keys() # same as gpg.list_keys(False)
	#print gpg.list_keys(True) # True => private keys
	self.pushButton_5.clicked.connect(self.writeNewMessage)
	self.btnMsgDelete.clicked.connect(self.deleteMessage)

    def deleteMessage(self):
		deleteFileSrc = str(self.tableWidget.item(self.tableWidget.currentRow(), 4).text())
		deleteFile = deleteFileSrc.replace('../mailbox/','')
		directoryFile = '../mailbox/trash/'+os.path.dirname(deleteFile)
		copyFileTo = '../mailbox/trash/'+deleteFile
		print deleteFileSrc
		print copyFileTo	
		#print deleteFile

		if not os.path.exists(copyFileTo):
			os.makedirs(copyFileTo)
		shutil.move(deleteFileSrc,copyFileTo)
		self.loadAllMessages()

    def loadAllMessages(self):
		self.plainTextEdit_3.clear()
		getSelected = self.treeWidget.selectedItems()
		if getSelected:
			baseNode = getSelected[0]
			print self.treeWidget.indexFromItem(baseNode)
			getChildNode = baseNode.text(0)
			folder = str(getChildNode)
			#print itmIndex

		print folder
		#item = self.treeWidget.currentItem()
		#folder = str(folder)
		import fnmatch
		import os
		import os.path
		if (folder=='Inbox'): 
			folder = 'from'
			self.tableWidget.horizontalHeaderItem(2).setText('From')
		if (folder=='Sent'): 
			folder = 'to'
			self.tableWidget.horizontalHeaderItem(2).setText('To')
		if (folder=='Trash'): 
			folder = 'trash'
			self.tableWidget.horizontalHeaderItem(2).setText('From')
		if (folder=='Drafts'): 
			folder = 'drafts'
			self.tableWidget.horizontalHeaderItem(2).setText('To')
		matches = []
		i=0
		path = '../mailbox/'+folder
		print path
		count = 0
		for root, dirnames, filenames in os.walk('../mailbox/'+folder):
			for filename in fnmatch.filter(filenames, '*.gpg'):
				count += 1

		self.tableWidget.setRowCount(count)
		self.label_5.setText("Total: "+str(count))
		self.label_6.setText("Unread: 0")
		self.label_7.setText("Folder Size: "+size(self.getFolderSize('../mailbox/'+folder))+"B   All Folders: "+size(self.getFolderSize('../mailbox')))
		for root, dirnames, filenames in os.walk('../mailbox/'+folder):
			for filename in fnmatch.filter(filenames, '*.gpg'):
				matches.append(os.path.join(root, filename))
				#print os.path.join(root, filename)

				## slice up the string to get the sender node ID
				print 'FILENAME= '+filename
				sender = root
				print 'ROOT= '+root
				sender = sender.replace('../mailbox/to/','') # remove the ../mailbox portion of the string
				sender = sender.replace('../mailbox/from/','') # remove the ../mailbox portion of the string
				sender = sender.replace('../mailbox/trash/to/','')
				sender = sender.replace('../mailbox/trash/from/','')
				sender = sender.replace('/'+filename,'') #for some reason, when viewing trash, the root variable also includes the filename, so we need to delete that text from the string
				print 'SENDER= '+sender
				## 

				##
				# split the string to get the timestamp
				timestamp = filename
				timestamp = timestamp[3:-8] # 2014-09-14-195006
				timestamp = time.strptime(timestamp, '%Y-%m-%d-%H%M%S')
				timestampstr = strftime('%m/%d/%y, %I:%M %p',timestamp)
				print timestampstr
				# eventually be able to offset the time based on system settings
				# http://stackoverflow.com/questions/1111056/get-time-zone-information-of-the-system-in-python
				#
				
				self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(u"\u2022"))
				self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem('(encrypted)'))
				self.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem(sender))
				self.tableWidget.setItem(i, 3, QtGui.QTableWidgetItem(timestampstr))
				self.tableWidget.setItem(i, 4, QtGui.QTableWidgetItem(str(os.path.join(root, filename))))
				i += 1
		#self.loadSingleMessage()


	
    def loadSingleMessage(self):
	
		print self.tableWidget.item(self.tableWidget.currentRow(), 4).text()
		#file = open('lorem.txt-2014-09-13-235300.gpg', 'r')
		file = open(self.tableWidget.item(self.tableWidget.currentRow(), 4).text(), 'r')
		file_contents = file.read()
		
		start_time = time.time()
		#Begin GPG decryption
		gpg = gnupg.GPG(gnupghome="../config/gpg")
		gpg.encoding = varGpgEncoding
		file_contents = gpg.decrypt(file_contents, always_trust=True, passphrase='test')
		#print 'ok: ', file_contents.ok
		#print 'status: ', file_contents.status
		stderr_output = str(file_contents.stderr)
		#print 'stderr: ', stderr_output
		#print 'decrypted string: ', file_contents.data
		file_contents_str = str(file_contents)
		file_contents_str = file_contents_str.encode('utf-8').strip()
		if not file_contents_str: file_contents_str = str(file_contents.stderr)
		self.plainTextEdit_3.clear()

		goodsig_start = stderr_output.find("Good signature")
		goodsig_end = stderr_output.find("[GNUPG:] VALIDSIG")
		goodsig_alert = stderr_output[goodsig_start:goodsig_end]

		self.plainTextEdit_3.insertPlainText(goodsig_alert)
		self.plainTextEdit_3.insertPlainText(file_contents_str)
		timer = str(time.time() - start_time)
		timer = timer[:5] + ' seconds'
		print timer


    def getRowID(self):
		row = self.tableWidget.currentItem().row()
		col = self.tableWidget.currentItem().column()

		message = self.tableWidget.item(row,col).text()
		
		self.plainTextEdit_3.clear()
		self.plainTextEdit_3.insertPlainText(message)

    def getFolderSize(self,folder):
		total_size = os.path.getsize(folder)
		for item in os.listdir(folder):
			itempath = os.path.join(folder, item)
			if os.path.isfile(itempath):
			    total_size += os.path.getsize(itempath)
			elif os.path.isdir(itempath):
			    total_size += self.getFolderSize(itempath)
		return total_size

    def writeNewMessage(self):
		print "Opening a new Write Message window..."
		self.w = WriteNewMessage()
		self.w.show()

###########


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
