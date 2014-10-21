import os
import gnupg


key = "BD3950A05D60D683029DF62F6DC351A20643F973"
node = "3TP37WZ"

gpg = gnupg.GPG(gnupghome='../config/gpg', verbose=True)

ascii_armored_public_keys = gpg.export_keys(key)
ascii_armored_private_keys = gpg.export_keys(key, True)

with open(node+'.asc', 'w') as f:
	f.write(ascii_armored_public_keys)
	f.write(ascii_armored_private_keys)