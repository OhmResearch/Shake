import os
import gnupg


key = "BD3950A05D60D683029DF62F6DC351A20643F973"
node = "3TP37WZ"

gpg = gnupg.GPG(gnupghome='../config/gpg', verbose=True)

key_data = open(node+'.asc').read()
import_result = gpg.import_keys(key_data)
