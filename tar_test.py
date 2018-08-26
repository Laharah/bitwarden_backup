import os
import subprocess

path = '/home/jaredanderson/Documents/code/offsite_backup'
with open('temp', 'wb') as output:
    in_fd, out_fd = os.pipe()
    tar = subprocess.Popen(f'tar cv {path}'.split(), stdout=-1)
    with subprocess.Popen(f'gpg -c --cipher-algo AES256 --passphrase-fd {in_fd}'.split(), stdin=tar.stdout, stdout=output, pass_fds=[in_fd]) as gpg:
        os.close(in_fd)
        with open(out_fd, 'w') as of:
            of.write('123')
