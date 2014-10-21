import gnupg
from time import gmtime, strftime
from Tkinter import *



signer = 'BBZPN6Q'

def show_entry_fields():
	gpg = gnupg.GPG(gnupghome='../config/gpg', verbose=True)
	recipient = e1.get()
	message_file = '../mailbox/drafts/'+recipient+'/'+e2.get()
	passphrase = e3.get()
	output_file = '../mailbox/to/'+recipient+'/'+e2.get()+'-'+strftime("%Y-%m-%d-%H%M%S", gmtime())+'.txt.gpg'

	# get user's current GPG keys for the signature
	key_data = open('../config/gpg/mykeys.asc').read()
	import_result = gpg.import_keys(key_data)

	# get recipient's current GPG keys for encryption
	key_data = open('../mailbox/from/'+recipient+'/'+recipient+'.asc').read()
	import_result = gpg.import_keys(key_data)
	

	with open(message_file, 'rb') as f:
	    status = gpg.encrypt_file(
		f, recipients=[recipient,signer],
		output=output_file,
		passphrase=passphrase,
		sign=signer,
		always_trust=True)


master = Tk()
master.geometry("800x500")
master.wm_title("Compose New Message | Shake")
Label(master, text="Node ID").grid(row=0)
Label(master, text="Message").grid(row=1)
Label(master, text="Passphrase").grid(row=2)

e1 = Entry(master)
e1.insert(END,'GGZPN6Q')  # insert default text into the entry widget (text box)
e2 = Text(master, borderwidth=3, relief="sunken", height=10, width=55)
e2.config(font=("Arial", 12), undo=True, wrap='word')
e3 = Entry(master)

e1.grid(row=0, column=1, padx=10)
e2.grid(row=1, column=1, padx=10)
e3.grid(row=2, column=1, padx=10)

Button(master, text='Send Message', command=show_entry_fields).grid(row=5, column=0, sticky=W, pady=10, padx=4)
Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=10, padx=4)

mainloop()
