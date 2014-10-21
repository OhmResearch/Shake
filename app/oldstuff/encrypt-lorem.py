import gnupg
from time import gmtime, strftime

signer = 'user@user.com'
signer_pass = 'user'
#export_to = '133F8825CB21BAEF'
export_to = 'angelo.trivisonno@gmail.com'

input_file = 'lorem.txt'
output_file = 'to-'+export_to+'/'+input_file+'-'+strftime("%Y-%m-%d-%H%M%S", gmtime())+'.gpg'

gpg = gnupg.GPG(gnupghome='gpghome', verbose=True)

key_data = open('from-'+export_to+'/'+export_to+'.asc').read()
import_result = gpg.import_keys(key_data)


with open(input_file, 'rb') as f:
    status = gpg.encrypt_file(
        f, recipients=[export_to,signer],
        output=output_file,
	passphrase=signer_pass,
	sign=signer,
	always_trust=True)
