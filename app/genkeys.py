import os
import gnupg

from Tkinter import *

def show_entry_fields():
	gpg = gnupg.GPG(gnupghome='../config/gpg', verbose=True)
	input_data = gpg.gen_key_input(
	    	name_email=e1.get(),
	    	passphrase=e4.get(),
		key_length=e3.get(),
		name_real=e2.get())
	key = gpg.gen_key(input_data)
	print key

	ascii_armored_public_keys = gpg.export_keys(key)
	ascii_armored_private_keys = gpg.export_keys(key, True)
	with open(e1.get()+'.asc', 'w') as f:
	    f.write(ascii_armored_public_keys)
	    f.write(ascii_armored_private_keys)


master = Tk()
master.wm_title("Generate New Node Keys | Shake")
Label(master, text="Node").grid(row=0)
Label(master, text="Name").grid(row=1)
Label(master, text="Key Length").grid(row=2)
Label(master, text="Passphrase").grid(row=3)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0, column=1, padx=10)
e2.grid(row=1, column=1, padx=10)
e3.grid(row=2, column=1, padx=10)
e4.grid(row=3, column=1, padx=10)

Button(master, text='Generate New PGP Keys', command=show_entry_fields).grid(row=5, column=0, sticky=W, pady=10, padx=4)
Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=10, padx=4)

mainloop()
